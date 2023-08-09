import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from login import lista



for usuario in lista():

    Respuesta = input("ingrese su usuario")

    if Respuesta == usuario:
        codigoo = random.randint(100000, 999999)
        password = "khxqwlwstfmbxxcj"
        me = "carreramatias1707@gmail.com"
        you = input("Ingrese su email  >>>")

        email_boady = f"""
                    <html><boady><p>Hola,gracias por iniciar sesion.  \n Su codigo de verificacion es {codigoo}</p></boady></html> 
                    """

        message = MIMEMultipart("alternative", None, [MIMEText(email_boady, "html")])
        message["subject"] = "CODIGO DE VERIFICACION "
        message["from"] = me
        message["to"] = you

        try:
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(me, password)
            server.sendmail(me, you, message.as_string())
            server.quit()
            Verificacion = int(input("Ingrese el codigo de verificacion que le ha llegado "))
            if Verificacion == codigoo:
                print("Se ha iniciado sesion correctamente")
        except Exception as e:
            print(f"Error al enviar el email:{e}")
    elif Respuesta != usuario:
        print("usted no se ha registrado, por favor registrese")




