from fabric.api import run, env, local
from fabric.context_managers import cd
from fabric.operations import put, sudo
from fabric.contrib.project import rsync_project

env.user='ubuntu'


def deploy():
    with cd('/asylguiden'):

        #Copy files
        #sudo('chown ubuntu:ubuntu /asylguiden_d')
        rsync_project(
            remote_dir="/asylguiden/",
            local_dir="../*",
            exclude=(".git", "*.pyc"),
            )
        #put('../*', '/asylguiden_d/')
        #run('cp /asylguiden_prod/nginx/tls/asylguiden.crt /asylguiden/nginx/ssl/asylguiden/server.crt')
        #run('cp /asylguiden_prod/nginx/tls/asylguiden.key /asylguiden/nginx/ssl/asylguiden/server.key')
        #run('cp /asylguiden_prod/nginx/tls/bundle.crt /asylguiden/nginx/ssl/asylguiden/bundle.crt')
        #Stoping and buildning new images
        run('docker-compose stop')
        #sudo('rsync -av /asylguiden_d/* /asylguiden/')
        run('docker-compose build')
        run('docker-compose start')

        #clan out
