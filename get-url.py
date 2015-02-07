#!/usr/bin/env python
import urllib
import random

base_url = 'http://en.wikipedia.org/wiki/'

with open('list.txt', 'r') as f:
    states = f.read().split('\n')

state = random.choice(states)
url = base_url + urllib.quote(state.replace(' ', '_'))

print url
