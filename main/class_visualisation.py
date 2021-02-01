import pandas as pd
import numpy as np
from os import path
import matplotlib.pyplot as plt


f_score_in_lockdown = open(path.join(
    'score', f"score_in_lockdown_116.json"), 'r', newline='', encoding='utf8')
f_score_pre_lockdown = open(path.join(
    'score', f"score_pre_lockdown_120.json"), 'r', newline='', encoding='utf8')


df_pre_lockdown = pd.read_json(f_score_pre_lockdown).iloc[::-1]
df_in_lockdown = pd.read_json(f_score_in_lockdown).iloc[::-1]

class_to_compare = 'friends'

np.arange(df_pre_lockdown.shape[0])

fig, ax = plt.subplots(1, 2, sharey=True)

ax[0].scatter(np.arange(df_pre_lockdown.shape[0]), df_pre_lockdown[[class_to_compare]])
ax[0].set_xlabel('Posts')
ax[0].set_ylabel(f'Score of {class_to_compare}')
ax[0].set_title(f'Scores prelockdown for {class_to_compare}')

ax[1].scatter(np.arange(df_in_lockdown.shape[0]), df_in_lockdown[[class_to_compare]], c='red')
ax[1].set_xlabel('Posts')
ax[1].set_ylabel(f'Score of {class_to_compare}')
ax[1].set_title(f'Scores inlockdown for {class_to_compare}')

ax[0].axhline(y=0, lw=0.5, color='k')
ax[1].axhline(y=0, lw=0.5, color='k')

fig.tight_layout()
plt.show()

# print(label)
# labels = df_in_lockdown.columns.values.tolist()
# x = np.arange(len(labels))
# width = 0.35

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, df_in_lockdown.mean(), width, label='In Lockdown')
# rects2 = ax.bar(x + width/2, df_pre_lockdown.mean(), width, label='Pre Lockdown')

# plt.axhline(y=0, lw=0.5, color='k')

# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = round(rect.get_height(), 4)
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height if height > 0 else height-0.008),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')

# autolabel(rects1)
# autolabel(rects2)

# fig.tight_layout()
# plt.show()
