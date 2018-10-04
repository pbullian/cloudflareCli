# cloudflareCli

## setup

`pip install requirements.txt`

## usage

you can set into the environment the api key and email

`export CLOUDFLARE_EMAIL="xxxxx@xxxxx.xxx"`
`export CLOUDFLARE_KEY="xxxxxxxxxx"`

or run it as a one liner
python cloudflare.py -u "xxxxxxx" -k "xxxxxx" -p "zonename" [action]

`python cloudflare.py -u "foo@bar.com" -k "xxxxxx" -p "domain.com" clear-cache`

## man

usage: cloudflare.py [-h][-p project] [-u USER][-k key] {clear-cache}

cloudflare cli

positional arguments:
{clear-cache} ACTION what to do

optional arguments:
-h, --help show this help message and exit
-p PROJECT, --project PROJECT
-u USER, --user USER
-k KEY, --key KEY

## TO DO

only supports clear-cache right now
