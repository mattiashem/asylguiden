rom fabric.api import run, env, local
from fabric.context_managers import cd

env.user='ubuntu'


def deploy():
    with cd('/asylguiden'):
        run('docker-compose stop')
        local('rsync -avz * {0}@{1}:/asylguiden/'.format(env.user,env.hosts))
        run('cp /asylguiden_prod/nginx/tls/asylguiden.crt /asylguiden/nginx/ssl/asylguiden/server.crt')
        run('cp /asylguiden_prod/nginx/tls/asylguiden.key /asylguiden/nginx/ssl/asylguiden/server.key')
        run('cp /asylguiden_prod/nginx/tls/bundle.crt /asylguiden/nginx/ssl/asylguiden/bundle.crt')
        run('docker-compose build')
        run('docker-compose start')