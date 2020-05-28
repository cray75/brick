import subprocess
import os

packages = ["fail2ban", "clamp", "clamav-daemon", "debsums", "aide", "libpam-cracklib",
                "acct", "sysstat", "auditd", "gcc", "libpcre3-dev", "zliblg-dev", "libluajit-5.1-dev",
                "libpcap-dev", "openssl", "libssl-dev", "libnghttp2-dev", "libdumbnet-dev", "bison", 
                "flex", "libnetd", " zlib1g-dev "]

def install_deps():
    for package in packages:
            process = subprocess.Popen('sudo apt-get install -y ' + package, shell=True, stdin=None, executable="/bin/bash")
            process.wait()

