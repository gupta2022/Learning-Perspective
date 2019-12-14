import nltk
import textblob
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')	
nltk.download('brown')	
import csv

bad_chars = [';', ':', '!', '*','`'] 
##Frequency Of A String
def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1   
    if my_list == nounph:
        with open('networking1.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["String ", "Count"])
            for key, value in freq.items(): 
                print (key, value)
                writer.writerow([key,value])
    elif my_list == nounph2:
        with open('networking2.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["String ", "Count"])
            for key, value in freq.items(): 
                print (key, value)
                writer.writerow([key,value])
    else:
        with open('ncert_networking.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["String ", "Count"])
            for key, value in freq.items(): 
                print (key, value)
                writer.writerow([key,value])

file1="networking_notes1.txt"
file2="networking_notes2.txt"

file3="ncert_networking.txt"

text1=open(file1, 'r', encoding='utf-8')
text=text1.read()
print(text)
blob=textblob.TextBlob(text)
#print(blob.noun_phrases)
nounph=blob.noun_phrases
# Not Working
#for a in nounph:
 #   for i in bad_chars:
  #      a=a.replace(i,' ')
CountFrequency(nounph)


text2=open(file2, 'r', encoding='utf-8')
text=text2.read()
print(text)
blob2=textblob.TextBlob(text)
#print(blob.noun_phrases)
nounph2=blob2.noun_phrases
CountFrequency(nounph2)

text3=open(file3, 'r', encoding='utf-8')
text=text3.read()
print(text)
blob2=textblob.TextBlob(text)
#print(blob.noun_phrases)
nounph3=blob2.noun_phrases
CountFrequency(nounph3)