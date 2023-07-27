#! /usr/bin/python

import time
import daemon
import setproctitle

with daemon.DaemonContext():
    setproctitle.setproctitle("daemontest")
    time.sleep(5*60)  # 5 minutes
