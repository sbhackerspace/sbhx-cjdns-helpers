#!/usr/bin/env python

import re
import sys

USAGE = """Usage: ./cjdns/python/contrib/%s remote_host_port password public_key

e.g., %s 123.123.123.123:4321 rgzvtkfmv1qv9k3f4ls3zr2hxx7w1v1 r3791g2tdn22bg8cu3c622ubfvmut75d3dzdxms71hw4fn9m0t3z.k""" % (sys.argv[0], sys.argv[0])

if len(sys.argv) < 4:
    print USAGE
    sys.exit(1)

remote_host_port, password, public_key = sys.argv[1:4]

CJDROUTE_CONF = '../../cjdroute.conf'

f = open(CJDROUTE_CONF, 'r')
conf = f.read()
f.close()

connect_to = re.findall(r'("connectTo":.+?)["}]', conf, re.DOTALL)[0]

new_connect_to = connect_to + '''"%s": {
                        "password": "%s",
                        "publicKey": "%s"
                    },
                ''' % (remote_host_port, password, public_key)
conf = conf.replace(connect_to, new_connect_to, 1)

f = open(CJDROUTE_CONF, 'w')
f.write(conf)
f.close()
