# Especificar a imagem base
From node:alpine

WORKDIR /usr/app
# Instalar as dependencias

COPY ./package.json ./
RUN npm install
#Copia todos os arquivos pro container
COPY ./ ./ 

#Comando padrão
CMD ["npm","start"]