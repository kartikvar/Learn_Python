import time

import paramiko

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect("andcsv-devdb13d", 22, "oracle", "changeme")

stdin, stdout, stderr = conn.exec_command("cd /d00/Oracle19c/admin/orcl/dpdump \n ./make_directory.sh")
time.sleep(5)
conn.close()
