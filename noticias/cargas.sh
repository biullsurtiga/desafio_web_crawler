#!/bin/bash

echo -e  $(date +"%d-%m-%Y %H:%M:%S") " Iniciando execução de script"

echo -e  $(date +"%d-%m-%Y %H:%M:%S") " Executando carga do Tecnoblog"
#Tecnoblog
scrapy runspider noticias/spiders/Tecnoblog.py

echo -e  $(date +"%d-%m-%Y %H:%M:%S") " Executando carga do Canaltech"
#Canaltech
scrapy runspider noticias/spiders/Canaltech.py

echo -e  $(date +"%d-%m-%Y %H:%M:%S") " Finalizando execução de script"
