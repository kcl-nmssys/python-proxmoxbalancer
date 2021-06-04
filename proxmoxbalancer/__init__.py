import os
from datetime import datetime
from .proxmoxbalancer import ProxmoxBalancer


def balance():
    print("Started at %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if "https_proxy" in os.environ:
        del os.environ["https_proxy"]

    balancer = ProxmoxBalancer()
    balancer.balance()

    print("Finished at %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
