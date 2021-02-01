from os import write
from bs4 import BeautifulSoup
import requests

import csv

url = 'https://www.reddit.com/search/?q=subreddit%3Adepression%20india'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'lxml')

posts = soup.find('div', class_='rpBJOHq2PR60pnwJlUyP0')

f = open('data.csv', 'w')
writer = csv.writer(f)

writer.writerow(['title', 'vote', 'num_comments', 'posted_before'])

for post in posts:
    title = post.find('h3', class_='_eYtD2XCVieq6emjKBH3m').span.text
    vote = post.find('div', class_='_1rZYMD_4xY3gRcSS3p8ODO').text
    ncomments = post.find(
        'span', class_='FHCV02u6Cp2zYL0fhQPsO').text.split()[0]
    posted_before = post.find('a', class_='_3jOxDPIQ0KaOWpzvSQo-1s').text

    row = [title, vote, ncomments, posted_before]
    writer.writerow(row)


f.close()
