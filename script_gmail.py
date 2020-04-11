import smtplib,sys,os,getpass,re
from time import sleep
from colorama import init, Fore, Back, Style,Cursor
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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

try:
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    #server.ehlo()
    print(FG+B,"Conectado!"+FW)
    sleep(1)
except:
    print(FR+B+"[ERROR]: "+FW+"Se prdujo un error durante la coneccion")
    sleep(1)


#sendemail('mail_destinatario','tugmail@gmail.com')
def banner():
    print(Style.DIM+"╔════════════════════════════════════════════════════════════════════╗"+SR)
    print("║                                                                    ║")
    print(B+"║    "+B+ "Bienvenido a mi herramienta para envios de mensajes",R,"GMAIL      "+B+"║"+SR)
    print("║                            "+FB+B+"BY:"+FA+"Lman"+FW+B+"                                 ║")
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
    os.system ("cls") 
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
        os.system ("cls")
        try:
            login(pr,cr)
            sleep(1)
        except:
            print(FR+B+"[ERROR LOGIN]: "+FW+"Por favor revise sus credenciales o que tenga permitido el\n uso de aplicaciones no seguras en su cuenta")
            sleep(2)

        arch_adjunto(adj)
        sleep(1)
        try:
            enviar_mensaje(asu,sms,cd,cr)
            sleep(1)
        except:
            print(FR+B+"[ERROR ENVIO]: "+FW+"Error al enviar el mensaje")
            sleep(2)
        
        print(FB+B+"Mensaje enviado exidosamente")
        server.quit()

        
    elif o.isdigit() == False and aux == False:
        print(FR,B,"[ERROR]:",FW,"Por favor ingrese solo numeros")
        sleep(1)
    
    else:
        o = int(o)
        if o > 0 and o < 7 or o == 99:
            if o == 1:
                while True:
                    os.system ("cls")
                    patron = re.compile(r'@gmail.com$')
                    print(FG,"Correo del remitente: ",FW)
                    cr = input()
                    if patron.search(cr) != None:
                        break
                    else:
                        print(FR,B,"[ERROR CORREO]:",FW,"Se admiten solo correos gmail")
            if o == 2:
                while True:
                    os.system ("cls")
                    print(FG,"Clave del remitente: ",FW)
                    pr = getpass.getpass()
                    break
            if o == 3:
                while True:
                    os.system ("cls")
                    print(FG,B+"Para(Correo del receptor): ",FW)
                    cd = input()
                    break
            if o == 4:
                while True:
                    os.system ("cls")
                    print(FG,B+"Mentaje en formato HTML(Doble enter para terminar): ",FW)
                    lines = []
                    while True:
                        line = input()
                        if line:
                            lines.append(line)
                        else:
                            break
                    sms = '\n'.join(lines)
                    break
            if o == 5:
                while True:
                    os.system ("cls")
                    print(FG,"Archibo adjunto (path): ",FW)
                    adj = input()
                    break
            if o == 6:
                while True:
                    os.system ("cls")
                    print(FG,"Asunto: ",FW)
                    asu = input()
                    break
            if o == 99:
                    os.system ("cls")
                    print(FR+B,"Saliendo...",FW)
                    sleep(2)
                    server.quit()
                    exit()
        else:
            print(FR,B,"[ERROR]:",FW,"Por favor solo ingrese valores del 1 al 6 o 99")
            sleep(1)




