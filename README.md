# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/rfdeoliveira/eventex.svg?branch=master)](https://travis-ci.org/rfdeoliveira/eventex)
[![codebeat badge](https://codebeat.co/badges/f0127aef-b2e0-4d4d-b3e8-fab3a506b98b)](https://codebeat.co/projects/github-com-rfdeoliveira-eventex-master)
[![CodeFactor](https://www.codefactor.io/repository/github/rfdeoliveira/eventex/badge)](https://www.codefactor.io/repository/github/rfdeoliveira/eventex)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:rfdeoliveira/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina `DEBUG=FALSE`
5. Configure o serviço de email.
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure o email
git push heroku master --force
```
