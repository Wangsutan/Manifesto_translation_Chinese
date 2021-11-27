#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 09:12:51 2021

@author: wst
"""
import regex as re


# about texts.
path = '/home/wst/Desktop/Manifesto研究材料/原文/manifestTxt/'
fileNames = ['1_bourprol']
for fileName in fileNames:
    textFilename = path + fileName + '_text.txt'
    with open(textFilename, 'r') as f:
        text = f.read()
        # print(text)
        
pattern = re.compile(r'\[(\d+)\]')
findNotes = pattern.findall(text)
print("The number of notes:", len(findNotes), findNotes)

# about notes.
for fileName in fileNames:
    noteFilename = path + fileName + '_note.txt'
    with open(noteFilename, 'r') as f:
        note = f.read()
        # print(note)

# prepare the list of numbers of notes
numPatterns = []
for num in findNotes:
    numPatterns.append(r"\[%s\]" % num)
# print("numPatterns:", numPatterns)

# prepare the list of contents of notes
notesList = []
findNotePattern = r'^[\d+\.].*'
notesList = re.findall(findNotePattern, note, re.M)    # re.M，指多行
print(notesList)

# add special marks to notes
newNotes = []
for note in notesList:
    newNotes.append(r"\\footnote{%s}" % note)    # \f，当心换页

# substitute new notes for the old note numbers.
for i in range(len(numPatterns)):
    text = re.sub(numPatterns[i], str(newNotes[i]), text)

# print(text)
with open("text_note.txt", 'w') as f:
    f.write(text)
    