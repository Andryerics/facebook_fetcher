import re
import requests
from bs4 import BeautifulSoup as bs4


class Event:
    def __init__(self, eventid, requests_session):
        self.__eventid = eventid
        self.__session = requests_session
        self.__host = f"https://mbasic.facebook.com/events/{self.__eventid}"

        self.__req = self.__session.get(self.__host)
        self.__res = bs4(self.__req.text, 'html.parser')

        if not self.__res.find('a', href=re.compile('/events/\d+')):
            raise Exception(f"Évènement avec l'ID \"{eventid}\" n'a pas été trouvé!")

        self.__event_info = {
            'title': '',
            'date': '',
            'time': '',
            'location': '',
            'host': '',
            'description': '',
            'interested': '',
            'going': '',
            'invited': '',
            'image': '',
            'details': ''
        }

        self._extract_event_info()

    def _extract_event_info(self):
        # Image
        image_tag = self.__res.find('div', id='event_header')
        if image_tag:
            image_tag = image_tag.find('a', class_='bp bq br')
            if image_tag and image_tag.find('img'):
                self.__event_info['image'] = image_tag.find('img')['src']

        # Title
        title_tag = self.__res.find('h1', class_='cc')
        if title_tag:
            self.__event_info['title'] = title_tag.get_text(strip=True)

        # Date and Time
        date_time_tag = self.__res.find('span', class_='bv bw bx by')
        if date_time_tag:
            self.__event_info['date'] = date_time_tag.get('title', '')
            time_tag = date_time_tag.find_next('div', class_='cs ct y')
            if time_tag:
                self.__event_info['time'] = time_tag.get_text(strip=True)

        # Host
        host_tag = self.__res.find('div', class_='cd')
        if host_tag:
            host_tag = host_tag.find('a', class_='_aq1q')
            if host_tag:
                self.__event_info['host'] = host_tag.get_text(strip=True)

        # Location
        location_tag = self.__res.find('div', class_='cg ch')
        if location_tag:
            location_info = location_tag.find('div', class_='cs ct y cw cx')
            if location_info:
                self.__event_info['location'] = location_info.get_text(strip=True)

        # Guest statistics
        guest_list_tag = self.__res.find('div', id='event_guest_list')
        if guest_list_tag:
            stats = guest_list_tag.find_all('div', class_='df ct dg')
            if len(stats) >= 3:
                self.__event_info['interested'] = stats[0].get_text(strip=True)
                self.__event_info['going'] = stats[1].get_text(strip=True)
                self.__event_info['invited'] = stats[2].get_text(strip=True)

        # Description (if any)
        description_tag = self.__res.find('div', id='event_summary')
        if description_tag:
            self.__event_info['description'] = description_tag.get_text(strip=True)

        # Details
        details_tag = self.__res.find('div', class_='_52ja _2pi9 _2pip _2s23')
        if details_tag:
            self.__event_info['details'] = details_tag.get_text(separator="\n", strip=True)

    def __str__(self):
        return (f"Facebook Event:\n"
                f"Title: {self.__event_info['title']}\n"
                f"Date: {self.__event_info['date']}\n"
                f"Time: {self.__event_info['time']}\n"
                f"Location: {self.__event_info['location']}\n"
                f"Host: {self.__event_info['host']}\n"
                f"Description: {self.__event_info['description']}\n"
                f"Interested: {self.__event_info['interested']}\n"
                f"Going: {self.__event_info['going']}\n"
                f"Invited: {self.__event_info['invited']}\n"
                f"Image: {self.__event_info['image']}\n"
                f"Details: {self.__event_info['details']}")

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, key):
        return self._event_info[key] if key in self._event_info.keys() else None

    @property
    def _event_info(self):
        return self.__event_info.copy()

    def refresh(self):
        self.__init__(eventid=self.__eventid, requests_session=self.__session)
        return True

    def get(self, item):
        return self[item]


