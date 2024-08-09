class LoginFailed(Exception):
  '''Failed to log in to the Facebook account'''
  pass

class InvalidCookies(Exception):
  '''Cookies are invalid'''
  pass

class AccountCheckPoint(Exception):
  '''Account is under CheckPoint'''
  pass

class AccountTemporaryBanned(Exception):
  '''Account temporarily banned by Mark'''
  pass

class AccountDisabled(Exception):
  '''Account permanently banned by Mark'''
  pass

class PageNotFound(Exception):
  '''Page is expired / URL is not valid!'''
  pass

class SessionExpired(Exception):
  '''Session has expired'''
  pass

class FacebookError(Exception):
  '''Facebook error'''
  pass
