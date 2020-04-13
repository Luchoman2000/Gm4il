import getpass
import os
import re
import smtplib
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

from colorama import Back, Cursor, Fore, Style, init

init()
B = Style.BRIGHT
R = Style.NORMAL
SR = Style.RESET_ALL
FG = Fore.GREEN
FY = Fore.YELLOW
FB = Fore.CYAN
FR = Fore.RED
FW = Fore.RESET
FA = Fore.BLUE
cr = ''
pr = ''
cd = ''
sms = """"""
adj = ''
asu = ''
msg = MIMEMultipart()
aux = False
server = smtplib.SMTP('smtp.gmail.com: 587')
def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
def conectar():
    try:
        server.starttls()
        #server.ehlo()
        print(FG+B,"Conectado!"+FW)
        sleep(1)
    except:
        print(FR+B+"[ERROR]: "+FW+"Se prdujo un error durante la coneccion")
        sleep(1)



def banner():
    print(Style.DIM+"╔════════════════════════════════════════════════════════════════════╗"+SR)
    print("║                                                                    ║")
    print(B+"║    "+B+ "Bienvenido a mi herramienta para envios de mensajes",R,"GMAIL      "+B+"║"+SR)
    print("║                            "+FB+B+"BY:"+FA+"Lman"+FW+B+"                                 "+R+"║")
    print(Style.DIM+"╚════════════════════════════════════════════════════════════════════╝"+SR)

def login(pas,adress):
    
    print(FY+B,"Logeando...\n"+FW)
    msg['From'] = adress
    server.login(msg['From'], pas)
    print(FG+B,"Logeo completo :D"+FW)

def enviar_mensaje(tema,sms,to_address,adress):
    print(FY+B,"Enviando...\n"+FW)
    msg['From'] = adress
    msg['To'] = to_address
    msg['Subject'] = tema
    body = sms
    msg.attach(MIMEText(body, 'html'))
    #msg.add_header('Content-Type', 'text/html')
    #msg.set_payload(sms)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    print(FG+B,"Enviado! :D\n"+FW)

def arch_adjunto(adj):
    print(FY+B,"Adjuntando...\n"+FW)
    nombre_archivo = adj
    adjunto = open(nombre_archivo, "rb")
    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload((adjunto).read())
    encoders.encode_base64(parte)
    parte.add_header('Content-Disposition','attachment', filename=nombre_archivo)
    msg.attach(parte)
    print(FG+B,"Adjuntado :D\n"+FW)

