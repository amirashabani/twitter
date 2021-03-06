from matplotlib import pyplot as plt
import pandas as pd
import json

with open("tweet.js", 'r') as f:
	text = f.read().split('=', 1)[1].lstrip()

data = json.loads(text)

tweets, retweets, mentions = [0] * 3
for tweet in data:
	if "in_reply_to_user_id" in tweet["tweet"]:
		mentions += 1
	else:
		if tweet["tweet"]["full_text"][:2] == "RT":
			retweets += 1
		else:
			tweets += 1

names = [
    f"Tweets ({tweets})",
    f"Retweets ({retweets})",
    f"Mentions ({mentions})"
]
counts = [tweets, retweets, mentions]

plt.rcParams["font.family"] = "mononoki"
fig, ax = plt.subplots()
ax.pie(
    counts,
    labels=names,
    autopct="%1.2f%%",
    wedgeprops={
        "edgecolor": 'k',
        "linewidth": 1,
        "linestyle": "solid",
        "antialiased": True
    }
)
ax.set_title("Ratio of Tweets, Retweets, and Mentions")

fig.set_facecolor("grey")
fig.tight_layout()
fig.savefig("pie.png", dpi=200)
