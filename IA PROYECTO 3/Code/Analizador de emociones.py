import pandas as pd
from googletrans import Translator
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import re


sentimientos_tweet =()

def traducir_tweet(string):
    translator = Translator()
    #blob_object = TextBlob(string)
    #string = blob_object.translate(to = "en")
    #Traduce el tweet detectando automaticamente el idioma del tweet
    try:
        string = translator.translate(string, "en")
        string = string.text
        #verificamos el resultado
        # #print(string)
    except Exception as e:
        print(e) 
    return string

def limpia_tweet(string):
    characters = "@1234567890"
    string = ''.join( x for x in string if x not in characters)
    string = re.sub(r'https?:\/\/.\S+', "", string) 
    #string = re.sub(r'#', '', string) 
    string = re.sub(r'^RT[\s]+', '', string)
    return string

def sentimiento_tweet(string):
    blob_object = TextBlob(string, analyzer=NaiveBayesAnalyzer())
    # Valora todo el tweet para decidir si es positivo o negativo
    # El algoritmo de NaiveBayesAnalyzer fue entrenado con reseñas de peliculas
    #analysis = blob_object.sentiment
    #print(analysis)
    analysis = blob_object.polarity
    #print(analysis)
    return analysis

#c = "Habrá algún pasaje al mar y de ahí a traspasar el gran muro de hielo de la Antártida hacia su base "

#s = traducir_tweet(c)
#print(c)
#print(s)
#Main

#Unir todos los csv

csv1 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\Antartida.csv',encoding='unicode_escape')
csv2 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\cabeza plana.csv',encoding='unicode_escape')
csv3 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\conspiraciones.csv',encoding='unicode_escape')
csv4 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\conspiranoicos medievales.csv',encoding='unicode_escape')
csv5 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\domo.csv',encoding='unicode_escape')
csv6 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\infinita plana.csv',encoding='unicode_escape')
csv7 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\muro de hielo.csv',encoding='unicode_escape')
csv8 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\plano pensantes.csv',encoding='unicode_escape')
csv9 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\terraglobistas.csv',encoding='unicode_escape')
csv10 = pd.read_csv('C:\\Users\\jcuay\\OneDrive\\Otoño 2022\\Tecnicas de IA\\IA PROYECTO 3\\tweets TP\\terraplanistas.csv',encoding='unicode_escape')
#solo texto
#print("*** Merging multiple csv files into a single pandas dataframe ***")
#data=pd.read_csv("C:\\Users\\akashkumar\\Downloads\\Customers.csv",encoding='unicode_escape')

# merge files

alltweets = pd.concat([csv1, csv2, csv3, csv4, csv5, csv6, csv7, csv8, csv9, csv10], axis=0)
#alltweets = pd.concat(map(csv1, csv2, csv3, csv4, csv5, csv6, csv7, csv8, csv9, csv10))
#print(alltweets)
general = []

i=1
#print(alltweets['Tweet'])
general = []
for tweet  in alltweets['Tweet']:
#   print(i)
#    i+=1
#    Traduce el tweet
#    tweet = traducir_tweet(tweet)
#    #Limpia el tweet de caracteres especiales y de urls
    tweet = limpia_tweet(tweet)
#    #Se hace el analisis de sentimientos 
    analysis = sentimiento_tweet(tweet)
    if analysis > 0:  #El tweet es positivo
        sentimiento = "positivo"
        general.append([tweet, sentimiento, analysis])
    if analysis < 0:  #El tweet es negativo
        sentimiento = "negativo"
        general.append([tweet, sentimiento, analysis])
    if analysis == 0: #El tweet es neutral
        sentimiento = "neutro"
        general.append([tweet,  sentimiento, analysis])

df = pd.DataFrame(general, columns=['tweeet','Sentimiento', 'Ponderacion'])
df.to_csv('Diccionario_Sentimientos2.csv')