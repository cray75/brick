import subprocess
import os

def configure_node_exporter(): 
    server = "172.31.18.149"
    os.chdir("/home/ubuntu")
    make_node_user = subprocess.Popen('useradd --no-create-home --shell /bin/false node_exporter', shell=True, stdin=None, executable="/bin/bash")
    make_node_user.wait()
    get_node_exporter = subprocess.Popen('wget https://github.com/prometheus/node_exporter/releases/download/v0.18.1/node_exporter-0.18.1.linux-amd64.tar.gz && tar xvf node_exporter-0.18.1.linux-amd64.tar.gz && cd node_exporter-0.18.1.linux-amd64',
                                          shell=True, stdin=None, executable="/bin/bash")
    get_node_exporter.wait()
    os.chdir("/home/ubuntu/node_exporter-0.18.1.linux-amd64")
    set_permissions = subprocess.Popen('cp node_exporter /usr/local/bin && chown node_exporter:node_exporter /usr/local/bin/node_exporter',
                                        shell=True, stdin=None, executable="/bin/bash")
    set_permissions.wait()
    os.chdir("/home/ubuntu")
    clean_up = subprocess.Popen('rm -rf node_exporter-0.18.1.linux-amd64 node_exporter-0.18.1.linux-amd64.tar.gz', shell=True, stdin=None, executable="/bin/bash")
    clean_up.wait()
    os.chdir("/etc/systemd/system/")
    f = open("node_exporter.service", "w+")
    f.write("[Unit] \n"
            "Description=Node Exporter \n"
            "Wants=network-online.target \n"
            "After=network-online.target \n \n"

            "[Service] \n"
            "User=node_exporter \n"
            "Group=node_exporter \n"
            "Type=simple \n"
            "ExecStart=/usr/local/bin/node_exporter \n \n"

            "[Install] \n"
            "WantedBy=multi-user.target")
    f.close()
    open_port = subprocess.Popen('ufw allow from ' + server + ' to any port 9100', shell=True, stdin=None, executable="/bin/bash")
    open_port.wait()
    enable_service = subprocess.Popen('systemctl daemon-reload && systemctl enable node_exporter && systemctl start node_exporter', shell=True, stdin=None, executable="/bin/bash")
    enable_service.wait()
    print('node exporter installed')