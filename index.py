import emoji
import requests
import os
from threading import Thread
import time
import json
import datetime
from datetime import date


'''
Developer: Koenomatachi San
Description: Monitoring HTTP Applications using HTTP requests.
'''
class text_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def create_log_error(_file, _application, _exception):
    logFileLocation = f"./logs/{date.today()}/{_file}.gossip"

    if os.path.isdir(f"logs/{str(date.today())}") == False:
        os.makedirs(f"logs/{str(date.today())}")

    if os.path.isfile(logFileLocation) == False:
        open(logFileLocation, "a").close

    if os.path.isfile(logFileLocation) == True:
        f = open(logFileLocation, 'a')
        f.write(
            f"\n[GOSSIP][{datetime.datetime.now()}] {_application} {_exception}")
        f.close()


def verifyFrontend(_application):
    print(emoji.emojize(f"{text_colors.BOLD}[FRONTEND] {text_colors.ENDC}{_application['url']} - Verificando :high_voltage:"), end='\r')
    try:
        request = requests.head(_application['url'], timeout=5)
        if request.status_code == 200:
            print(emoji.emojize(f"{text_colors.BOLD}[FRONTEND] {text_colors.ENDC}{text_colors.OKGREEN}{_application['url']} - SERVIÇO ONLINE :check_mark_button:{text_colors.ENDC}"))
        else:
            print(emoji.emojize(f"{text_colors.BOLD}[FRONTEND] {text_colors.ENDC}{text_colors.FAIL}{_application['url']} - SERVIÇO INDISPONÍVEL :police_car_light:{text_colors.ENDC}"))
            create_log_error(
                _application['logFile'], _application['url'], f"status_code: {request.status_code}")
    except Exception as e:
        print(emoji.emojize(f"{text_colors.BOLD}[FRONTEND] {text_colors.ENDC}{text_colors.FAIL}{_application['url']} - SERVIÇO INDISPONÍVEL :police_car_light:{text_colors.ENDC}"))
        create_log_error(_application['logFile'], _application['url'], e)


def verifyBackend(_application):
    print(emoji.emojize(f"{text_colors.BOLD}[BACKEND] {text_colors.ENDC}{_application['url']} - Verificando :high_voltage:"), end='\r')
    try:
        request = requests.head(_application['url'], timeout=5)
        if request.status_code == 200:
            print(emoji.emojize(f"{text_colors.BOLD}[BACKEND] {text_colors.ENDC}{text_colors.OKGREEN}{_application['url']} - SERVIÇO ONLINE :check_mark_button:{text_colors.ENDC}"))
        else:
            print(emoji.emojize(f"{text_colors.BOLD}[BACKEND] {text_colors.ENDC}{text_colors.FAIL}{_application['url']} - SERVIÇO INDISPONÍVEL :police_car_light:{text_colors.ENDC}"))
            create_log_error(_application['logFile'], _application['url'], f"status_code: {request.status_code}")
    except Exception as e:
        print(emoji.emojize(f"{text_colors.BOLD}[BACKEND] {text_colors.ENDC}{text_colors.FAIL}{_application['url']} - SERVIÇO INDISPONÍVEL :police_car_light:{text_colors.ENDC}"))
        create_log_error(_application['logFile'], _application['url'], e)


def main():
    os.system('cls||clear')
    config = []
    print('''\n
         ██████╗  ██████╗ ███████╗███████╗██╗██████╗ 
        ██╔════╝ ██╔═══██╗██╔════╝██╔════╝██║██╔══██╗
        ██║  ███╗██║   ██║███████╗███████╗██║██████╔╝
        ██║   ██║██║   ██║╚════██║╚════██║██║██╔═══╝ 
        ╚██████╔╝╚██████╔╝███████║███████║██║██║     
        ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  SERVICE MONITOR
    ''')
    print(f"Data e Hora: {datetime.datetime.now()}")
    # print("Carregando arquivo de configuração...")
    try:
        openConfigBlob = open('config.json')
        config = json.load(openConfigBlob)
    except Exception:
        print("Nao foi encontrado o arquivo de configuracao.")
        print("Por favor visite nosso link: https://gossip.ctrl-alt-delete.com.br")
        exit()

    for project in config:
        print(f"\n{text_colors.BOLD}{text_colors.HEADER}{project['name']}{text_colors.ENDC}")
        for application_frontend in project['frontend']:
            verifyFrontend(application_frontend)
        for application_backend in project['backend']:
            verifyBackend(application_backend)


while True:
    main()
    time.sleep(10)
