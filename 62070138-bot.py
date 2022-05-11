import requests
import json
import time
access_token = 'NmM1NTg5MjUtZWYzMS00MTQzLWFkN2QtMDEzOGYyMjkxMjAzMTRmNzUzMDgtMzdj_P0A1_008987e2-e168-4a36-b708-98b3f31e9588'
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl"
room_id_test = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vODMxODQ2NTAtY2RkZi0xMWVjLTk4YTgtMWQwNWU3MzAwZDNh"
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
            checking_status(0)

def send_message_up(status):
    message = 'Loopback62070138 - Operational status is up'
    message2 = 'Enable Loopback62070138 - Now the Operational status is up again'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    param = {'roomId': room_id, 'markdown': message2}
    if status == 0:
        res = requests.post(url, headers=headers, json=params)
    elif status == 1:
        res = requests.post(url, headers=headers, json=param)

def send_message_down(status):
    message = 'Loopback62070138 - Operational status is down'
    message2 = 'Enable Loopback62070138 - Now the Operational status is up again'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    param = {'roomId': room_id, 'markdown': message2}
    if status == 0:
        res = requests.post(url, headers=headers, json=params)
        enable_interface()
    elif status == 1:
        res = requests.post(url, headers=headers, json=param)
        get_message()

def checking_status(status):
    headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
    basicauth = ("admin", "cisco")
    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False).json()
    if status == 0:
        if resp['ietf-interfaces:interface']['enabled'] == True:
            send_message_up(status)
        elif resp['ietf-interfaces:interface']['enabled'] == False:
            send_message_down(status)
    elif status == 1:
        if resp['ietf-interfaces:interface']['enabled'] == True:
            send_message_up(status)
        elif resp['ietf-interfaces:interface']['enabled'] == False:
            send_message_down(status)
def enable_interface():
    headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
    basicauth = ("admin", "cisco")
    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False).json()
    resp['ietf-interfaces:interface']['enabled'] = True
    respo = requests.put(api_url, auth=basicauth, headers=headers, json=resp, verify=False)
    checking_status(1)


get_message()