while True:
    clear()
    banner()
    print(B+"[*]:",R+"Para realizar el envio correctamente debe llenar los siguentes parametros:\n")

    if len(cr) != 0 and len(pr) != 0 and len(cd) != 0 and len(sms) != 0  and len(adj) != 0 and len(asu) != 0:
        print(FG,B,"> Listo para enviar <",FW)
        print(FW,B,"Enviar?",FG,"['y']",FW,"si\n")
        aux = True
    else:
        print(FR,B+"> Campos Incompletos <",FW)
        aux = False

    print(B+"   ["+FG+"1"+FW+"]:",R+"Correo del remitenete:   "+FY+cr+FW)
    if len(pr) != 0:
        print(B+"   ["+FG+"2"+FW+"]:",R+"Clave del remitente:     "+FY+"OK."+FW)
    else:
        print(B+"   ["+FG+"2"+FW+"]:",R+"Clave del remitente:     ")
    print(B+"   ["+FG+"3"+FW+"]:",R+"Correo del destinatario: "+FY+cd+FW)
    if len(sms) != 0:
        print(B+"   ["+FG+"4"+FW+"]:",R+"Mensaje en formato HTML: "+FY+"OK."+FW)
    else:
        print(B+"   ["+FG+"4"+FW+"]:",R+"Mensaje en formato HTML: ")

    print(B+"   ["+FG+"5"+FW+"]:",R+"Archibo adjunto (path):  "+FY+adj+FW)
    print(B+"   ["+FG+"6"+FW+"]:",R+"Asunto:                  "+FY+asu+FW)

    print(B+"   ["+FR+"99"+FW+"]:",R+"Para salir.")

    o = input("Elige que quieres llenar: ")

    if o == 'y' and aux == True :
        clear()
        conectar()
        try:
            login(pr,cr)
            sleep(1)
            arch_adjunto(adj)
            sleep(1)
            enviar_mensaje(asu,sms,cd,cr)
            print(FB+B+"Mensaje enviado exidosamente"+FW+R)
            server.quit()
        except OSError:
            print(FR+B+"[ERROR ADJUNTAR]: "+FW+"Procura que el archivo que deseas enviar esta en la misma carpeta\n que el script ")
            sleep(2)
        except :
            print(FR+B+"[ERROR LOGIN]: "+FW+"Por favor revise sus credenciales o que tenga permitido el\n uso de aplicaciones no seguras en su cuenta")
            sleep(2)
        
        #except:
        #    print(FR+B+"[ERROR ENVIO]: "+FW+"Error al enviar el mensaje")
         #   sleep(2)
        
        
        

        
    elif o.isdigit() == False and aux == False:
        print(FR,B,"[ERROR]:",FW,"Por favor ingrese solo numeros")
        sleep(1)
    elif o != 'y' and aux ==True and o.isdigit() == False:
        print(FR,B,"[ERROR]:",FW,"Ingreso no permitido")
        sleep(1)
    
    else:
        o = int(o)
        if o > 0 and o < 7 or o == 99:
            if o == 1:
                a = cr
                while True:
                    clear()
                    
                    patron = re.compile(r'@gmail.com$')
                    print(FG,B+"Correo del remitente: ",FW+FB+"\tpara cancelar['X']",FW)
                    
                    cr = input()

                    if patron.search(cr) != None:
                        break
                    elif cr == 'X':
                        cr = a
                        break
                    else:
                        print(FR,B,"[ERROR CORREO]:",FW,"Se admiten solo correos gmail")
                        sleep(1)
            if o == 2:
                a = pr
                while True:
                    clear()
                    print(FG,"Clave del remitente: ",FW+FB+"\tpara cancelar['X']",FW)
                    
                    pr = getpass.getpass()
                    if pr == 'X':
                        pr = a
                        break
                    break
            if o == 3:
                a = cd
                while True:
                    clear()
                    print(FG,B+"Para(Correo del receptor): ",FW+FB+"\tpara cancelar['X']",FW)
                    
                    cd = input()
                    if cd == 'X':
                        cd = a
                        break
                    break
                    
            if o == 4:
                a =sms
                while True:
                    clear()
                    print(FG,B+"Mentaje en formato HTML(Doble enter para terminar): ",FW+FB+"\tpara cancelar['X']",FW)
                    
                    lines = []
                    while True:
                        line = input()
                        if line:
                            lines.append(line)
                        else:
                            break
                    sms = '\n'.join(lines)

                    
                    if sms == 'X':
                        sms = a
                        break
                    break
            if o == 5:
                a = adj
                while True:
                    clear()
                    print(FG,B+"Nombre de archivo a adjuntar Ej. 'texto.txt'\n (el archivo debe estar en la misma carpeta del script): ",FW+FB+"\tpara cancelar['X']",FW)
                    
                    
                    adj = input()
                    if adj == 'X':
                        adj = a
                        break
                    break
            if o == 6:
                a = asu
                while True:
                    clear()
                    print(FG,B+"Asunto: ",FW+FB+"\tpara cancelar['X']",FW)
                    
                    asu = input()
                    if asu == 'X':
                        asu = a
                        break
                    break
            if o == 99:
                    clear()
                    print(FR+B,"Saliendo...",FW)
                    sleep(2)
                    server.quit()
                    exit()
        else:
            print(FR,B,"[ERROR]:",FW,"Por favor solo ingrese valores del 1 al 6 o 99")
            sleep(1)
