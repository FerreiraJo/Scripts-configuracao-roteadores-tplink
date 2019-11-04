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
        login_url = "https://redmine.intranet.gertec/login?back_url=http%3A%2F%2F172.18.1.26%2F"
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

def login(session_requests, payload, login_url= "https://redmine.intranet.gertec/login?back_url=http%3A%2F%2F172.18.1.26%2F" ):
#realiza login
    post = session_requests.post(login_url, data=payload, headers = dict(referer=login_url))
    print(post.status_code)
    downlaod_csv(session_requests)

def  downlaod_csv(session_requests, url_csv = "https://redmine.intranet.gertec/issues.csv" ):
    url_csv = "https://redmine.intranet.gertec/issues.csv?c%5B%5D=project&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&c%5B%5D=priority&c%5B%5D=fixed_version&c%5B%5D=estimated_hours&c%5B%5D=cf_22&f%5B%5D=status_id&f%5B%5D=cf_22&f%5B%5D=&group_by=&op%5Bcf_22%5D=%2A&op%5Bstatus_id%5D=o&set_filter=1&t%5B%5D=estimated_hours&t%5B%5D=spent_hours&utf8=%E2%9C%93"

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

#converter_csv_para_xls(nome_arquivo)


''''
def converter_csv_para_xls(nome_arquivo):
    for csvfile in glob.glob(os.path.join('C:\\Users\\joferreira\\PycharmProjects\\Get_Tickets', '*.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(nome_arquivo, 'rt', encoding='ascii') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()
'''

init_session("https://redmine.intranet.gertec/login?back_url=http%3A%2F%2F172.18.1.26%2F")


