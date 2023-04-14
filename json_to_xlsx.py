import time
import multiprocessing
import xlsxwriter
import numpy as np
from tkinter import N
import random
import time
import enum
import json
import nltk
import re
import xlsxwriter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from contextlib import closing
from multiprocessing import Pool, cpu_count
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

workbook = xlsxwriter.Workbook('Tweets.xlsx')
worksheet = workbook.add_worksheet('Tweets')

stpwrd = stopwords.words('english')
stpwrd.extend(['that', 'thats', 'that´s'])
file = open('datos.json')
datos = json.load(file)
titles = ['N°', 'Palabras Clave', 'Polaridad', 'Subjetividad', 'Sentimiento', "ngramas"]
row = 0
for col, data in enumerate(titles):
    worksheet.write(row, col, data)

tweets = []

workbook = xlsxwriter.Workbook('Tweets.xlsx')
worksheet = workbook.add_worksheet('Tweets')



def procesarTweet(num):
    for i in range(num):
      datos[i]['Contenido'] = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', datos[i]['Contenido'])
      datos[i]['Contenido'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",datos[i]['Contenido'])

      a = "Neutral"
      # Eliminar stopwords
      tweet = datos[i]['Contenido']
      tokens = word_tokenize(tweet)

      tokens_limpios = [word for word in tokens if not word in stpwrd]
      tweet = " ".join(str(x) for x in tokens_limpios)
      sentimiento = TextBlob(tweet)

      worksheet.write(i, 0, i)
      worksheet.write(i, 1, tweet)
      worksheet.write(i, 2, sentimiento.polarity)
      worksheet.write(i, 3, sentimiento.subjectivity)
      if(sentimiento.polarity < 0):
        a = "Negativo"
      if(sentimiento.polarity > 0):
        a = "Positivo"
      worksheet.write(i, 4, a)
      #print(sentimiento.ngrams)
      #worksheet.write(i, 5, "".join(sentimiento.ngrams.))

num = 20000
# for i in range(num):
#   tweets.append([i, len(word_tokenize(datos[i]['Contenido']))])
procesarTweet(num)
workbook.close()
fin = time.time()