import ftplib 
import os
import time

# Loading files from FTP-server 
ftp = ftplib.FTP('speedtest.tele2.net')
ftp.login()
filenames = ftp.nlst()
filenames = filenames[8::]
filenames = filenames[::4]
loading_time = []
print(filenames)


for filename in filenames:
	begin = time.time()

	host_file = os.path.join('loads', filename)

	try:
		with open(host_file, 'wb') as local_file:
			ftp.retrbinary('RETR ' + filename, local_file.write)
	except ftplib.error_perm:
		pass
	loading_time.append((time.time() - begin) * 1000)
	
ftp.quit()

print(loading_time)

# Uploading files to the FTP-server 
uploading_time = []
ftp = ftplib.FTP('speedtest.tele2.net', 'anonymous', 'XXXX')
ftp.cwd('upload')

filenames = os.listdir('uploads')
ftp.sendcmd('PASV')


for filename in filenames:
	path = os.path.join('uploads', filename)
	begin = time.time()
	print(filename)
	with open(path, 'rb') as file_to_upload:
	 	transfer_to_server = ftp.storbinary('STOR ' + filename, file_to_upload)
	uploading_time.append((time.time()-begin) * 1000)
	print(transfer_to_server)

print(uploading_time)
print(ftp.nlst())

ftp.quit()


