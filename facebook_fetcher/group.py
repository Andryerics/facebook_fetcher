import re
import requests
from bs4 import BeautifulSoup as bs4
import logging

class Group:
    def __init__(self, groupname, requests_session):
        self.__grp = groupname
        self.__session = requests_session
        self.__host = "https://mobile.facebook.com/groups"

        try:
            self.__req = self.__session.get(self.__host + '/' + str(groupname) + '?view=info', timeout=10)
            self.__req.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Failed to retrieve group info: {e}")
            raise

        self.__res = bs4(self.__req.text, 'html.parser')

        if self.__res.find('a', href=re.compile('\/home\.php\?rand=\d+')):
            raise Exception(f"Groupe avec le nom \"{groupname}\" non trouvé!")

        self.__group_info = {
            'infos' : {
                'name': self.__extract_group_name(),
                'type': self.__extract_group_type(),
                'members': self.__extract_group_members(),
                'photos': self.__extract_group_photos(),
                'files': self.__extract_group_files()
            },
            'admins': [],
            'members_list': []
        }

        self.fetch_members()

    def __extract_group_name(self):
        group_name_type_container = self.__res.find('div', class_='bk bl')
        if group_name_type_container:
            name_tag = group_name_type_container.find('h1')
            return name_tag.get_text(strip=True) if name_tag else None
        return None

    def __extract_group_type(self):
        group_name_type_container = self.__res.find('div', class_='bk bl')
        if group_name_type_container:
            type_tag = group_name_type_container.find('div', class_='br bs')
            return type_tag.get_text(strip=True) if type_tag else None
        return None

    def __extract_group_members(self):
        members_tag = self.__res.find('a', href=re.compile(r'view=members.*'))
        if members_tag:
            members_count = members_tag.find_next('span', class_='by bz')
            return int(members_count.get_text(strip=True).replace(',', '')) if members_count else 0
        return 0

    def __extract_group_photos(self):
        photos_tag = self.__res.find('a', href=re.compile(r'view=photos.*'))
        if photos_tag:
            photos_count = photos_tag.find_next('span', class_='by bz')
            return int(photos_count.get_text(strip=True).replace(',', '')) if photos_count else 0
        return 0

    def __extract_group_files(self):
        files_tag = self.__res.find('a', href=re.compile(r'view=files.*'))
        if files_tag:
            files_count = files_tag.find_next('span', class_='by bz')
            return int(files_count.get_text(strip=True).replace(',', '')) if files_count else 0
        return 0

    def fetch_members(self):
        print("Récupération du lien des membres...")
        members_link_tag = self.__res.find('a', href=re.compile(r'view=members.*'))
        if not members_link_tag:
            print("Lien des membres non trouvé.")
            raise Exception("Impossible de trouver le lien des membres.")
        members_link = members_link_tag['href']
        members_url = "https://mbasic.facebook.com" + members_link
        print(f"Lien des membres : {members_url}")

        members_req = self.__session.get(members_url)
        if members_req.status_code != 200:
            print(f"Erreur lors de la requête des membres : {members_req.status_code}")
            raise Exception("Erreur lors de la requête des membres.")
        members_res = bs4(members_req.text, 'html.parser')

        admins, members = self.__extract_members(members_res)

        self.__group_info['admins'] = admins
        self.__group_info['members_list'] = members

        # Fetch all admins by following the "Voir tout" link
        all_admins = self.__fetch_all_admins(members_res)
        self.__group_info['admins'].extend(all_admins)

        # Fetch all members by following the "Voir tout" link
        all_members = self.__fetch_all_members(members_res)
        self.__group_info['members_list'].extend(all_members)

        return admins, members

    def __extract_members(self, soup):
        admins = []
        members = []

        # Extract admins and moderators
        print("Extraction des administrateurs et modérateurs...")
        sections = soup.find_all('div')
        for section in sections:
            if section.find('h3'):
                tables = section.find_all('table')
                if tables:
                    for table in tables:
                        member_info = self.__parse_member_info(table)
                        if member_info:
                            if "Admin" in member_info.get('role', '') or "Mod" in member_info.get('role', ''):
                                admins.append(member_info)
                            else:
                                members.append(member_info)
        print(f"Nombre d'administrateurs trouvés : {len(admins)}")
        print(f"Nombre de membres trouvés : {len(members)}")

        return admins, members

    def __fetch_all_admins(self, soup):
        print("Récupération de tous les administrateurs...")
        voir_tout_link_tag = soup.find('a', href=re.compile(r'listType=list_admin_moderator.*'))
        if not voir_tout_link_tag:
            print("Lien 'Voir tout' des administrateurs non trouvé.")
            return []

        voir_tout_link = voir_tout_link_tag['href']
        voir_tout_url = "https://mbasic.facebook.com" + voir_tout_link
        print(f"Lien 'Voir tout' des administrateurs : {voir_tout_url}")

        voir_tout_req = self.__session.get(voir_tout_url)
        if voir_tout_req.status_code != 200:
            print(f"Erreur lors de la requête 'Voir tout' des administrateurs : {voir_tout_req.status_code}")
            return []

        voir_tout_res = bs4(voir_tout_req.text, 'html.parser')
        all_admins = []

        admin_tables = voir_tout_res.find_all('table')
        for table in admin_tables:
            admin_info = self.__parse_member_info(table)
            if admin_info:
                all_admins.append(admin_info)
        print(f"Nombre total d'administrateurs trouvés : {len(all_admins)}")

        return all_admins

    def __fetch_all_members(self, soup):
        print("Récupération de tous les membres...")
        voir_tout_link_tag = soup.find('a', href=re.compile(r'listType=list_nonfriend_nonadmin.*'))
        if not voir_tout_link_tag:
            print("Lien 'Voir tout' des membres non trouvé.")
            return []

        voir_tout_link = voir_tout_link_tag['href']
        voir_tout_url = "https://mbasic.facebook.com" + voir_tout_link
        print(f"Lien 'Voir tout' des membres : {voir_tout_url}")

        voir_tout_req = self.__session.get(voir_tout_url)
        if voir_tout_req.status_code != 200:
            print(f"Erreur lors de la requête 'Voir tout' des membres : {voir_tout_req.status_code}")
            return []

        voir_tout_res = bs4(voir_tout_req.text, 'html.parser')
        all_members = []

        member_tables = voir_tout_res.find_all('table')
        for table in member_tables:
            member_info = self.__parse_member_info(table)
            if member_info:
                all_members.append(member_info)
        print(f"Nombre total de membres trouvés : {len(all_members)}")

        return all_members

    def __parse_member_info(self, table):
        member_info = {}
        img_tag = table.find('img')
        name_tag = table.find('a', href=True)
        join_date_tag = table.find('abbr')
        if img_tag and name_tag and join_date_tag:
            member_info['name'] = name_tag.get_text(strip=True)
            member_info['profile_picture'] = img_tag['src']
            profile_link = name_tag['href']
            if profile_link.startswith('/'):
                profile_link = 'https://www.facebook.com' + profile_link.split('?')[0]  # Split to remove query parameters
            member_info['profile_link'] = profile_link
            member_info['joined'] = join_date_tag.get_text(strip=True)
            # Role determination based on the context of the table, which is more generic
            parent_section = table.find_previous('h3')
            if parent_section and ("Admin" in parent_section.text or "Mod" in parent_section.text):
                member_info['role'] = "Admin/Mod"
            else:
                member_info['role'] = "Member"
            return member_info
        return None



    def __str__(self):
        return f"Facebook Group : name={self.__group_info['name']}, type={self.__group_info['type']}"

    def __repr__(self):
        return f"Facebook Group : name={self.__group_info['name']}, type={self.__group_info['type']}"

    def __getitem__(self, key):
        return self._group_info[key] if key in self._group_info.keys() else None

    @property
    def _group_info(self):
        return self.__group_info.copy()

    def refresh(self):
        self.__init__(groupname=self.__grp, requests_session=self.__session)
        return True

    def get(self, item):
        return self[item]


