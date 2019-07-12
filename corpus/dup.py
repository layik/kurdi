with open("kurdi_list_UP.txt", "r", encoding="utf-8") as f:
    new = []
    for i in f:
        if not i in new:
            new.append(i)
        else:
            pass
new.sort()
for i in new:
    with open("newlist_without_dup_01.txt", "a", encoding="utf-8") as f:
        f.write(i)
