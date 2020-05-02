
import base64
data = open("base64.txt", "r").read()
decoded = base64.b64decode(data)
print ("decoded")
photo=base64.b64decode(data)
f=open('snap.png','wb')
f.write(photo)
f.close()
