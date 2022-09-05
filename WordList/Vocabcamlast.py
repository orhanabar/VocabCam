import os
import pytesseract
from pdf2image import convert_from_path
import string 
from nltk.stem.snowball import SnowballStemmer
from googletrans import Translator
import pandas as pd
import string 
from nltk.tokenize import sent_tokenize

def vocab_cam(file_name1):
    def File_Content(file_name):
        file_str = ''

        if file_name.endswith('.pdf'):
            pdf_file = convert_from_path(file_name)

            for i in range(len(pdf_file)):
                pdf_file[i].save(f'page{str(i + 1)}.jpg', 'JPEG')   # Saves pages as images in the pdf
                file = f'page{str(i + 1)}.jpg'
                file_str += pytesseract.image_to_string(file)
                # os.remove(file)   # Deletes saved image files
        elif file_name.endswith(('.jpg', '.png')):
            file_str = pytesseract.image_to_string(file_name)   
        return file_str
    file_cont= File_Content(file_name1)
    
    with open("Deneme.txt","a",encoding="utf-8") as file:
        file.write(file_cont)  
    with open("Deneme.txt","r+",encoding="utf-8") as file:
        content= file.readlines()
        parag=  file.read()
        untitled=""
        for i in content:
            if(i.isupper()==True or (i.istitle()==True)):
                untitled += " "
            else:
                untitled += i + " "
    with open("Computer Reading Son.txt","a",encoding="utf-8") as file1:
        for i in untitled:
            file1.write(i)
    with open("Computer Reading Son.txt","r",encoding="utf-8") as file:
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
        
        for i in content_word_split:
            if(len(i)>=3):
                word_list.append(i)
    sentence_list_last = list()
    
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
        from nltk.stem.snowball import SnowballStemmer
        stem_list=[]

        for i in word_list:
            stemmer = SnowballStemmer("english")
            stem_list.append(stemmer.stem(i))
        #stem_set = set(stem_list)
        #stem_list = list(stem_set)
        from googletrans import Translator
        translator = Translator()
        ceviri_list= list()
        for i in word_list:
            translation = translator.translate(i,dest = 'tr')
            ceviri_list.append(translation.text)
        from nltk.corpus import state_union
        import nltk
        from nltk.tokenize import PunktSentenceTokenizer
        code_list = list()
        for i in word_list:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                code_list.append(tagged[0][1])
        import pandas as pd
        dict = {"Code:":code_list,"Raw":word_list,"Root":stem_list,"Translation":ceviri_list,"Sentence":sentence_list_last}
        df= pd.DataFrame(dict)
        df.to_csv("Computer Reading Translate.csv")
        
        
vocab_cam('Computer Reading.pdf')
