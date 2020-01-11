# -*- coding: ascii -*-
import requests
from lxml import html
from bs4 import BeautifulSoup
import time
import json
import os
import glob
import csv
import excel
from xlsxwriter.workbook import Workbook


#realiza o login
def init_session(login_url):
    with requests.session() as session_requests:
        login_url = "Link"
        result = session_requests.get(login_url, verify = False)
        data_page = html.fromstring(result.text)
    #captura o token da pagina
        authenticity_token = data_page.xpath("//input[@name='authenticity_token']/@value")[0]
        print(str(authenticity_token))
        gerar_dados_login(session_requests, authenticity_token, login_url)

def gerar_dados_login(session_requests, authenticity_token, login_url):
#gera os daddos de autenticacao
    payload = {
        "username": "************",
        "password": "************",
        "authenticity_token": authenticity_token
    }
    print(payload["authenticity_token"])
    login(session_requests, payload, login_url)

def login(session_requests, payload, login_url= "LINK" ):
#realiza login
    post = session_requests.post(login_url, data=payload, headers = dict(referer=login_url))
    print(post.status_code)
    downlaod_csv(session_requests)

def  downlaod_csv(session_requests, url_csv = "LINK" ):
    url_csv = "LINK"

    #result2 = session_requests.get(url, headers=dict(referer=url))
    #print(result2.text)
    nome_arquivo = "arquivo.csv"
    result3 = session_requests.get(url_csv, headers=dict(referer=url_csv))
    if result3.status_code == requests.codes.OK:
        with open(nome_arquivo, 'wb') as novo_arquivo:
                novo_arquivo.write((result3.content))
        print("Download finalizado. Arquivo salvo em: {}".format(url_csv))
    else:
        result3.raise_for_status()


    with open(nome_arquivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')


init_session("Link")


