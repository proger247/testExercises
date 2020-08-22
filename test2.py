# Uploading files to the FTP-server 

import ftplib 
import os
import time
import localset


ftp = ftplib.FTP('speedtest.tele2.net', 'anonymous', 'XXXX')
ftp.cwd('upload')
ftp.sendcmd('PASV')
filenames = os.listdir('uploads')
uploading_time = []

for filename in filenames:
	path = os.path.join('uploads', filename)
	begin = time.time()
	
	with open(path, 'rb') as file_to_upload:
	 	transfer_to_server = ftp.storbinary('STOR ' + filename, file_to_upload)
	
	uploading_time.append((time.time()-begin))
	file_size = os.stat(path).st_size / 125000
	uploading_speed = round((file_size / uploading_time[-1]), 2)
	assert transfer_to_server == "226 Transfer complete.", "Uploading error!"
	print(f"Время загрузки файла {filename} составляет {uploading_time[-1] * 1000} мc \nСредняя скорость загрузки {uploading_speed} Mbit/s \n\n")

ftp.quit()
