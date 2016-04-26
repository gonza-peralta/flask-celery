'''
Created on Apr 26, 2016

@author: gonzalo
'''
from celerytask.tasks import changename
import time
import random

if __name__ == '__main__':
    for i in range(1000):
        seconds = random.random() / 2.0
        print seconds
        time.sleep(seconds)
        changename.delay()
