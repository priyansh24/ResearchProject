from research_iet import process_all_posts, save_to_file
from os import path
import json

# processing posts
input_file_name = 'pre_lockdown_120.json'
json_file = open(path.join('data', input_file_name),
                 'r', newline='', encoding="utf8")
all_posts = json.load(json_file)
all_sentiments = process_all_posts(all_posts)
save_to_file(path.join('score', f'score_{input_file_name}'), all_sentiments)
print('Scores calculated successfully 🙏')