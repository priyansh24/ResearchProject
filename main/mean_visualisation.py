import pandas as pd
import numpy as np
from os import path
import matplotlib.pyplot as plt


f_score_in_lockdown = open(path.join(
    'score', f"score_in_lockdown_116.json"), 'r', newline='', encoding='utf8')
f_score_pre_lockdown = open(path.join(
    'score', f"score_pre_lockdown_120.json"), 'r', newline='', encoding='utf8')


df_in_lockdown = pd.read_json(f_score_in_lockdown)
df_pre_lockdown = pd.read_json(f_score_pre_lockdown)

print(df_in_lockdown)

labels = df_in_lockdown.columns.values.tolist()
x = np.arange(len(labels))  
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, df_in_lockdown.mean(), width, label='In Lockdown')
rects2 = ax.bar(x + width/2, df_pre_lockdown.mean(), width, label='Pre Lockdown')

ax.set_xlabel('Classes')
ax.set_ylabel('Scores')
ax.set_title('Scores prelockdown and inlockdown')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.axhline(y=0, lw=0.5, color='k')

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = round(rect.get_height(), 4)
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height if height > 0 else height-0.008),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()
