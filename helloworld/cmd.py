import os.path
import sys

import helloworld

sys.path.insert(0, os.path.dirname(helloworld.__file__))
from helloworld.openstack.common import processutils

def main():
    out, _ = processutils.execute('uname', '-rms')

    print "Hello from oslo on:", out
