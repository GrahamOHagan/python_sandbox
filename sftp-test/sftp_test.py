import paramiko
import os

# ----------------------------------
# --- Change the below variables ---
# ----------------------------------
localFile = "test.txt"
remoteFile = f"/Remote_Folder/{localFile}"
hostname = "example.hostname.com"
port = 22
username = "example_username"
password = "example_password"
# ----------------------------------
# ----------------------------------
# ----------------------------------

connect = paramiko.Transport((hostname, port))
connect.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(connect)

if os.path.isfile(localFile):
    sftp.put(localFile, remoteFile)
else:
    raise IOError('Could not find localFile %s !!' % localFile)
    
sftp.close()
connect.close()
