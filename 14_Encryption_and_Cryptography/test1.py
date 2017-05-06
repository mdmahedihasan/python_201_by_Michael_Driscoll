import hashlib


md5 = hashlib.md5()
# print(md5.update("python rocks!"))
print(md5.update(b"Python rocks!"))
print(md5.digest())
print(md5.hexdigest())

sha = hashlib.sha1(b"hello python").hexdigest()
print(sha)