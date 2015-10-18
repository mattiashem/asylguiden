from twython import Twython

APP_KEY = ''
APP_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET)
#auth = twitter.get_authentication_tokens(callback_url='http://mysite.com/callback')



twitter.update_status(status='See how easy using Twython is!')