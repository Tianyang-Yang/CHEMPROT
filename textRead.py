#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:46:45 2017

@author: yty
"""

import csv 
import os
import numpy as np
import pandas as pd
import re


textpath = os.path.dirname(os.getcwd())+'/biocreative/chemprot_training/chemprot_training/'

abstractpath = textpath+'chemprot_training_abstracts.tsv'
entitypath = textpath+'chemprot_training_entities.tsv'
relationpath = textpath+'chemprot_training_relations.tsv'

column1 = ['ID','title','abstract']
column2 = ['ID','T','type','p1','p2','entity']
column3 = ['ID','group','eval','relation','arg1','arg2']

" first read the abstract file:  chemprot_training_abstracts.tsv "
allabstract = []
with open(abstractpath,'r', encoding='utf-8') as abstractfile:
    templines = abstractfile.readlines()
    for line in templines:
        newline = line.split('\t')
        newline[2] = re.sub(r'\n'," ",newline[2])
        newdict = dict(zip(column1,newline))
        allabstract.append(newdict)
        

" get every pair of the entities from:    chemprot_training_entities.py"
"                                         chemprot_training_relations.py"
allentity = []
allrelation = []

with open(entitypath,'r',encoding='utf-8') as entityfile:
    templines = entityfile.readlines()
    for line in templines:
        newline = line.split('\t')
        newline[5] = newline[5].strip('\n')
        newline[3] = int(newline[3])
        newline[4] = int(newline[4])
        newdict = dict(zip(column2,newline))
        allentity.append(newdict)
        
with open(relationpath,'r',encoding='utf-8') as relationfile:
    templines = relationfile.readlines()
    for line in templines:
        newline = line.split('\t')
        newline[5] = newline[5].strip('\n')
        newline[4] = newline[4][6:]
        newline[4] = int(newline[4])
        newline[5] = newline[5][6:]
        newline[5] = int(newline[5])
        newdict = dict(zip(column3,newline))
        allrelation.append(newdict)

"""
def form(filepath,column,i):
    table = []
    with open(filepath,'r',encoding='utf-8') as file:
        templines = file.readlines()
        for line in templines:
            newline = line.split('\t')
            if i==1:
                newline[2] = re.sub(r'\n'," ",newline[2])
                newdict = dict(zip(column,newline))
                table.append(newdict)
            if i==2:
                newline[5] = newline[5].strip('\n')
                newdict = dict(zip(column,newline))
                table.append(newdict)
            if i==3:
                newline[5] = newline[5].strip('\n')
                newdict = dict(zip(column,newline))
                table.append(newdict)
    return newdict

allabstract = form(abstractpath,column1,1)
allentity = form(entitypath,column2,2)
allrelation = form(relationpath,column3,3)
"""            
                
                
                
                
#to get the entity in abstract, use the matching function of regular expression
#or use the information of location by slicing
#given a pair of entities, using the [abstract ID] and [Arg ID] to pinpoint the 
#two entities. In fact we can use no information of the very names of entities.

#abstractframe = pd.Dataframe(allabstract)

abstracttable = pd.DataFrame(allabstract,columns=column1)
entitytable = pd.DataFrame(allentity,columns=column2)
relationtable = pd.DataFrame(allrelation,columns=column3)
"""
for relation in relationtable.iterrows():
    index = relation.ID
    arg1 = relation.arg1.strip('Arg1:')
    arg2 = relation.arg2.strip('Arg2:')
    abstract = abstracttable[abstracttable.ID==idex].abstract
    entity1 = entitytable[(entitytable.ID==index) & (entitytable.T = arg1)].entity
    entity2 = entitytable[(entitytable.ID==index) & (entitytable.T = arg2)].entity
    pair = [entity1,entity2]
"""

def rela2text(reladict,allentity,allabstract):
    ID = reladict['ID']
    arg1 = reladict['arg1']
    arg2 = reladict['arg2']
    










