import requests
import json
import time
access_token = 'ZGMwNGY0YWUtMWJiYi00ZjNjLTg1M2ItYzQxMWRhMDYwZjliOWI5YTkxNmItODcx_P0A1_008987e2-e168-4a36-b708-98b3f31e9588'
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl"
requests.packages.urllib3.disable_warnings()
api_url = "https://10.0.15.107/restconf/data/ietf-interfaces:interfaces/interface=Loopback62070138"
url = 'https://webexapis.com/v1/messages'

def get_message():
    while True:
        time.sleep(1)
        headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'max': 1}
        res = requests.get(url, headers=headers, params=params).json()
        if res['items'][0]['text'] == '62070138':
            checking_status()

def send_message_up():
    message = 'Loopback62070138 - Operational status is up'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)

def send_message_down():
    message = 'Loopback62070138 - Operational status is down'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)

def checking_status():
    headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
    basicauth = ("admin", "cisco")
    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False).json()
    if resp['ietf-interfaces:interface']['enabled'] == True:
        send_message_up()
    elif resp['ietf-interfaces:interface']['enabled'] == False:
        send_message_down()

get_message()
