no = []
with open("No_sentence.txt", "r", encoding="utf-8") as f:
    for i in f:
        no.append(i)
with_sentence = []
with open("kurdi_words.txt", "r", encoding="utf-8") as f:
    for i in f:
        if i in no:
            pass
        else:
            with_sentence.append(i)
with_sentence.sort()
for i in with_sentence:
    with open("with_sentence.txt", "a", encoding="utf-8") as f:
        f.write(i)
