# @Author: drxos
# @Date:   2016-08-14T02:27:26+01:00
# @Email:  drxost@gmail.com
# @Project: zbraaku
# @Last modified by:   drxos
# @Last modified time: 2016-08-15T11:52:58+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)



from fabric.api import *

from zbraa.utils import gen_secret_key

# env variables
# ------------------------------------------------------------------------------
env.hosts = ['37.139.29.66']
env.user = "root"

# Local fab
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# git commit
# ------------------------------------------------------------------------------
def ci(act='new', aud='dev', msg='empty', tag='wip'):
    local('git add .')
    local('git commit -m "%s: %s: %s !%s"' % (act, aud, msg, tag))

# Server fab
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Init dokku app
# ------------------------------------------------------------------------------
def initapp():
    run('dokku apps:create zbraa')
    run('dokku domains:add zbraa zbraa.com')
    run('dokku config:set zbraa DJANGO_SECRET_KEY="%s"' % gen_secret_key())
    run('dokku docker-options:add zbraa deploy "-v /apps/zbraa/media:/app/media"')

# Init database
# ------------------------------------------------------------------------------
def initdb():
    run('dokku postgres:create zbraa')
    run('dokku postgres:link zbraa zbraa')

# Migrate
# ------------------------------------------------------------------------------
def migrate():
    run('dokku run zbraa python manage.py migrate')

# deploy
# ------------------------------------------------------------------------------
def deploy():
    initapp()
    initdb()
    migrate()
    local('git push dokku master')
