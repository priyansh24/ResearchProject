import json
import datetime

input_file_name = "reddit_depression_india_236_posts.json"
f = open(input_file_name, 'r', newline='', encoding="utf8")

data = json.load(f)

march_23_2020_epoch = datetime.datetime(2020,3,23,0,0,0).timestamp()

threshold_index = 0
for i, post in enumerate(data):
    if post["created"] < march_23_2020_epoch:
        threshold_index = i
        break

# print(march_23_2020_epoch)

data_in_lockdown = data[:threshold_index]
data_pre_lockdown = data[threshold_index:]

f_in_lockdown = open(f"in_lockdown_{len(data_in_lockdown)}.json", 'w')
f_pre_lockdown = open(f"pre_lockdown_{len(data_pre_lockdown)}.json", 'w')

json.dump(data_in_lockdown, f_in_lockdown, ensure_ascii=False)
json.dump(data_pre_lockdown, f_pre_lockdown, ensure_ascii=False)

f_in_lockdown.close()
f_pre_lockdown.close()
f.close()

print('Dona done done😎')