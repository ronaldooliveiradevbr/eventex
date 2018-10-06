# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/rfdeoliveira/eventex.svg?branch=master)](https://travis-ci.org/rfdeoliveira/eventex)
[![codebeat badge](https://codebeat.co/badges/f0127aef-b2e0-4d4d-b3e8-fab3a506b98b)](https://codebeat.co/projects/github-com-rfdeoliveira-eventex-master)
[![CodeFactor](https://www.codefactor.io/repository/github/rfdeoliveira/eventex/badge)](https://www.codefactor.io/repository/github/rfdeoliveira/eventex)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/73b9866368fa4e77961f7604cd3436f2)](https://www.codacy.com/app/rfdeoliveira/eventex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rfdeoliveira/eventex&amp;utm_campaign=Badge_Grade)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. atualizar virtualenv.
5. Instale as dependências.
6. Configure a instância com o .env
7. Execute os testes.

```console
git clone git@github.com:rfdeoliveira/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install pip --upgrade 
pip install setuptools --upgrade
pip install wheel
pip install -r requirements-dev.txt
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
