"""
Proje 2
Elinizde 5 kişinin maillerinin ve isimlerinin bulunduğu bir dosya olsun. 
Bu dosyayı okuyarak, her bir kişiye isimleriyle beraber mail göndermeye çalışın. 

Dosya formatı şu şekilde olacak:

                       Mustafa Murat Coşkun,coskun.m.murat@gmail.com
                                       //
                                       //
                                       //
                                       //
                                       
"""


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "ahmetgenez55@gmail.com"

with open("g:/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-14-ileri seviye moduller/14-2-smtp.txt","r",encoding="utf-8") as txt:
    icerik = txt.read()
    liste = icerik.split("\n")
    isimler = []
    mailler = []
    for i in liste:
        a = i.split(",")
        isimler.append(a[0])
        mailler.append(a[1])


mesaj["Subject"] = "Smtp Mail Gönderme Ödevi"


yazi = """

Smtp ile mail gönderiyorum.

Ahmet Genez

"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("ahmetgenez55@gmail.com","a4m3t4e6e9")

    for kime in mailler:
        mesaj["To"] = kime
        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

    print("Mailler Başarıyla Gönderildi....")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()
