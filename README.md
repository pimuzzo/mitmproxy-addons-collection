# mitmproxy-addons-collection
A personal collection of [mitmproxy](https://github.com/mitmproxy/mitmproxy) addons

### Create a virtual environment

`virtualenv --python=/usr/bin/python3 venv`

## Always

### Activate the virtual environment

`source venv/bin/activate`

### Install dependencies

`pip install -r requirements.txt`

### Run

`mitmproxy -s addon_name.py`

## Useful in development

### Update requirements

`pip freeze > requirements.txt`


