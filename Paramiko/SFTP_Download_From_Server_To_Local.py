import paramiko

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect("andcsv-devdb13d", 22, "oracle", "changeme")

sftp = conn.open_sftp()
source_path = "/d00/Oracle19c/admin/orcl/dpdump/file_from_server_to_local.txt"
destination_path = "D:\\Learn_SDET\\Python\\Codes\\Learn_Python\\Paramiko\\file_from_server_to_local.txt"

sftp.get(source_path, destination_path)

conn.close()
