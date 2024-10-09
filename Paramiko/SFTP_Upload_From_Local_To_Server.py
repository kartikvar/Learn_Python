import paramiko

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect("andcsv-devdb13d", 22, "oracle", "changeme")

source_path = "D:\\Learn_SDET\\Python\\Codes\\Learn_Python\\Paramiko\\file_from_local_to_server.txt"

sftp = conn.open_sftp()
destination_path = "/d00/Oracle19c/admin/orcl/dpdump/file_from_local_to_server.txt"

sftp.put(source_path, destination_path)

conn.close()
