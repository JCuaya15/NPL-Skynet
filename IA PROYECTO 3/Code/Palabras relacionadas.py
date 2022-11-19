import pandas as pd
from textblob import TextBlob
import pandas as pd
#import matplotlib.pyplot as plt

df = pd.read_csv('Diccionario_Sentimientos2.csv')
#Clasifica en postivos y negativos
is_pos = df.loc[:, 'Sentimiento'] == 'positivo'
df_pos = df.loc[is_pos]
#df_pos.head(100)
#print(df_pos)
df_pos.to_csv('pos.csv')
#Clasifica en negativos
is_neg = df.loc[:, 'Sentimiento'] == 'negativo'
df_neg = df.loc[is_neg]
#df_neg.head(100)
#print(df_neg)
df_neg.to_csv('neg.csv')

def palabras_rela (string):
    lista =[]
    alltweets = pd.read_csv( string +".csv")
    for tweet  in alltweets['tweeet']:
        blob_object = TextBlob(tweet)
        lis =blob_object.tags  
        for pal in lis:
            if (len(pal[0]) > 3):
                lista.append([pal[0], pal[1]])

    df2 = pd.DataFrame(lista, columns=['Palabra','Etiqueta'])
    is_jj = df2.loc[:, 'Etiqueta'] == 'NN'
    df3 = df2.loc[is_jj]
    df4 = df2['Palabra'].value_counts()
    print (df4)
    df4.to_csv("Palabras "+string+'.csv')

palabras_rela("pos")
palabras_rela("neg")
