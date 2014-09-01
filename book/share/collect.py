import pymongo


#Connect to db
from pymongo import MongoClient
client = MongoClient()

#Connect to db
db = client.tumblelog
post = db.post
user_info = db.user_info


def saved_posts(id):
    '''
    Test if the post has bean posten in teh last 20 posts.
    If it has no new post is posted.
    If not saved the new post id and resturns true so script can continu posting
    '''


    with open("saved") as myfile:
        head = [next(myfile) for x in xrange(20)]
    if any(str(id) in s for s in head):
        #The id are alreay in latest post
        print "\n"+str(id) + "are in list"
        return False
    else:
        #The post is not in lates post update the file and tell script to move on.
        print "not in file"
        f = open('saved', 'w')
        f.write(str(id)+"\n")
        for data in head:
            f.write(data)
        f.close()
        return True


def get_top_posts():
    '''
    find the top post and post it
    '''
    #Fins the post with higest rate
    highrated = db.post.find().sort('page_rate',-1).limit(1)

    for post in highrated:
        print post['_id']

        if saved_posts(post['_id']):
            #Post the post to different serivces
            print "<a href='http://localhost:8000/book/articel/"+str(post['_id'])+"/'><h1>"+str(post['title'])+"</h1></a>\n<h3>"+str(post['location'])+"</h3>\n<h3>"+str(post['tags'])+"</h3>\n<p>"+str(post['text'])+"</p>"


def get_random_locations():
    '''
    get radnom loctaions and post atricels about that to portals
    '''
    #Get and random post
    location = db.post.find_one()

    #Use that post location to get new post matching that id nor already in saved file
    if saved_posts(location['location'][0]):

        relevant = db.post.find({'location':location['location'][0]})

        print "Read our great post about "+location['location'][0]
        for posts in relevant:
            print "<a href='http://www.asylguiden.se/book/post/'" +str(posts['_id'])+ "><h3>"+ str(posts['title']) + "</h3></a>"



def get_random_tags():
    '''
    get radnom tag and post atricels about that to portals
    '''
    #Get and random post
    tag = db.post.find_one()

    #Use that post location to get new post matching that id nor already in saved file
    if saved_posts(tag['tags'][0]):

        relevant = db.post.find({'tags':tag['tags'][0]})

        print "Read our great post about "+tag['tags'][0]
        for posts in relevant:
            print "<a href='http://www.asylguiden.se/book/post/'" +str(posts['_id'])+ "><h3>"+ str(posts['title']) + "</h3></a>"

def get_higest_user():
    '''
    Get the user with the higest number of posts
    '''
    #Fins the post with higest rate
    highrated = db.user_info.find().sort('postscount',-1).limit(1)

    for post in highrated:
        print post['_id']

        if saved_posts(post['_id']):
            #Post the post to different serivces
            print "<a href='http://localhost:8000/book/articel/"+str(post['_id'])+"/'><h1>Our most active writer is "+str(post['first_name'])+" "+str(post['last_name'])+" read all users post here </h1></a>"



def get_mostread_user():
    '''
    Get the user with the most read of posts
    '''
    #Fins the post with higest rate
    highrated = db.user_info.find().sort('read',-1).limit(1)

    for post in highrated:
        print post['_id']

        if saved_posts(post['_id']):
            #Post the post to different serivces
            print "<a href='http://localhost:8000/book/articel/"+str(post['_id'])+"/'><h1>The writer that is the most read "+str(post['first_name'])+" "+str(post['last_name'])+" read all users post here </h1></a>"



get_mostread_user()