from ftplib import FTP


ftp = FTP("ftp.cse.buffalo.edu")
ftp.login()
ftp.retrlines("LIST")
print(ftp.cwd("mirror"))
ftp.retrlines("LIST")
print(ftp.cwd("mirror"))
ftp.retrlines("LIST")