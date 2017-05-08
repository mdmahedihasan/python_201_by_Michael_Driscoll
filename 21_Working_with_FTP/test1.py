from ftplib import FTP


ftp = FTP("ftp.cse.buffalo.edu")
print(ftp.login())