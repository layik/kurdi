#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from kurdish import ku
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# main_word = "بەرد"
with open("kurdi_words.txt", "r", encoding="utf-8") as f:
    for each_word in f.read().split():
        main_word = each_word
        

        wiki_url = "https://ckb.wikipedia.org/wiki/" + main_word
        # print(wiki_url)
        url = requests.get(wiki_url).text
        soup = BeautifulSoup(url, "lxml")
        sentence = []
        for main in soup.find_all("div", "mw-parser-output"):
            for para in main.find_all("p"):
                if main_word in para.text:
                    sentence.append(para.text)
        try:
            sentence = sentence[0]
            one_sent = []
            for i in sentence.split("\n"):
                one_sent.append("".join(i))
            
            for i in one_sent:
                with open("sent.txt", "a", encoding="utf-8") as f:
                    print(main_word)
                    f.write(i + "\n")
        except:
            pass
