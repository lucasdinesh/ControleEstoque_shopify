from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
import smtplib


class Email:
   def enviar_email(self, emailcliente ,cliente, pedido=0) :
        meu_email = ''
        senha = '2'

        with open('template.html', 'r') as html:
            template = Template(html.read())
            body_msg = template.substitute(nome = cliente)
            print(emailcliente)

        print(body_msg)
        msg= MIMEMultipart()
        msg['from'] = ''
        msg['to']= meu_email
        msg['subject'] = f'Confirmar endereço de entrega pedido {pedido}'

        corpo = MIMEText(body_msg,'html')
        msg.attach(corpo)

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(meu_email, senha)
            smtp.send_message(msg)
        print('Email executado com sucesso')