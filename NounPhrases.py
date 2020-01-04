import nltk
import textblob
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')	
nltk.download('brown')	
file1="Notes/me.txt"
text1=open(file1, 'r', encoding='utf-8')
text=text1.read()
blob=textblob.TextBlob(text)
nounph=blob.noun_phrases
file2="NounPhrases/me.txt"
f = open(file2, "w")
for i in nounph:
    f.write("\""+i+"\",")
f.close