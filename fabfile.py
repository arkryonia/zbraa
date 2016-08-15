# @Author: drxos
# @Date:   2016-08-14T02:27:26+01:00
# @Email:  drxost@gmail.com
# @Project: zbraaku
# @Last modified by:   drxos
# @Last modified time: 2016-08-15T11:52:58+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)



from fabric.api import local


def hello(name="world", gender="M"):
    print("Hello %s (%s)!" % (name, gender))

def ci(act='new', aud='dev', msg='empty', tag='wip'):
    local('git add .')
    local('git commit -m "%s: %s: %s: %s"' % (act, aud, msg, tag))
    local('gitchangelog > CHANGELOGS.md && git commit --amend')
    run('print "Hello!"')
