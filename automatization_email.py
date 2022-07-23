import email
from email.message import EmailMessage
import os
import ssl

email_emisor = 'reprogramando@gmail.com'
email_constrasena = os.environ.get('EMAIL_PASSWORD')

email_receptor = 'r.r.d.o@hotmail.com'

asunto = 'Automatizacion correo'
cuerpo = """
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Busject'] = asunto
em.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtlib.SMTP_SSL('smtp.gmail.com', 465, contexto=contexto) as smtp:
  smtp.login(email_emisor, email_constrasena)
  smtp.sendmail(email_emisor, email_constrasena, em.as_string())
