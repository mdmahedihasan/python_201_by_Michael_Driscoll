import ftplib


def ftp_upload(ftp_obj, path, ftype = "TXT"):
    if ftype == "TXT":
        with open(path) as fobj:
            ftp.storlines("STOR" + path, fobj)
    else:
        with open(path, "rb") as fobj:
            ftp.storbinary("STOR" + path, fobj, 1024)


if __name__ == '__main__':
    ftp = ftplib.FTP("host", "username", "password")
    ftp.login()

    path = "/home/mahedi/Desktop/new.txt"
    ftp_upload(ftp, path, ftype="PDF")

    ftp.quit()