#!/usr/bin/python
import nltk
import sys
import textblob
import io
reload(sys)
sys.setdefaultencoding('utf-8')


text1=io.open('sample.txt', 'r', encoding='utf-8')
text=text1.read()
print(text)
blob=textblob.TextBlob(text)

print(blob)
#print(blob.tags)
print(blob.noun_phrases)
