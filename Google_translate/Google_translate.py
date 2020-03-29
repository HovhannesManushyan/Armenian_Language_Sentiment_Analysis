# -*- coding: utf-8 -*-
import os
from googletrans import Translator
import time

i=0
for cur_name in os.listdir("train/pos"):
    checker = ""
    with open("train/pos/"+cur_name,"r",encoding="utf-8") as file:
        checker = file.read()
    if(i==50):
        i=0
        time.sleep(50)
    i+=1
    translator = Translator()
    zx = translator.translate(checker,dest="hy").text
    with open("output.txt","a",encoding = "utf-8") as file:
        file.write(zx + '\n')

