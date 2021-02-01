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

class_to_compare = 'family'
temp_df = df_pre_lockdown[[class_to_compare]]
temp_df2 = df_in_lockdown[[class_to_compare]]

# fig, ax = plt.subplots()

# ax.boxplot(temp_df[temp_df[class_to_compare] != 0])
# ax.set_xlabel('Posts')
# ax.set_ylabel(f'Score of {class_to_compare}')
# ax.set_title(f'Scores prelockdown for {class_to_compare}')
# ax.axhline(y=0, lw=0.5, color='k')

fig, ax = plt.subplots(1, 2, sharey=True)

ax[0].boxplot(temp_df[temp_df[class_to_compare] != 0])
ax[0].set_xlabel('Posts')
ax[0].set_ylabel(f'Score of {class_to_compare}')
ax[0].set_title(f'Scores prelockdown for {class_to_compare}')

ax[1].boxplot(temp_df2[temp_df2[class_to_compare] != 0])
ax[1].set_xlabel('Posts')
ax[1].set_ylabel(f'Score of {class_to_compare}')
ax[1].set_title(f'Scores inlockdown for {class_to_compare}')

ax[0].axhline(y=0, lw=0.5, color='k')
ax[1].axhline(y=0, lw=0.5, color='k')

fig.tight_layout()
plt.show()

