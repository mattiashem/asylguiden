from fabric.api import run, env, local
from fabric.context_managers import cd
from fabric.operations import put, sudo

env.user='ubuntu'


def deploy():
    with cd('/asylguiden'):

        #Copy new files
        sudo('mkdir /asylguiden_d')
        sudo('chown ubuntu:ubuntu /asylguiden_d')
        put('../*', '/asylguiden_d/')
        #run('cp /asylguiden_prod/nginx/tls/asylguiden.crt /asylguiden/nginx/ssl/asylguiden/server.crt')
        #run('cp /asylguiden_prod/nginx/tls/asylguiden.key /asylguiden/nginx/ssl/asylguiden/server.key')
        #run('cp /asylguiden_prod/nginx/tls/bundle.crt /asylguiden/nginx/ssl/asylguiden/bundle.crt')
        #Stoping and buildning new images
        run('docker-compose stop')
        sudo('rsync -av /asylguiden_d/* /asylguiden/')
        run('docker-compose build')
        run('docker-compose start')

        #clan out
        sudo('rm -rf /asylguiden_d')
