import requests
import datetime
import os

day = datetime.datetime.now().day
path = "../Day{}".format(day)

# Make current days directory
if not os.path.exists(path):
    os.makedirs(path)

# Make current days files
filename = "main.py"
with open(os.path.join(path, filename), 'w') as temp_file:
    temp_file.write("# Day{}".format(day))

filename = "input.txt"
with open(os.path.join(path, filename), 'wb') as temp_file:
    url = "https://adventofcode.com/2020/day/{}/input".format(day)
    cookies = \
        dict(session='53616c7465645f5fd2305a19ffa2a8ba991b74791742e313ce6578118be46b9e531b3a0aca1c47c580802081853bdba5')
    response = requests.get(url, cookies=cookies)
    temp_file.write(response.content)


