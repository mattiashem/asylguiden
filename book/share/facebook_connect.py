'''
File for posting new post to asylguiden facebook wall

Use by calling post_to_facebook('you post from')
and make shoure that your token is valid to post to ypu pages.


'''

import facebook


def post_to_facebook(message):
    '''
    Posting to facebook wall of asylguiden
    '''


    #token = ''
    token = ''
    graph = facebook.GraphAPI(token)
    #profile = graph.get_object("me")

    graph.put_object("175357059145044", "feed", message=message)


