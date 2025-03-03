#!/bin/bash
# Script de implantação automática

cd /caminho/para/aplicacao

echo "Atualizando código..."
git pull origin master

echo "Reconstruindo containers..."
docker-compose down
docker-compose build
docker-compose up -d

echo "Verificando status..."
docker-compose ps

echo "Implantação concluída!" 