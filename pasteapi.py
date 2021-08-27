import re
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['show', 'file', 'paste'])
parser.add_argument('input')
args = parser.parse_args()

user_input = args.input
dev_key = 'f6ade61387a928553d5ad87814931857'
user_key = '273a606bd17c017c932123cf12be1ad0'
api_url = 'https://pastebin.com/api/api_post.php'

# Paste from command line:
if args.mode == 'paste': 
    api_data = {'api_dev_key': dev_key, 'api_option': 'paste', 'api_paste_code': user_input}
    req = requests.post(api_url, api_data)
    print(req.text.replace('pastebin.com', 'pastebin.com/raw'))

# Open a paste url:
elif args.mode == 'show':
    if re.search(r'^(https?:\/\/)?pastebin.com\/(\w{8})', user_input) == None:
        print("Not a pastebin url")
    elif 'raw' not in user_input:
        user_input = user_input.replace('pastebin.com', 'pastebin.com/raw')
        req = requests.get(user_input)
        print(req.text)

# Upload content of a file
else:
    with open(args.input, 'r', encoding = 'utf-8') as file:
        data = file.read()

    api_data = {'api_dev_key': dev_key, 'api_option': 'paste', 'api_paste_code': data}
    req = requests.post(api_url, api_data)
    print(req.text.replace('pastebin.com', 'pastebin.com/raw'))