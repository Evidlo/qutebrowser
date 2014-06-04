"""Profile qutebrowser."""

import sys
import cProfile
import os.path
from os import getcwd
from tempfile import mkdtemp
from subprocess import call
from shutil import rmtree

sys.path.insert(0, getcwd())

import qutebrowser.qutebrowser  # pylint: disable=unused-import

tempdir = mkdtemp()

if '--profile-keep' in sys.argv:
    sys.argv.remove('--profile-keep')
    profilefile = os.path.join(getcwd(), 'profile')
else:
    profilefile = os.path.join(tempdir, 'profile')
callgraphfile = os.path.join(tempdir, 'callgraph')

profiler = cProfile.Profile()
profiler.run('qutebrowser.qutebrowser.main()')
profiler.dump_stats(profilefile)

call(['pyprof2calltree', '-k', '-i', profilefile, '-o', callgraphfile])
rmtree(tempdir)
