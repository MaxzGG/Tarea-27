#Maximiliano Gómez Guevara
#2177546
import six
import sys
import requests
import getpass
import argparse
import logging

if not six.PY3:
    raise Exception("Este script requiere ser ejecutado con Python 3.")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api_key = getpass.getpass(prompt="Por favor, introduzca su API key: ")

def get_arguments():
    parser = argparse.ArgumentParser(description="Verifica si una cuenta de correo electrónico ha sido comprometida.")
    parser.add_argument('-e', '--email', type=str, required=True, help="Correo electrónico a verificar")
    return parser.parse_args()

def check_breach(email, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-apikey": api_key,
        "User-Agent": "Python script"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        breaches = response.json()

        if breaches:
            logger.info(f"La cuenta {email} ha sido comprometida en los siguientes sitios:")
            for breach in breaches:
                logger.info(f"Sitio: {breach['Name']}")
        else:
            logger.info(f"La cuenta {email} no ha sido comprometida.")
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            logger.info(f"La cuenta {email} no ha sido comprometida.")
        else:
            logger.error(f"Error al obtener los datos: {err}")
    except Exception as e:
        logger.error(f"Ha ocurrido un error: {e}")

def main():
    args = get_arguments()
    email = args.email
    logger.info(f"Verificando la cuenta de correo electrónico: {email}")
    check_breach(email, api_key)

if __name__ == '__main__':
    main()