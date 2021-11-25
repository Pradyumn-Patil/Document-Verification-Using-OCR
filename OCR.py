# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 04:48:56 2021

@author: prady
"""

import cv2
import cvlib as cv
import sys
import numpy as np

import pandas as pd 
import glob
import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image
 
import matplotlib.pyplot as plt

 # run pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




candidate_list = pd.read_excel("Data.xlsx")
cand_list = candidate_list[['ApplicationID', 'Name', 'Catergory', 'Caste', 'Caste Number','path']]
print(list(candidate_list.columns))
errorlist = [] 

for ind in cand_list.index:
    name = cand_list['Name'][ind]
    keys = name.split(' ')
    keys.append('other backward')
    keys.append(cand_list['Caste'][ind])
    keys.append(str(cand_list['Caste Number'][ind]))
    
    
    image_path_in_colab=cand_list['path'][ind]
    im = cv2.imread(image_path_in_colab, cv2.IMREAD_COLOR)

    extract = pytesseract.image_to_string(Image.open(image_path_in_colab))
    content = extract.lower()
    index1=extract.find("CASTE")
    index2=extract.find("NON-CREAMY")
    if index1>=0 and index2>=0 :
        part1=extract[index1:index2].lower()
        part2=extract[index2:].lower()
        print(f"{part1} \n {part2}")
        
    
    #part !1 validation keys 
    error = []
    counti=0
    if part2.find("2022")>0 or part2.find("2023")>0 or part2.find("2024")>0 :
        print ( name , "valid year")
    else :
        error.append(name)
        print("invalid year of issue for " , name )


    for key in keys :
        if  part1.find(key.lower())>=0:
            counti+=1
            print(f"found key {key}")
    print(counti)
    
    if counti < len(keys):
        error.append(name)
        errorlist.append(error)



print (errorlist)