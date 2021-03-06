from __future__ import with_statement
from fabric.api import *
from fabric.contrib.files import exists

import os
from StringIO import StringIO

env.hosts = ['root@172.22.26.7']

env.shell = '/bin/sh -c'

def pre_cmd():
    run('mount -o remount,rw /')

def post_cmd():
    run('mount -o remount,ro /')

def etckeeper_check():
    run('etckeeper pre-install')

def etckeeper_commit(message):
    run('if etckeeper unclean; then etckeeper commit "%s"; fi' % message)

def etckeeper_done():
    run('etckeeper post-install')

def update_configs():
    for plugin in os.listdir('usr/share/munin/plugins'):
        if plugin != 'dorfmap_':
            run('ln -fs /usr/share/munin/plugins/%s /etc/munin/plugins' % plugin)

    for area in ['Hackcenter', 'Lounge', 'Nomspace', 'Schleuse', 'Werkstatt']:
        run('ln -fs /usr/share/munin/plugins/dorfmap_ /etc/munin/plugins/dorfmap_%s' % area)

def deploy(version):
    pre_cmd()
    etckeeper_check()
    put("../dorfmon_%s_all.deb" % version, '/root/', use_sudo=True)
    run("dpkg --install /root/dorfmon_%s_all.deb" % version)
    run("rm /root/dorfmon_%s_all.deb" % version)
    update_configs()
    etckeeper_done()
    post_cmd()
    restart_daemons()
