
import nltk
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')
    # nltk.download('brown')
    # pip install textblob
import textblob
text1=open('sample.txt')
text=text1.read()
#print(text)
blob=textblob.TextBlob(text)

#print(blob)
#print(blob.tags)
print(blob.noun_phrases)