# Loading files from FTP-server 

import ftplib 
import os
import time
import localset


ftp = ftplib.FTP('speedtest.tele2.net', 'anonymous', 'XXXX')
filenames = ftp.nlst()
# filenames = localset.cut_list(filenames) # local settings, limit files list
loading_time = []

for filename in filenames:
	
	host_file = os.path.join('loads', filename)
	begin = time.time()

	with open(host_file, 'wb') as local_file:
		transfer_from_server = ftp.retrbinary('RETR ' + filename, local_file.write)
	
	loading_time.append((time.time() - begin))
	file_size = os.stat(host_file).st_size / 125000 # size of the loaded file in Mbits
	loading_speed = round((file_size / loading_time[-1]), 2)

	assert transfer_from_server == "226 Transfer complete."
	print(f"Время скачивания файла {filename} составляет {loading_time[-1] * 1000} мc \nСредняя скорость скачивания {loading_speed} Mbit/s \n\n")

ftp.quit()