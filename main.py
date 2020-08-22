import ftplib 
import os
import time
import localset

# Loading files from FTP-server 
ftp = ftplib.FTP('speedtest.tele2.net', 'anonymous', 'XXXX')
filenames = ftp.nlst()
filenames = localset.cut_list(filenames) # local settings
loading_time = []
print(filenames)


for filename in filenames:
	
	host_file = os.path.join('loads', filename)
	begin = time.time()

	with open(host_file, 'wb') as local_file:
		ftp.retrbinary('RETR ' + filename, local_file.write)
	
	loading_time.append((time.time() - begin))
	file_size = os.stat(host_file).st_size / 125000 # size of the loaded file in Mbits
	loading_speed = round((file_size / loading_time[-1]), 2)
	# print(size)
	print(f"Время скачивания файла {filename} составляет {loading_time[-1] * 1000} мc \nСредняя скорость скачивания {loading_speed} Mbit/s")

ftp.quit()


# Uploading files to the FTP-server 
uploading_time = []
ftp = ftplib.FTP('speedtest.tele2.net', 'anonymous', 'XXXX')
ftp.cwd('upload')

filenames = os.listdir('uploads')
ftp.sendcmd('PASV')


for filename in filenames:
	path = os.path.join('uploads', filename)
	begin = time.time()
	
	with open(path, 'rb') as file_to_upload:
	 	transfer_to_server = ftp.storbinary('STOR ' + filename, file_to_upload)
	
	uploading_time.append((time.time()-begin))
	file_size = os.stat(path).st_size / 125000
	uploading_speed = round((file_size / uploading_time[-1]), 2)
	print(transfer_to_server)
	print(f"Время загрузки файла {filename} составляет {uploading_time[-1] * 1000} мc \nСредняя скорость загрузки {uploading_speed} Mbit/s")


ftp.quit()

data = {'filename': filenames, 'loading_time (ms)': loading_time, 'uploading_time (ms)': uploading_time}

