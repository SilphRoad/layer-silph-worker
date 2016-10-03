from charms.reactive import (
    when,
    when_not,
    set_state,
)

from charmhelpers.core.hookenv import unit_get
from charms.layer import php


@when('silph-web.ready')
@when_not('silph-worker.ready')
def install_silph_worker():
    php.stop()
    set_state('silph-worker.ready')


@when('database.connected')
def configure_database(mysql):
    host = unit_get('private-address')
    mysql.configure('silph-web', 'worker', host)
