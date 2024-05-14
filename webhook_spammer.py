import requests
import threading
import time

delay = 1
threads = 3
webhook = ''

def spam():
    while True:
        headers = {
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
        }
        
        json_data = {
            'content': 'message', #edit this to change the message
            'username': 'username', #edit this to change the username
        }
        
        response = requests.post(
            webhook,
            headers=headers,
            json=json_data,
        )
       
        response
        time.sleep(delay)
        continue

def main():
    for n in range(threads+1):
        t = threading.Thread(target=spam)
        t.start()

main()
