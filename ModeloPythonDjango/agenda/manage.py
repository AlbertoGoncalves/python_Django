#!/usr/bin/env python

"""
Agora vamos criar tabelas padroes
comanda: python manage.py migrate
Configuracao do banco esta dentro do arquivo settings.py DATABASES

url para acesso ao ADMIM
http://127.0.0.1:8000/admin/

criando SuperADMIN
comando: python manage.py createsuperuser --username admin
Vai pedir um e-mail
depois vai pedir uma senha */
"""

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
