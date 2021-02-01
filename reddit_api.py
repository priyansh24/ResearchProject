import requests
import json

data = []


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

next_hundred = None

subreddit_param = 'depression'
q_param = 'india'
after_param = ''

sno = 0

for i in range(10):
    res = requests.get(
        f'https://www.reddit.com/r/{subreddit_param}/search.json?q={q_param}&restrict_sr=on&limit=100&after={after_param}&sort=new', headers=headers)

    next_hundred = json.loads(res.text)  # dictionary

    print('Req', i+1, ':\t', next_hundred['data']['dist'])

    if len(next_hundred['data']['children']) < 1:
        break

    for child in next_hundred['data']['children']:

        data.append({
            'sno' : sno,
            'created': child['data']['created'],
            'author': child['data']['author'],
            'title': child['data']['title'].replace('\n', ''),
            'selftext': child['data']['selftext'].replace('\n', ''),
            'is_suicide': 0
        })

        sno+=1
        after_param = child['data']['name']

f = open(
    f'reddit_{subreddit_param}_{q_param}_{len(data)}_posts.json', 'w', newline='')
f.write(json.dumps(data, ensure_ascii=False))
f.close()

print("No. of posts : ", len(data))
print("Done Dona Done!!😎")
