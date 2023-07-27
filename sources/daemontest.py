#! /usr/bin/python

import os
import sys
import time
import daemon
import subprocess
import setproctitle

if os.fork() == 0:
    sys.stderr.write("== PID=" + str(os.getpid()) + " starts daemon test processes ==\n")

    # child ends up as daemon.
    with daemon.DaemonContext():
        title = "daemontest PID=" + str(os.getpid())
        setproctitle.setproctitle(title)
        time.sleep(5*60)  # 5 minutes

else:
    time.sleep(3)
    subprocess.call("pgrep daemontest -a >&2", shell=True)
