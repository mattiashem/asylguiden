from twython import Twython
from django.conf import settings





twitter = Twython(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET, settings.TWITTER_APP_ACC_TOK, settings.TWITTER_APP_ACC_SEC)
#auth = twitter.get_authentication_tokens(callback_url='http://www.asylguiden.se/')


#ACCESS_TOKEN = twitter.obtain_access_token()


def send_to_twitter(head,tags,location):
    '''
    Sending post to twitter
    '''
    twitter.update_status(status='Las om {0} pa www.asylguiden.se #{1} #{2} #asyl #asylguiden'.format(head,tags,location))