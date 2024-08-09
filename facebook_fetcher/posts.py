"""
fbthon.posts
--------------
Parsing Post data
"""

import os
import re
import json
import codecs
import requests
import multiprocessing

from . import utils
from . import exceptions
from datetime import datetime
from .comments import Comments
from bs4 import BeautifulSoup as bs4

class Posts:

  def __init__(self, requests_session, post_url, ft_data = {}):
    # Vérifie si l'URL fournie correspond à un format valide de publication Facebook.
    if not re.match("https:\/\/((?:(?:.*?)\.facebook.com|facebook\.com)\/((\d+|groups|[a-zA-Z0-9_.-]+)\/(\d+|posts|videos)\/(?:\d+|permalink\/\d+|\w+)|story\.php\?story_fbid|photo\.php\?fbid=\w+|watch(?:\/\?|\?)v=\d+)|fb\.(?:gg|watch)\/\w+)",post_url):
      raise exceptions.FacebookError('"%s" Bukanlah URL Yang valid, coba periksa kembali URl anda!!!!' % (post_url))

    # Adaptation des URLs de vidéos pour correspondre à un format standard.
    if re.match('https:\/\/fb\.watch\/(?:.*?)\/',post_url):
      vid_id = re.search('https:\/\/fb\.watch\/(.*?)\/',post_url)
      if vid_id is not None:
        post_url = "https://fb.gg/v/%s/" % (vid_id.group(1))

    self.__session = requests_session
    self.__host = ('https://'+self.__session.headers['host'] if 'host' in self.__session.headers.keys() else "https://mbasic.facebook.com")

    # Tentative de récupérer la page du post via une session de requêtes.
    try:
      self.__req = self.__session.get(post_url)
    except requests.exceptions.TooManyRedirects:
      head = {'User-Agent':self.__session.headers['User-Agent']}
      self.__session.headers.clear()
      self.__session.headers.update(head)
      self.__req = self.__session.get(post_url)

    self.__res = bs4(self.__req.text,'html.parser')

    # Gestion des erreurs lorsque la page n'est pas trouvée.
    if self.__res.find('a', href = re.compile('\/home\.php\?rand=\d+')):
      raise exceptions.PageNotFound("The post was not found, the post may have been deleted or maybe you do not have permission to view the post!!!")
    
    tmp_ban = self.__res.find('a', href = re.compile('^\/\?'), target = '_self')
    if tmp_ban is not None:
      try:
        a_ban = self.__session.get(self.__host + tmp_ban['href'])
        if 'next=' in a_ban.url:
          self.__session.get(requests.utils.unquote(re.search('next=(.*)',a_ban.url).group(1)))
      finally:
        raise exceptions.AccountTemporaryBanned('Your Facebook account is temporarily banned!')

    # Gestion des erreurs diverses renvoyées par Facebook.
    if self.__res.find('a', href = re.compile('^\/$')):
      err_msg = self.__res.find('div', class_ = 'area error')
      err = (''.join([i.strip() for i in err_msg.findAll(text = True)]) if err_msg is not None else "There is an error!")
      raise exceptions.FacebookError(err)

    # Localise la div principale contenant l'article.
    div_article = self.__res.find('div', role = 'article')
    if div_article is not None:
      self.__res = div_article
      url = self.__res.find('a', href = re.compile('(\/story\.php\?story_fbid|https:\/\/(.*?)\.facebook\.com\/groups\/\d+\/permalink/)'), class_ = False, attrs = {'data-ft':False})
      if url is not None:
        self.__res = bs4(self.__session.get((self.__host + url['href'] if 'https://' not in url['href'] else url['href'])).text,'html.parser')

    # Recherche de la div contenant les informations de publication.
    div_post = self.__res.find('div', class_ = True, attrs = {'data-ft':True, 'id':True})
    post_datetime = None

    if div_post is not None:
      ft_data.update(json.loads(div_post.get('data-ft')))
      try:
        page_id = list(ft_data['page_insights'].keys())
        if len(page_id) != 0:
          post_datetime = datetime.fromtimestamp(ft_data['page_insights'][page_id[0]]['post_context']['publish_time'])
      except KeyError:
        pass
    else:
      div_post = self.__res

    # Définit les types de réactions Facebook et initialise les fichiers du post.
    self.__react_type = {'1':'like','2':'love','3':'wow','4':'haha','7':'sad','8':'angry','16':'care'}
    post_file = {'image':[],'video':[]}

    # Recherche le formulaire pour commenter et les actions pour aimer ou réagir.
    self.__form_komen = self.__res.find('form', action = re.compile('\/a\/comment\.php\?'))
    self.__like_action = self.__res.find('a', href = re.compile('\/a\/like\.php\?'))
    self.__react_url = self.__res.find('a', href = re.compile('\/reactions\/picker\/\?'))
    self.__data = {i.get('name'):i.get('value') for i in self.__res.findAll('input', type = 'hidden')}

    # Extraction des images associées à la publication.
    for khaneysia in div_post.findAll('a', href = re.compile('^(\/photo\.php(?:\?|\/\?)|\/[a-zA-Z0-9_.-]+\/photos)')):
      khaneysia_data = {'link':None, 'id':None, 'preview':None, 'content-type':'image/jpeg'}
      photo = self.__host + khaneysia['href']
      thubmnail = khaneysia.find_next('img')
      req_photo = self.__session.get(photo)
      res_photo = bs4(req_photo.text,'html.parser')
      link_photo = res_photo.find('img', src = re.compile('^https:\/\/(?:z-m-scontent|scontent)'))

      if link_photo is not None:
        khaneysia_data['link'] = link_photo['src']
      if thubmnail is not None:
        khaneysia_data['preview'] = thubmnail['src']
      if link_photo is not None:
        khaneysia_data['id'] = re.search("(\d+_\d+_\d+)",link_photo['src']).group(1)

      post_file['image'].append(khaneysia_data)

    # Extraction des vidéos associées à la publication.
    for rahmet in div_post.findAll('a', href = re.compile('^\/video_redirect\/')):
      rahmet_data = {'link':None, 'id':None, 'preview':None, 'content-type':'video/mp4'}
      video = re.search('src=(.*)', requests.utils.unquote(rahmet['href']))
      preview = rahmet.find_next('img')

      if video is not None:
        rahmet_data['link'] = video.group(1)
        rahmet_data['id'] = re.search('&id=(\d+)',video.group(1)).group(1)

      if preview is not None:
        rahmet_data['preview'] = preview['src']

      post_file['video'].append(rahmet_data)

    # Extraction des informations de l'auteur et du contenu de la publication.
    author = div_post.find('a', class_ = 'actor-link')

    if author is None:
      author = div_post.find('a',class_ = False,href = re.compile('^\/(profile\.php\?|[a-zA-Z0-9_.-]+(\?|\/\?))'))

    caption  = [khaneysia_nabila_zahra.text for khaneysia_nabila_zahra in div_post.findAll('p')]
    upload_time = div_post.find('abbr')

    author = (author.text if author is not None else None)
    caption = ('\n'.join(caption) if len(caption) != 0 else '')
    upload_time = (upload_time.text if upload_time is not None else None)

    if 'mf_story_key' in ft_data.keys() and 'content_owner_id_new' in ft_data.keys():
      post_url = "%s/%s/posts/%s" % (self.__host, ft_data['content_owner_id_new'], ft_data['mf_story_key'])
      
    #link_post = 
    url_post = re.search(r'story_fbid=(\w+).*?id=(\d+)', post_url)
    if url_post:
        story_fbid = url_post.group(1)
        user_id = url_post.group(2)
        link_post = f"https://www.facebook.com/{user_id}/posts/{story_fbid}/?app=fbl"
    else:
        link_post = "URL invalide"
          
    link_post = (link_post if link_post is not None else None)
      
    # Stockage des données récupérées dans des attributs de l'objet.
    self.__data['author'] = author
    self.__data['upload_time'] = upload_time
    self.__data['caption'] = caption
    self.__data['link_post'] = link_post
    self.__data['post_file'] = post_file
    self.__data['post_url'] = post_url
    self.__data['data_ft'] = ft_data
    self.__data['post_datetime'] = post_datetime
    self.__data['can_comment'] = self.__form_komen is not None

    self.author = author
    self.upload_time = upload_time
    self.caption = caption
    self.link_post = link_post
    self.post_file = post_file
    self.post_url = post_url
    self.data_ft = ft_data
    self.post_datetime = post_datetime
    self.can_comment = self.__data['can_comment']

  def __str__(self):
    # Définition de la représentation en chaîne de caractères pour l'objet.
    return "Facebook Posts: author='%s' upload_time='%s' post_url='%s' link_post='%s' can_comment=%s" % (self['author'], self['upload_time'], self['post_url'], self['link_post'], self['can_comment'])

  def __repr__(self):
    # Définition de la représentation officielle pour l'objet.
    return "Facebook Posts: author='%s' upload_time='%s' post_url='%s' link_post='%s' can_comment=%s" % (self['author'], self['upload_time'], self['post_url'], self['link_post'] ,self['can_comment'])

  def __getitem__(self, item):
    # Méthode pour accéder aux données de l'objet via des clés.
    return (self.__data[item] if item in self.__data.keys() else None)

  def __enter__(self):
    # Méthode pour utiliser l'objet avec une déclaration `with`.
    return self

  def __exit__(self, exc_type, exc_value, tb):
    # Méthode pour gérer les exceptions dans le contexte `with`.
    if exc_type is not None:
      traceback.print_exception(exc_type, exc_value, tb)
    return True

  def __get_user_from_react(self, data):
    # Méthode pour récupérer les utilisateurs ayant réagi à une publication.
    Moya_M = []

    a = self.__session.get(data[0])
    b = bs4(a.text,'html.parser')

    while len(Moya_M) < data[1]:
      rahmet = b.findAll('a',href = re.compile('^\/([a-zA-Z0-9_.-]+\?eav|profile\.php)'))
      if len(rahmet) == 0: break
      for x in rahmet:
        Moya_M.append({'name':x.text,'username':re.search('^\/(([a-zA-Z0-9_.-]+)\?eav|profile\.php\?id=(\d+))',x['href']).group(2 if 'profile.php' not in x['href'] else 3)})

      next_uri = b.find('a', href = re.compile('^\/ufi\/reaction\/profile(.*)shown_ids=\d'))
      if len(Moya_M) >= data[1] or next_uri is None: break
      b = bs4(self.__session.get(self.__host + next_uri['href']).text,'html.parser')
    return {'react_type':re.search('reaction_type=(\d+)',data[0]).group(1),'user':Moya_M}

  def send_comment(self, message, file = None):
    # Méthode pour envoyer un commentaire sur la publication.
    if self.__form_komen is None: raise exceptions.FacebookError('Tidak dapat menulis komentar di postingan ini!!!')

    message = codecs.decode(codecs.encode(message,'unicode_escape'),'unicode_escape')

    if file is not None:
      view_photo = self.__res.find('input', attrs = {'name':'view_photo','type':'submit'})
      form = view_photo.find_previous('form', action = re.compile('\/a\/comment\.php\?'))
      form_data = {i.get('name'):i.get('value') for i in form.findAll('input', attrs = {'type':'hidden'})}
      form_data['view_photo'] = view_photo.get('value')
      z_upload = self.__session.post(self.__host + form['action'], data = form_data)
      z_upload_form = bs4(z_upload.text,'html.parser').find('form', action = re.compile('https:\/\/(z-upload\.facebook\.com|upload\.facebook\.com)'))
      z_upload_data = {i.get('name'):(None,i.get('value')) for i in z_upload_form.findAll('input', attrs = {'type':'hidden'})}
      z_upload_data['comment_text'] = (None, message)

      # Utilise une fonction utilitaire pour téléverser la photo avec le commentaire.
      kirim = utils.upload_photo(requests_session = self.__session, upload_url = z_upload_form['action'], input_file_name = 'photo', file_path = file, fields = z_upload_data)
    else:
      # Envoie le commentaire sans fichier joint.
      komen_action = self.__host + self.__form_komen["action"]
      komen_data = {i.get('name'):i.get('value') for i in self.__form_komen.findAll('input')}
      komen_data['comment_text'] = message

      kirim = self.__session.post(komen_action, data = komen_data)

    return kirim.ok

  def get_comment(self, limit = 10):
    # Méthode pour récupérer les commentaires de la publication, jusqu'à une limite donnée.
    komentar = []
    html_parser = self.__res

    while len(komentar) < limit:
      for i in html_parser.findAll('a', href = re.compile('^\/([a-zA-Z0-9_.-]+\?eav|profile\.php)'), class_ = True):
        div_komen = i.find_previous('div', class_ = True, id = re.compile('^\d+')) 
        if div_komen is None:
          div_komen = i.find_previous('div', class_ = False, role = False, id = False)
        if div_komen is None:
          continue
        komentar.append(Comments(str(div_komen),self.__session))

      next_uri = html_parser.find('a', href = re.compile('^\/story\.php\?(.*)p=\d'))
      if next_uri is None or len(komentar) >= limit:
        break
      html_parser = bs4(self.__session.get(self.__host + next_uri['href']).text,'html.parser')

    return komentar[0:limit]

  # Méthode pour récupérer toutes les réactions d'une publication.
  def get_react(self):
    ufi = self.__res.find('a', href = re.compile('^\/ufi\/reaction\/profile'))
    react_data = {i:0 for i in ['like','love','care','haha','wow','sad','angry']}

    if ufi is not None:
      a = self.__session.get(self.__host + ufi['href'])
      b = bs4(a.text,'html.parser')
      c = b.findAll('a', href = re.compile('^\/ufi\/reaction\/profile(.*)total_count=\d'))

      for k,v in enumerate(c[1:]):
        total = int(re.search('total_count=(\d+)',v['href']).group(1))
        rct_type = re.search('reaction_type=(\d+)',v['href']).group(1)
        if rct_type not in self.__react_type.keys():
          continue
        react_data[self.__react_type[rct_type]] = total

    return react_data
    # finished

