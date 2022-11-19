import tweepy
import csv
import re

#Cadenas de autenticación
consumer_key = "EQpbZXI0fV7giWd4xwE3TVLgK"
consumer_secret = "uOG4mieyB0TTVBm8EEc2NMYdEn0lRmOV1WSXZvOK7nDiwDUj70"
access_token = "1444477757782691846-TM5hyADtcgK9f239As2zD6XQOURxl2"
access_token_secret = "9R9NwSMJBNGSVPF5nqf2o9JyLUjhzNMT7Mp2GTQt0kPKH"

#Términos de busqueda
search_words = ["geopipedistas","Cabez_plana","Escepticos","Cospiranoicos","Creyentes precientificos"]

#Nombre de archivos
archivos = ["geopipedistas.csv","Cabez_plana.csv","Escepticos.csv","Cospiranoicos.csv","Creyentes_precientificos.csv"]

#Conexión con la api de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

for nombre,busqueda in zip(archivos,search_words):
    busqueda = busqueda + " -filter:retweets"
    with open(nombre, 'a', encoding = 'utf-8') as f:
        csvWriter = csv.writer(f)
        for tweet in tweepy.Cursor(api.search_tweets, q=busqueda, tweet_mode = "extended", lang= "en").items(500):
            tem = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet.full_text).split()) 
            csvWriter.writerow([tweet.created_at, tem])
