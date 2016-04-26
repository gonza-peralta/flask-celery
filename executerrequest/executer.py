'''
Created on Apr 26, 2016

@author: gonzalo
'''
import requests
from requests.exceptions import HTTPError
HEADERS = {"Accept": "application/json",
           "Content-Type": "application/json"}
import time
import random

if __name__ == '__main__':
    for i in range(1000):
        seconds = random.random()
        print seconds
        time.sleep(seconds)
        try:
            request = requests.put('http://127.0.0.1:5000/user',
                                   headers=HEADERS)
        except HTTPError as exc:
            print exc
