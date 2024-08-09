import re
import requests
from bs4 import BeautifulSoup as bs4
import json
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Pub:
    def __init__(self, pubid, requests_session):
        self.__usr = pubid
        self.__session = requests_session
        self.__host = "https://mbasic.facebook.com/"
        self.__url = self.__host + pubid

        logging.info("Initializing Pub object with pubid: %s", pubid)
        logging.debug("Constructed URL: %s", self.__url)

        self.__pub_info = {}

        try:
            self.__req = self.__session.get(self.__url)
            self.__req.raise_for_status()
            self.__res = bs4(self.__req.text, 'html.parser')

            logging.debug("HTTP GET request to %s returned status code %s", self.__url, self.__req.status_code)

            if self.__res.find('a', href=re.compile(r'\/home\.php\?rand=\d+')):
                raise ValueError(f"Évènement avec l'ID \"{pubid}\" n'a pas été trouvé!")

            self.__parse_pub_info()

        except requests.exceptions.RequestException as e:
            logging.error("HTTP request error: %s", e)
            self.__pub_info = {"error": f"HTTP request error: {str(e)}"}
        except Exception as e:
            logging.error("An error occurred: %s", e)
            self.__pub_info = {"error": f"An error occurred: {str(e)}"}

    def __parse_pub_info(self):
        try:
            # Extract user name
            user_name_tag = self.__res.find('h3', class_='be bf bg bh')
            user_name = user_name_tag.get_text(strip=True) if user_name_tag else None
            logging.debug("User name extracted: %s", user_name)

            # Extract user profile link
            user_profile_link_tag = user_name_tag.find('a') if user_name_tag else None
            user_profile_link = self.__host + user_profile_link_tag['href'] if user_profile_link_tag else None
            logging.debug("User profile link extracted: %s", user_profile_link)

            # Extract publication date and privacy
            date_tag = self.__res.find('abbr')
            date = date_tag.get_text(strip=True) if date_tag else None
            logging.debug("Publication date extracted: %s", date)

            privacy_tag = date_tag.find_next_sibling('span') if date_tag else None
            privacy = privacy_tag.get_text(strip=True) if privacy_tag else None
            logging.debug("Privacy setting extracted: %s", privacy)

            # Extract post content
            content_tag = self.__res.find('div', class_='bi')
            content = content_tag.get_text(strip=True) if content_tag else None
            logging.debug("Post content extracted: %s", content)

            # Extract image
            image_tag = self.__res.find('img', class_='r')
            image_url = image_tag['src'] if image_tag else None
            logging.debug("Image URL extracted: %s", image_url)

            # Extract reactions
            reactions_tag = self.__res.find('div', class_='cu cv')
            reactions = reactions_tag.get_text(strip=True) if reactions_tag else None
            logging.debug("Reactions extracted: %s", reactions)

            # Extract comments
            comments = []
            comment_tags = self.__res.find_all('div', class_='dw')
            for comment_tag in comment_tags:
                comment_author_tag = comment_tag.find('h3')
                comment_author = comment_author_tag.get_text(strip=True) if comment_author_tag else None

                comment_content_tag = comment_tag.find('div', class_='dy')
                comment_content = comment_content_tag.get_text(strip=True) if comment_content_tag else None

                comment_reactions_tag = comment_tag.find('span', class_='ec')
                comment_reactions = comment_reactions_tag.get_text(strip=True) if comment_reactions_tag else None

                comment_date_tag = comment_tag.find('abbr')
                comment_date = comment_date_tag.get_text(strip=True) if comment_date_tag else None

                if comment_author and comment_content:
                    comments.append({
                        'author': comment_author,
                        'content': comment_content,
                        'reactions': comment_reactions,
                        'date': comment_date
                    })

            logging.debug("Comments extracted: %s", comments)

            self.__pub_info = {
                'user_name': user_name,
                'user_profile_link': user_profile_link,
                'date': date,
                'privacy': privacy,
                'content': content,
                'image_url': image_url,
                'reactions': reactions,
                'comments': comments
            }

        except Exception as e:
            logging.error("An error occurred during parsing: %s", e)
            self.__pub_info = {"error": f"An error occurred during parsing: {str(e)}"}

    def __str__(self):
        return json.dumps(self.__pub_info, indent=4, ensure_ascii=False)

    def __repr__(self):
        return json.dumps(self.__pub_info, indent=4, ensure_ascii=False)

    def __getitem__(self, key):
        return self.__pub_info[key] if key in self.__pub_info else None

    @property
    def pub_info(self):
        return self.__pub_info.copy()

    def refresh(self):
        self.__init__(pubid=self.__usr, requests_session=self.__session)
        return True

    def get(self, item):
        return self[item]
