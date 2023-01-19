import smtplib
import email.message

#definir as variaveis
assunto = 'teste de e-mail automatico' #titulo do email
origem = 'seu-email-aqui' #de qual email sera enviado
destino = 'email-de-destino-aqui' #para qual email sera enviado
senha = 'sua-senha-aqui' #senha gerada pelo gmail (passo a passo no readme)

#definir a mensagem do e-mail dentro das aspas triplas. Obs: o corpo do texto pode ser em formato html
corpo_do_email = '''
    Esse é um texto de envio de email
    '''

#Função para enviar o e-mail.
def enviar_email(Assunto, Origem, Destino, Senha, Corpo_do_email):
    
    

    #instancia a mensagem
    mensagem = email.message.Message() 
    mensagem['Subject'] = Assunto
    mensagem['From'] = Origem
    mensagem['To'] = Destino
    mensagem.add_header('Content-Type', 'text/html')
    mensagem.set_payload(Corpo_do_email)

    #instancia o protocolo 
    smt = smtplib.SMTP('smtp.gmail.com: 587')
    smt.starttls()

    #faz o login com as credenciais
    smt.login(mensagem['From'], Senha)

    #envia o email
    smt.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))

    print(f'email enviado de {Origem} para {Destino} com sucesso')


enviar_email(assunto, origem, destino,senha,corpo_do_email)