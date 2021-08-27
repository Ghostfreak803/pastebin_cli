import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['show', 'paste'])
parser.add_argument('input')
args = parser.parse_args()

user_input = args.input
dev_key = 'f6ade61387a928553d5ad87814931857'
user_key = '273a606bd17c017c932123cf12be1ad0'

if args.mode == 'show':
    req = requests.get(user_input)
    print(req.text)

else:
    api_url = 'https://pastebin.com/api/api_post.php'

    with open(args.input, 'r', encoding = 'utf-8') as file:
        data = file.read()

    api_data = {'api_dev_key': dev_key, 'api_option': 'paste', 'api_paste_code': data}
    req = requests.post(api_url, api_data)
    print(req.text)