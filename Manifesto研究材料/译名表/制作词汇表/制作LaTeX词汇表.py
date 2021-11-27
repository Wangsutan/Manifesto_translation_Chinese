#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 09:36:57 2021

@author: wst
"""

import re


fileName = '待用已整理词汇表.txt'
with open(fileName, 'r') as f:
    text = f.read()

# ('Wissenschaft', 4),科学界；科学

patternOrig = r"'(\w*)',"
wordOrig = re.findall(patternOrig, text)
print(wordOrig)

patternTrans = r"\),(.*)\n"
wordTrans = re.findall(patternTrans, text)
print(wordTrans)

wordList = ''
# \nomenclature{Abschaffung}{废除}%
for i in range(len(wordOrig)):
    wordList += "\\nomenclature{" + wordOrig[i] + "}{" + wordTrans[i] + "}%\n"
print(wordList)

with open('TeXWordList.txt', 'w') as f:
    f.write(wordList)
print("WORD LIST DONE!")
