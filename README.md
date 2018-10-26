# Eventex

Event System commissioned by Morena.

[![Build Status](https://travis-ci.org/rfdeoliveira/eventex.svg?branch=master)](https://travis-ci.org/rfdeoliveira/eventex)
[![codebeat badge](https://codebeat.co/badges/f0127aef-b2e0-4d4d-b3e8-fab3a506b98b)](https://codebeat.co/projects/github-com-rfdeoliveira-eventex-master)
[![CodeFactor](https://www.codefactor.io/repository/github/rfdeoliveira/eventex/badge)](https://www.codefactor.io/repository/github/rfdeoliveira/eventex)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/73b9866368fa4e77961f7604cd3436f2)](https://www.codacy.com/app/rfdeoliveira/eventex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rfdeoliveira/eventex&amp;utm_campaign=Badge_Grade)

## How to develop?

1. Clone the repository.
2. Create a virtualenv with Python 3.6
3. Activate virtualenv.
4. Install the dependencies.
5. Configure the instance with .env
6. Run the tests.

```console
git clone git@github.com:rfdeoliveira/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## How to deploy?

1. Create an instance in heroku
2. Send settings to heroku
3. Set a secure SECRET_KEY for the instance
4. Set `DEBUG = FALSE`
5. Configure the e-mail service.
6. Send the code to heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure o email
git push heroku master --force
```
