#program to hash strig data by using 3 algorithms 
import hashlib

s1=hashlib.sha1(b'hello world')
h1=s1.hexdigest()
print(h1)

s2=hashlib.sha224(b'hello world')
h2=s2.hexdigest()
print(h2)

s3=hashlib.sha256(b'hello world')
h3=s3.hexdigest()
print(h3)