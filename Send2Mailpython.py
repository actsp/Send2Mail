#TO SEND A E-MAIL WITH AN ATTACHMENT
#lINK: https://mailtrap.io/blog/python-send-email-gmail/
import streamlit as st
import pandas as pd
from PIL import Image
import openpyxl

#import smtplib
#from email import encoders
#from email.mime.base import MIMEBase
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.mime.image import MIMEImage

from pathlib import Path

import time
import pytz
from datetime import datetime

from Send2MaillMSK import Send2Mail

millis = str(round(time.time() * 1000))

image01 = Image.open('pixabay300x256.png')
image02 = Image.open('act_logo300x200.png')
st.sidebar.image(image01, width=300, caption='Envio automático de e-mail') 
Titulo_Laterial = '<p style="font-weight: bolder; color:Blue; font-size: 18px;">Aplicativo Web para envio automático de e-mail</p>'
st.sidebar.markdown(Titulo_Laterial, unsafe_allow_html=True)
mystyle1 =   '''<style> p{text-align:center;}</style>'''
st.markdown(mystyle1, unsafe_allow_html=True)
st.sidebar.image(image02, width=300, caption='Desenvolvedor: Massaki de O. Igarashi') 

Titulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 86px;">act.MAIL 1.0</p>'
st.markdown(Titulo_Principal, unsafe_allow_html=True)
mystyle1 =   '''<style> p{text-align:center;}</style>'''
st.markdown(mystyle1, unsafe_allow_html=True)

#INSERÇÃO DE DADOS COMUNS ÀS DUAS ABAS TAB
st.subheader("1º Passo: Digite o Remetente.")
FROM = st.text_input("Digite o remetente: ", "informacoes.actsp@gmail.com")
st.subheader("2º Passo: Digite o Assunto.")
ASSUNTO = st.text_input("Digite o assunto: ", "FELICIDADES 2024") 
Fname = st.text_input("Nome do arquivo anexo (Salvo no GitHub):", "niver.jpeg")
st.subheader("3º Passo: Digite a mensagem e Insira o anexo!")

MSG = " "
m = st.text_area("Digite sua mensagem aqui:", "Olá! \n Passando para desejar \n um Próspero 2024 \n repleto de Alegria, \n Saúde \n e Prosperidade! \n São os votos da família ACT.SP")
if m is not None:
    textsplit = m.splitlines()
    for x in textsplit:
        #st.write(x)
        MSG+=x + " \n "   

st.subheader("4º Passo: Escolha envio Simples ou Lista de Destinatários.")
#SEPARAÇÃO DE DADOS SIMPLES E ENVIO MÚLTIPLOS EM ABAS TAB
tab1, tab2 = st.tabs(["SIMPLES", "LISTA"])
with tab1:
    form = st.form('Dados de envio')
    TO = form.text_input("Digite a(o) destinatária(o): ", "massaki.igarashi@gmail.com")
           
    if form.form_submit_button(label = '✔️ ENVIAR'):
        st.write(Send2Mail(Fname,FROM, TO, ASSUNTO, MSG))
with tab2:
    #df = get_data()
    #st.dataframe(df)
    #for i in range(len(df)):
    #    st.write(df['e-mail'][i])
    st.subheader("5º Passo: Carregue o arquivo Excel com a lista de e-mails para envio em lote.")
    data = st.file_uploader("Faça Upload da Lista.XLSX para envio em lote.", type=["xlsx"])
    if data is not None:
        df = pd.read_excel(data)
        st.dataframe(df)
        if st.button(label = '✔️ ENVIAR PARA LISTA'):
            for i in range(len(df)):
                st.write(Send2Mail(Fname,FROM, df['e-mail'][i], ASSUNTO, MSG))
