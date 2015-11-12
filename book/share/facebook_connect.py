'''
File for posting new post to asylguiden facebook wall

Use by calling post_to_facebook('you post from')
and make shoure that your token is valid to post to ypu pages.


'''

import facebook
from django.conf import settings


def post_to_facebook(head,tags,location):
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : settings.FACEBOOK_PAGE_ID,  # Step 1
    "access_token" : settings.FACEBOOK_ACCESS_TOKEN
  }

  api = get_api(cfg)
  msg = 'Las om {0} pa www.asylguiden.se #{1} #{2} \n\n  #asyl #asylguiden'.format(head,tags,location)
  status = api.put_wall_post(msg)
  print status

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3




