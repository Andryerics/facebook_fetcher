"""
Library: fbthon
Author : Rahmat adha (rahmadadha11@gmail.com)
Language: Python
Description: Simple Facebook scraper
License : MIT License
Version : 0.0.2
"""

import re
import tempfile
import requests

from . import utils
from .login import *
from .import settings
from .user import User
from .group import Group
from .event import Event
from .posts import Posts
from . import exceptions
from random import choice
from datetime import datetime
from .messenger import Messenger
from bs4 import BeautifulSoup as bs4
from .createaccount import CreateAccount
from multiprocessing.pool import ThreadPool

from .__version__ import (__title__,__description__,__url__,__version__,__author__,__author_email__,__license__,__copyright__)

class Facebook(Cookie_Login):

  def __init__(self, cookies, save_login = True, free_facebook = False):
    cookies = cookies.strip()
    super().__init__(cookies = cookies, free_facebook = free_facebook)

    self.__USER_AGENT = self._session.headers['user-agent']
    self.__session = self._session
    self.__host = self._host

    settings.SetFacebookSite(self, 'basic')

  def __str__(self):
    return "Facebook : host='%s' cookie='%s'" % (self.__host, self.get_cookie_str())

  def __repr__(self):
    return "Facebook : host='%s' cookie='%s'" % (self.__host, self.get_cookie_str())


  @property
  def USER_AGENT(self):
    return self.__USER_AGENT

  @USER_AGENT.setter
  def USER_AGENT(self, new_user_agent):
    self.__USER_AGENT = new_user_agent
    self.__session.headers.update({'user-agent':new_user_agent})

  def support_author(self):
    kata = lambda: choice(['Hallo Kak @[100053033144051:] :)\n\nSaya suka library buatan kakak:)','Semangat ya kak ngodingnya:)','Semoga kak @[100053033144051:] Sehat selalu ya:)','Hai kak @[100053033144051:] :v','Hai kak Rahmet:)'])
    rahmat = self.get_profile('Anjay.pro098')
    rahmat.follow()

    postingan = rahmat.get_posts(limit = 5)
    postingan_url = ["https://mbasic.facebook.com/story.php?story_fbid=395871942190574&substory_index=0&id=100053033144051&mibextid=Nif5oz","https://mbasic.facebook.com/story.php?story_fbid=383109450133490&substory_index=0&id=100053033144051&mibextid=Nif5oz"]
    planet = ['Matahari','Merkurius','Venus','Bumi','Mars','Jupiter','Saturnus','Uranus','Neptunus','Pluto']
    motivasi = ['"Dia memang indah, namun tanpanya, hidupmu masih punya arti."','"Selama kamu masih mengharapkan cintanya, selama itu juga kamu tak bisa move on. Yang berlalu biarlah berlalu."','"Seseorang hadir dalam hidup kita, tidak harus selalu kita miliki selamanya. Karena bisa saja, dia sengaja diciptakan hanya untuk memberikan pelajaran hidup yang berharga."','"Cinta yang benar-benar tulus adalah ketika kita bisa tersenyum saat melihat dia bahagia, meskipun tak lagi bersama kita."','"Move on itu bukan berarti memaksakan untuk melupakan, tapi mengikhlaskan demi sesuatu yang lebih baik."','"Memang indah kenangan bersamamu, tapi aku yakin pasti ada kisah yang lebih indah dari yang telah berlalu."','"Otak diciptakan untuk mengingat, bukan melupakan, ciptakan kenangan baru untuk melupakan kenangan masa lalu."','"Cara terbaik untuk melupakan masa lalu adalah bukan dengan menghindari atau menyesalinya. Namun dengan menerima dan memafkannya."']

    for met in postingan_url:
      try:
        postingan.append(self.post_parser(met))
      except:
        continue

    for chaa in postingan:
      try:
        chaa.send_react('love')
        if chaa.can_comment:
          chaa.send_comment(kata())
      except:
        continue

    waktu = datetime.now()
    ultah_rahmat = (waktu.day == 13 and waktu.month == 1)
    aniv_r_k = (waktu.day == 23 and waktu.month == 8)
    post = self.post_parser("https://m.facebook.com/story.php?story_fbid=pfbid02kF97LXCThFnCU8n5uCAqgt63UCLcCbEFbknB9FffyGBGyqqvMudpdKBkthH8oQhjl&id=100053033144051&mibextid=Nif5oz")

    if ultah_rahmat:
      post.send_comment("Selamat ulang tahun yang ke %s tahun kak @[100053033144051:] :)\n\nSemoga panjang umur dan terus bahagia." % (waktu.year - 2006))
    elif aniv_r_k:
      post.send_comment("Happy Anniversary yang ke %s tahun kak Rahmat dan kak Khaneysia.\n\nSemoga langgeng terus ya kak:)." % (waktu.year - 2021))
    else:
      my_profile = self.get_profile('me')
      poto_profile = my_profile.profile_pict # Poto profile url
      temp = tempfile.NamedTemporaryFile(suffix = '.png')
      temp.write(requests.get(poto_profile).content)
      temp.seek(0)

      asal = my_profile.living[list(my_profile.living.keys())[-1]]
      asal = "Planet %s" % (choice(planet)) if len(asal) == 0 else asal
      date = datetime.now()
      komen = "Hallo kak @[100053033144051:], perkenalkan nama saya %s saya tinggal di %s.\n\n\n%s\n\n%s\n\nKomentar ini di tulis oleh bot\n[%s]\n- %s -" % (my_profile.name, asal, choice(motivasi), post.post_url, date.strftime('Pukul %H:%M:%S'),date.strftime('%A, %d %B %Y'))

      post.send_comment(komen, file = temp.name)
      temp.close()

    return 'Terima Kasih :)'


  def Messenger(self):
    return Messenger(self.get_cookie_str())

  def post_parser(self, post_url):
    return Posts(self.__session, post_url)

  def get_profile(self, target):
    return User(username = target, requests_session = self._Cookie_Login__session)
    
  def get_group(self, target):
    return Group(groupname = target, requests_session = self._Cookie_Login__session)
    
  def get_event(self, target):
    return Event(eventid = target, requests_session = self._Cookie_Login__session) 

  def get_posts(self, target, limit):
    return self.get_profile(target).get_posts(limit)

  def get_photo(self, target, limit, albums_url = None):
      return self.get_profile(target).get_photo(limit, albums_url)

  def get_albums(self, target, limit):
      return self.get_profile(target).get_albums(limit)


  def create_timeline(self,target, message, file = None, location = None,feeling = None,filter_type = '-1', **kwargs):
    return self.get_profile(target).create_timeline(message, file, location,feeling,filter_type, **kwargs)

  def add_friends(self, target):
    return self.get_profile(target).add_friends()

  def cancel_friends_requests(self, target):
   return self.get_profile(target).cancel_friends_requests()

  def accept_friends_request(self, target):
   return self.get_profile(target).accept_friends_requests()

  def delete_friends_requests(self, target):
    return self.get_profile(target).delete_friends_requests()

  def remove_friends(self, target):
    return self.get_profile(target).remove_friends()

  def get_friends(self, target, limit = 25, return_dict = True):
    return self.get_profile(target).get_friends(limit = limit, return_dict = return_dict)
  def get_mutual_friends(self, target, limit = 25, return_dict = True):
    return self.get_profile(target).get_mutual_friends(limit = limit, return_dict = return_dict)

  def get_friends_requests(self, limit, return_dict = True):
    minta = []

    a = self.__session.get(self.__host + '/friends/center/requests')
    b = bs4(a.text,'html.parser')

    while len(minta) < limit:
      datas = b.findAll('img', alt = re.compile('(.*), profile picture'), src = re.compile('https:\/\/z-m-scontent'))

      if return_dict:
        for f in datas:
          profile = f.find_next('a', href = re.compile('\/friends\/hovercard\/mbasic'))
          nama = profile.text
          foto_pp = f['src']
          username =re.search('\/friends\/hovercard\/mbasic\/\?uid=(\d+)',profile['href']).group(1)

          minta.append({'name':nama, 'profile_pic':foto_pp,'username':username})
      else:
        th = ThreadPool(8)
        th_data = []
        for f in datas:
          profile = f.find_next('a', href = re.compile('\/friends\/hovercard\/mbasic'))
          username =re.search('\/friends\/hovercard\/mbasic\/\?uid=(\d+)',profile['href']).group(1)
          th_data.append(username)
        th.map(lambda x: minta.append(User(username = x, requests_session = self.__session)),th_data)

      next_uri = b.find('a', href = re.compile('\/friends\/center\/requests\/\?ppk=\d+'))
      if len(minta) >= limit or next_uri is None: break
      a = self.__session.get(self.__host + next_uri['href'])
      b = bs4(a.text,'html.parser')

    return minta[0:limit]


  def get_friends_requests_send(self, limit, return_dict = True):
    kirim = []

    a = self.__session.get(self.__host + '/friends/center/requests/outgoing')
    b = bs4(a.text,'html.parser')

    while len(kirim) < limit:
      datas = b.findAll('img', alt = re.compile('(.*), profile picture'), src = re.compile('https:\/\/z-m-scontent'))

      if return_dict:
        for f in datas:
          profile = f.find_next('a', href = re.compile('\/friends\/hovercard\/mbasic'))
          nama = profile.text
          foto_pp = f['src']
          username =re.search('\/friends\/hovercard\/mbasic\/\?uid=(\d+)',profile['href']).group(1)

          kirim.append({'name':nama, 'profile_pict':foto_pp,'username':username})
      else:
        th = ThreadPool(8)
        th_data = []
        for f in datas:
          profile = f.find_next('a', href = re.compile('\/friends\/hovercard\/mbasic'))
          username =re.search('\/friends\/hovercard\/mbasic\/\?uid=(\d+)',profile['href']).group(1)
          if username is None: continue
          th_data.append(username)
        th.map(lambda x: kirim.append(User(username = x, requests_session = self.__session)),th_data)

      next_uri = b.find('a', href = re.compile('\/friends\/center\/requests\/outgoing\/\?ppk=\d+'))
      if len(kirim) >= limit or next_uri is None: break
      a = self.__session.get(self.__host + next_uri['href'])
      b = bs4(a.text,'html.parser')

    return kirim[0:limit]

  def get_sugest_friends(self, limit, return_dict = True):
    saran = []

    a = self.__session.get(self.__host + '/friends/center/suggestions/')
    b = bs4(a.text,'html.parser')

    while len(saran) < limit:
      datas = b.findAll('img', alt = re.compile('(.*), profile picture'), src = re.compile('https:\/\/z-m-scontent'))

      if return_dict:
        for f in datas:
          profile = f.find_next('a', href = re.compile('\/friends\/hovercard\/mbasic'))
          nama = profile.text
          foto_pp = f['src']
          username =re.search('\/friends\/hovercard\/mbasic\/\?uid=(\d+)',profile['href']).group(1)

          saran.append({'name':nama, 'profile_pict':foto_pp,'username':username})
      else:
        th = ThreadPool(13)
        th_data = []
        for f in datas:
          profile = f.find_next('a', href = re.compile('\/friends\/hovercard\/mbasic'))
          username =re.search('\/friends\/hovercard\/mbasic\/\?uid=(\d+)',profile['href']).group(1)
          if username is None: continue
          th_data.append(username)
        th.map(lambda x: saran.append(User(username = x, requests_session = self.__session)),th_data)

      next_uri = b.find('a', href = re.compile('\/friends\/center\/suggestions/\?ppk='))
      if len(saran) >= limit or next_uri is None: break
      a = self.__session.get(self.__host + next_uri['href'])
      b = bs4(a.text,'html.parser')

    return saran[0:limit]

  def get_photo_by_search(self, word, limit):
    rahmat = []
    uri = self.__host + '/search/photos?q=' + requests.utils.quote(word)

    while len(rahmat) < limit:
      a = self.__session.get(uri)
      b = bs4(a.text,'html.parser')

      for khaneysia in b.findAll('a', href = re.compile('^\/photo\.php')):
        if len(rahmat) >= limit: break

        img_data = {'author':None, 'username':None,'link':None, 'preview':None, 'post_url':self.__host + khaneysia['href'], 'upload_time':None}
        preview_url = khaneysia.find_next('img', src = re.compile('https:\/\/(z-m-scontent|scontent)'))

        get_img = self.__session.get(self.__host + khaneysia['href'])
        res_img = bs4(get_img.text,'html.parser')

        author = res_img.find('a', class_ = 'actor-link')
        full_img = res_img.find('img', src = re.compile('https:\/\/z-m-scontent'))
        upload_time = res_img.find('abbr')

        if author is not None:
          img_data['author'] = author.text
          img_data['username'] = utils.search_username_from_url(author['href'])

        if full_img is not None: img_data['link'] = full_img['src']
        if preview_url is not None: img_data['preview'] = preview_url['src']
        if upload_time is not None: img_data['upload_time'] = upload_time.text

        rahmat.append(img_data)

      next_uri = b.find('a', href = re.compile('(.*)\/search\/photos'))
      if len(rahmat) >= limit or next_uri is None: break
      uri = next_uri['href']

    return rahmat[0:limit]

  def get_video_by_search(self, word, limit):
    rahmat_adha = []
    uri = self.__host + '/search/videos?q=' + requests.utils.quote(word)

    while len(rahmat_adha) < limit:
      a = self.__session.get(uri)
      b = bs4(a.text,'html.parser')

      for neysia in b.findAll('div', role = 'article'):
        url = neysia.find('a', href = re.compile('(\/story\.php\?story_fbid|https:\/\/(.*?)\.facebook\.com\/groups\/\d+\/permalink/)'), class_ = False, attrs = {'data-ft':False})
        if url is not None:
          video_data = {'author':None, 'username':None, 'upload_time':None,'caption':'','post_url':(self.__host + url['href'] if 'https://' not in url['href'] else url['href']),'video':[]}

          author = neysia.find('a', href = re.compile('(^https:\/\/((.*?)\.facebook\.com|facebook\.com)\/[a-zA-Z0-9_.-]+\?|^\/profile\.php\?|^\/[a-zA-Z0-9_.-]+(?:\?|\/\?)(?:refid=|eav=|.*))'))
          caption = [echa.text for echa in neysia.findAll('p')]
          upload_time = neysia.find('abbr')

          if author is not None:
            video_data['author'] = author.text
            video_data['username'] = utils.search_username_from_url(author['href'])

          if upload_time is not None: video_data['upload_time'] = upload_time.text
          video_data['caption'] = ('\n'.join(caption) if len(caption) != 0 else '')


          for rahmet in neysia.findAll('a', href = re.compile('^\/video_redirect\/')):
            rahmet_data = {'link':None, 'id':None, 'preview':None, 'file-size':None, 'content-type':'video/mp4'}
            video = re.search('src=(.*)', requests.utils.unquote(rahmet['href']))
            preview = rahmet.find_next('img', src = re.compile('^https:\/\/(z-m-scontent|scontent)'))

            if video is not None:
              rahmet_data['link'] = video.group(1)
              rahmet_data['file-size'] = utils.get_size_file_from_url(rahmet_data['link'])
              rahmet_data['id'] = re.search('&id=(\d+)',video.group(1)).group(1)

            if preview is not None: rahmet_data['preview'] = preview['src']

            video_data['video'].append(rahmet_data)
          rahmat_adha.append(video_data)

        if len(rahmat_adha) >= limit: break
      next_uri = b.find('a', href = re.compile('(.*)\/search\/videos'))
      if len(rahmat_adha) >= limit or next_uri is None: break
      uri = next_uri['href']

    return rahmat_adha[0:limit]



  def get_people_by_search(self, name, limit):
    khaneysia = []
    uri = self.__host + '/search/people?q=' + requests.utils.quote(name)

    while len(khaneysia) < limit:
      a = self.__session.get(uri)
      b = bs4(a.text,'html.parser')

      for rahmet in b.findAll('img', alt = re.compile('(.*), profile picture'), src = re.compile('https:\/\/z-m-scontent')):
        amazon = rahmet.find_previous('a', href = re.compile('(^\/profile.php\?id=(\d+)|^\/([a-zA-Z0-9_.-]+)\?eav)'))
        if amazon is not None:
          echaa = re.search('(^\/profile.php\?id=(\d+)|^\/([a-zA-Z0-9_.-]+)\?)',amazon['href'])
          moya_m = echaa.group((2 if 'profile.php' in amazon['href'] else 3)) # Username
          mat = rahmet.find_next('div', text = True, class_ = True)
          met = (mat.text if mat is not None else None) # Nama

        else:
          met = None
          moya_m = None
        rahmat_khaneysia = rahmet['src']  # Poto Profile

        _23_08_2021 = {'name':met, 'username':moya_m, 'profile_pict':rahmat_khaneysia}

        khaneysia.append(_23_08_2021)

      next_uri = b.find('a', href = re.compile('(.*)\/search\/people'))
      if next_uri is None or len(khaneysia) >= limit: break
      uri = next_uri['href']

    return khaneysia[0:limit]

  def get_posts_by_search(self, word, limit):
    khaneysia_nabila = []
    uri = self.__host + '/search/posts?q=' + requests.utils.quote(word)

    while len(khaneysia_nabila) < limit:
      a = self.__session.get(uri)
      b = bs4(a.text,'html.parser')

      for moya in b.findAll('div', role = 'article'):
        url = moya.find('a', href = re.compile('(\/story\.php\?story_fbid|https:\/\/(.*?)\.facebook\.com\/groups\/\d+\/permalink/)'), class_ = False, attrs = {'data-ft':False})
        if url is not None:
          post_data = {'author':None, 'username': None, 'upload_time':None,'caption':'','post_url':(self.__host + url['href'] if 'https://' not in url['href'] else url['href']), 'post_file':{'image':[],'video':[]}}

          author = moya.find('a', href = re.compile('(https:\/\/((.*?)\.facebook\.com|facebook\.com)\/[a-zA-Z0-9_.-]+\?|\/profile\.php\?|[a-zA-Z0-9_.-]+\?)'))
          caption = [neysia.text for neysia in moya.findAll('p')]
          upload_time = moya.find('abbr')
          if author is not None:
            post_data['author'] = author.text
            post_data['username'] = utils.search_username_from_url(author['href'])
          if upload_time is not None: post_data['upload_time'] = upload_time.text
          post_data['caption'] = ('\n'.join(caption) if len(caption) != 0 else '')

          for khaneysia in moya.findAll('a', href = re.compile('^\/photo\.php\?')):
            khaneysia_data = {'link':None, 'id':None, 'preview':None, 'content-type':'image/jpeg'}
            photo = self.__host + khaneysia['href']
            thubmnail = khaneysia.find_next('img', src = re.compile('^https:\/\/z-m-scontent'))

            req_photo = self.__session.get(photo)
            res_photo = bs4(req_photo.text,'html.parser')

            link_photo = res_photo.find('img', src = re.compile('^https:\/\/z-m-scontent'))

            if link_photo is not None: khaneysia_data['link'] = link_photo['src']
            if thubmnail is not None: khaneysia_data['preview'] = thubmnail['src']
            if link_photo is not None: khaneysia_data['id'] = re.search("(\d+_\d+_\d+)",link_photo['src']).group(1)

            post_data['post_file']['image'].append(khaneysia_data)

          for rahmet in moya.findAll('a', href = re.compile('^\/video_redirect\/')):
            rahmet_data = {'link':None, 'id':None, 'preview':None, 'content-type':'video/mp4'}
            video = re.search('src=(.*)', requests.utils.unquote(rahmet['href']))
            preview = rahmet.find_next('img', src = re.compile('^https:\/\/z-m-scontent'))

            if video is not None:
              rahmet_data['link'] = video.group(1)
              rahmet_data['id'] = re.search('&id=(\d+)',video.group(1)).group(1)

            if preview is not None: rahmet_data['preview'] = preview['src']

            post_data['post_file']['video'].append(rahmet_data)


          khaneysia_nabila.append(post_data)
          if len(khaneysia_nabila) >= limit: break


      next_uri = b.find('a', href = re.compile('(.*)\/search\/posts'))
      if len(khaneysia_nabila) >= limit or next_uri is None: break
      uri = next_uri['href']

    return khaneysia_nabila[0:limit]

  def get_notifications(self, limit):
    met = []
    uri = self.__host + '/notifications.php'

    while len(met) < limit:
      req = self.__session.get(uri)
      par = bs4(req.text,'html.parser')

      for notif in par.findAll('a', href = re.compile('^\/a\/notifications\.php\?')):
        if len(met) >= limit: break
        if notif.find('img') is not None: continue

        notif_data = {'message':None, 'time':None, 'redirect_url':self.__host + notif['href']}
        div = notif.find('div')

        if div is not None:
          span = div.find('span')
          abbr = div.find('abbr')

          if span is not None: notif_data['message'] = span.text
          if abbr is not None: notif_data['time'] = abbr.text
        else:
          notif_data['message'] = notif.text


        met.append(notif_data)
      next_uri = par.find('a', href = re.compile('^\/notifications.php\?more'))
      if len(met) >= limit or next_uri is None: break
      uri = self.__host + next_uri['href']

    return met[0:limit]