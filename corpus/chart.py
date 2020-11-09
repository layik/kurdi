import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import re

plt.style.use("ggplot")

all_freq = {}
with open("kurdi_words.txt", "r", encoding="utf-8") as kw, open(
    "letters_lines.txt", "r", encoding="utf-8"
) as chars:
    uu_pat = re.compile(r"وو")
    for ch in chars:
        for word in kw:
            new_word = re.sub(uu_pat, r"u", word)
            for c in new_word:
                if c != "\n":
                    if c in all_freq:
                        all_freq[c] += 1
                    else:
                        all_freq[c] = 1

all_freq["وو"] = all_freq["u"]
del all_freq["u"]

# Sorting dictionary file as per the frequency
all_freq = dict(sorted(all_freq.items(), key=lambda s: s[1], reverse=True))
print(all_freq)

x = list(all_freq.keys())
y = list(all_freq.values())


# make the figure size = (wisth, height)
plt.figure(figsize=(20, 15))

# bar plot for X and Y
plt.bar(x, y)

for i in range(len(x)):
    # print(x[i], y[i])
    plt.text(
        x=x[i],
        y=y[i],
        s="  " + str(y[i]),
        # size=6,
        ha="center",
        rotation=90,
        fontname="Source Code Pro",
        color="k",
    )

plt.xticks(ticks=x, fontfamily="Vazir", weight="bold")
plt.yticks(np.arange(0, 3000000, 300000))
plt.ticklabel_format(style="plain", axis="y")

# Title of the chart
title_font = {
    "family": "Source Code Pro",
    "color": "#232323",
    "weight": "bold",
    "size": 16,
}
plt.title("Character Frequency Bar Chart\n", fontdict=title_font)

# Lable for X axis
lable_x_font = {
    "family": "Source Code Pro",
    "color": "#232323",
    "weight": "bold",
    "size": 13,
}
plt.xlabel("\nCharacter", fontdict=lable_x_font)

# Lable for Y axis
lable_y_font = {
    "family": "Source Code Pro",
    "color": "#232323",
    "weight": "bold",
    "size": 13,
}
plt.ylabel("Frequency\n", fontdict=lable_y_font)

# make a grid for the chart
# plt.grid(True)
# plt.grid(axis="y", linestyle="-")

# save the char bar as a PDF file
# plt.savefig("graph.pdf")
# plt.savefig("graph.png")
plt.show()
