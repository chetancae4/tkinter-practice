import sys
import numpy as np
import wikipedia
from PIL import Image
from wordcloud import WordCloud,STOPWORDS
x=str(input("enter the title : "))
title=wikipedia.search(x)[0]
page=wikipedia.page(title)
text=page.content
print(text)
background=np.array(Image.open("4.png"))
stopwords=set(STOPWORDS)   #it removes word like is the who were etc in the paragraph
wc=WordCloud(background_color="white", #extract text from wikipedia page
             max_words=200,
             stopwords=stopwords)
wc.generate(text)
wc.to_file("5.png")  #saving file