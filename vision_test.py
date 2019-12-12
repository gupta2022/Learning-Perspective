import os,io
from google.cloud import vision
from google.cloud.vision import types
#import panda as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='learning-perspective-7179ad627978.json'

client = vision.ImageAnnotatorClient()
#print (dir(client))

with io.open("abcd.jpeg",'rb') as image_file:
    content =image_file.read()
image=vision.types.Image(content=content)
response=client.text_detection(image=image)
#df=pd.Dataframe(columns=['locale','description'])
print(response.text_annotations.descriptions)