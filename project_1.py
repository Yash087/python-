#code to generate md5 of string data
import hashlib
text="hello world"
t=text.encode("utf-8")
hash=hashlib.md5(t)
hexa=hash.hexdigest()
print(hexa)