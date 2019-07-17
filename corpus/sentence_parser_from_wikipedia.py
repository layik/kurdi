#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wikipedia


wikipedia.set_lang("ckb")
with open('kurdi_words.txt', 'r', encoding='utf-8') as f:
    for i in f:
        with open('kurdi_sentence.txt', 'a', encoding='utf-8') as new_f:
            try:
                print(i)
                new_f.write(wikipedia.summary(i, sentences=1))
                new_f.write('\n')
            except:
                 with open('No_sentence.txt', 'a', encoding='utf-8') as new_file:
                     new_file.write(i)
                     new_f.write('\n')
                     
