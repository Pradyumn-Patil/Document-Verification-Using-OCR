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
    keys.append(cand_list['Catergory'][ind])
    keys.append(cand_list['Caste'][ind])
    keys.append(str(cand_list['Caste Number'][ind]))
    keys.append('2022')
    keys.append('2023')
    keys.append('2024')
    image_path_in_colab=cand_list['path'][ind]
    im = cv2.imread(image_path_in_colab, cv2.IMREAD_COLOR)

    extract = pytesseract.image_to_string(Image.open(image_path_in_colab)).lower()
    content = extract
    print(keys)
    counti=0
    error = []
    for key in keys :
        if  content.find(key.lower())>=0:
            counti+=1
            print(f"found key {key}")
    print(counti)
    
    if counti<8:
        error.append(name)
        print(error)
        errorlist.append(error)



print (errorlist)