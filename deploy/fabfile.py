from fabric.api import run, env, local
from fabric.context_managers import cd
from fabric.operations import put, sudo
from fabric.contrib.project import rsync_project
import string
import random

env.user='root'



def id_generator(size=30, chars=string.ascii_uppercase + string.digits):
    '''
    For generaing the secret key used for django
    '''
    return ''.join(random.choice(chars) for _ in range(size))

def deploy():
    with cd('/asylguiden'):

        #Copy files
        #sudo('chown ubuntu:ubuntu /asylguiden_d')
        rsync_project(
            remote_dir="/asylguiden/",
            local_dir="../*",
            exclude=(".git", "*.pyc"),
            )

        #Stoping and buildning new images
        run('docker-compose stop')

        # Setting up correct permissions
        #TLS
        #run('cp /asylguiden_prod/nginx/tls/asylguiden.crt /asylguiden/nginx/ssl/asylguiden/server.crt')
        #run('cp /asylguiden_prod/nginx/tls/asylguiden.key /asylguiden/nginx/ssl/asylguiden/server.key')
        #run('cp /asylguiden_prod/nginx/tls/bundle.crt /asylguiden/nginx/ssl/asylguiden/bundle.crt')

        #Configs
        run('cp /asylguiden_prod/settings.py /asylguiden/asylguiden/settings.py')
        run("sed -i 's/DEBUG \= True/DEBUG \= False/' /asylguiden/asylguiden/settings.py")
        run("sed -i 's/TEMPLATE_DEBUG \= DEBUG/\#TEMPLATE_DEBUG \= DEBUG/' /asylguiden/asylguiden/settings.py")
        run("sed -i 's/THUMBNAIL_DEBUG \= True/\THUMBNAIL_DEBUG \= False/' /asylguiden/asylguiden/settings.py")
        run("sed -i 's/^SECRET_KEY.*/\SECRET_KEY = {0}/' /asylguiden/asylguiden/settings.py".format (id_generator()))


        #sudo('rsync -av /asylguiden_d/* /asylguiden/')
        run('docker-compose build')
        run('docker-compose start')

        #clan out
