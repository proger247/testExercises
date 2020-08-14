# import ftputil
# import warnings
# warnings.filterwarnings("ignore")

# host='speedtest.tele2.net/'
# username='anonymous'
# password=''

# # Соединяемся с FTP сервером и получаем список файлов и папок

# try:
#     ftp_host=ftputil.FTPHost(host, username, password)
#     ftp_host.use_list_a_option = False

#     with ftp_host:
#             list = ftp_host.listdir(ftp_host.curdir)
#             for fname in list:
#                 # Если нашли папку то пробуем загрузить в нее файл test.txt
#                 if ftp_host.path.isdir(fname):
#                     print(fname+' (папка)')
#                     try:
#                         # Закачивание
#                         ftp_host.upload('test.txt', '/'+fname+'/test.txt')
#                         print("Файл загружен в папку "+fname)
#                     except:
#                         print("Папка недоступна для записи")
#                 else:
#                     # Если это не папка а файл то печатаем его имя
#                     # Если в имени файла есть расширение .zip скачиваем этот файл
#                     print(fname+' (файл)')
#                     if('.zip' in fname):
#                         print('Скачиваю файл '+fname)
#                         # Скачивание
#                         ftp_host.download(fname, 'downloads/'+fname)
#                         print('Файл '+fname+' успешно скачан')
# except:
#     print('Сервер не отвечает')


# from ftplib import FTP

# ftp = FTP('speedtest.tele2.net')
# ftp.login()
# # # ftp.cwd('devel')

# data = ftp.retrlines()

# print(f'\n{data}')

import ftplib 
import os
import time


ftp = ftplib.FTP('speedtest.tele2.net')
ftp.login()
filenames = ftp.nlst()
filenames = filenames[8::]
filenames = filenames[::4]
time_lost = []
print(filenames)
# begin = time.time()
for filename in filenames:
	begin = time.time()

	host_file = os.path.join('.', filename)

	try:
		with open(host_file, 'wb') as local_file:
			ftp.retrbinary('RETR ' + filename, local_file.write)
	except ftplib.error_perm:
		pass
	time_lost.append((time.time() - begin) * 1000)
ftp.quit()

print(time_lost)


time.sleep(5)


def ftp_upload(ftp_obj, path):

	if ftype == 'TXT':
		with open(path) as fobj:
			ftp.storlines('STOR' + path, fobj)
	else:
		with open(path, 'rb') as fobj:
			ftp.storbinary('STOR' + path, fobj, 1024)


ftp = ftplib.FTP('speedtest.tele2.net')
ftp.login()

if __name__ == '__main__':

	for filename in filenames:
	
		path = os.path.join('.', filename)
		ftp_upload(ftp, path, ftype = 'ZIP')

		ftp.quit()



