#importa las librerias necesarias para trabajar las descargas
import snscrape.modules.twitter as sntwitter
import pandas as pd

#Lectura de la palabra, hashtag o usuario a buscar 
palabra_buscar = input("Dame la palabra o hashtag a buscar: ")
#Se pide el nombre del archivo para guardar las descargas
nombre=input("Deme el nombre del archivo a guardar: ")
#Se crea un arreglo de los encabezados que vamos a leer
tweets = []
#numero de Tweets a Descargar en este caso 50000
limit = 5000
for tweet in sntwitter.TwitterSearchScraper(palabra_buscar).get_items():
    if len(tweets) == limit:
        break
    else:
        # La obtencion de los tweets los obtiene en un objecto con los
        # atributos de id del tweet, fecha, Usuario, y el contenido del tweet
        tweets.append([tweet.id, tweet.date, tweet.user.username, tweet.content])        
df = pd.DataFrame(tweets, columns=['Id_tweeet','Fecha', 'User', 'Tweet'])
#imprime en consola los resultado
df.head(100)
#Lo guarda el archivo con formato csv
df.to_csv(nombre+'.csv')
