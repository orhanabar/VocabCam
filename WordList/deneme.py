import os 
import string 
from nltk.stem.snowball import SnowballStemmer
from googletrans import Translator
import pandas as pd


doc_list = list()
with os.scandir("c:/Users/Semih/Documents/GitHub/VocabCam/WordList") as tarama:
    for belge in tarama:
        if belge.name.endswith("txt"):
            doc_list.append(belge.name)

for i in doc_list:

    with open(i,"r+",encoding="utf-8") as file:
        content= file.readlines()
        parag=  file.read()
    untitled=""
    for a in content:
        if(a.isupper()==True or (a.istitle()==True)):
            untitled += " "
        else:
            untitled += a + " "
    with open("Son "+i,"a",encoding="utf-8") as file1:
        for b in untitled:
            file1.write(b)
    with open("Son "+i,"r",encoding="utf-8") as file: 
        contents=file.read()
        content_clear =contents.replace("\n","")
        content_clear = content_clear.replace("/n","")
    
        def punctuation_clear(text):
            result = ""
            for i in text:
                if( i not in string.punctuation or i == " " ):
                    result+= i 
                else:
                    result+= ""
            return result
        def punctuation_clear_list(text):
            result = ""
            for i in text:
                for a in i:
                    if( a not in string.punctuation or a == "." or a == " " ):
                        result+= a 
            
            return result
        content_clears = punctuation_clear(content_clear)
        content_split_sentence = punctuation_clear_list(content_clear).split(".")
        content_word_split= set(content_clears.split())
        word_list= list()
        say = 0
        for i in content_word_split:
            if(len(i)>=3):
                word_list.append(i)
    
    sentence_list_last= list()
    for a in word_list:
        x=0
        for i in content_split_sentence:
            sentence = i.split()
            for j in sentence:
                if a==j:
                    sentence_list_last.append(i)
                    x+=1
                if x==1:
                    break
            if x==1:
                break
            
    content_clear_split_last = list()
    
    stem_list=[]

    for i in word_list:
        stemmer = SnowballStemmer("english")
        stem_list.append(stemmer.stem(i))
    
    translator = Translator()
    ceviri_list= list()
    for i in word_list:
        translation = translator.translate(i,dest = 'tr')
        ceviri_list.append(translation.text)    
    
    dict = {"Raw":word_list,"Root":stem_list,"Translation":ceviri_list,"Sentence":sentence_list_last}
    df= pd.DataFrame(dict)
    df.to_csv(i+".csv")