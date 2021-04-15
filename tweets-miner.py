#Acessar o Twitter via API com Python

#import os
import tweepy as tw 
import pandas as pd

# Definindo token's de acesso, twitter developer tools

consumer_key= '2Pa4kELzUNk2ySa6d1bXzQdfH'
consumer_secret= 'GFWpLjikar5W0yySkQKsHuL0fSNj5kxDG56dq09gkFniKXXKiD'
access_token= '1372604758880612352-cEhcjlNcJh7MIfGUjWvmvkRyMyBvEx'
access_token_secret= 'pPuVnsN3DD1NVPKd4FkpWkA1DJ5OS4E7Rd3sUsejlUXRh'

# Definindo as palavras-chave para a busca

search_words = "#Isolamento"
new_search = "#Lockdown"
date_since = "2021-04-01"

#Limite de tempo
count = 50000

# Definindo e validando a seção de login 

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#Testando o API 
#Falta validar a autorização
#api.update_status("Postando um twitter diretamente pelo API !")
#Postado

# Coletando Tweets

tweets = tw.Cursor(api.search,  #Aqui ele vai procurar os tweets pela palavra #Isolamento linha 16
              q=search_words,
              lang="en",
              since=date_since).items(15) # Define o número de tweets que será retornado, junto da data inicial

# Testando se o API funcionou, irá retornar alguma mensagem 0x7fafc296e400
tweets


# Função que limpa caracteres especiais e links

#def _clean_tweet(self, tweet.text):

#       clean_text = re.sub(r'RT+', '', tweet.text)
  #     clean_text = re.sub(r'@\S+', '', clean_text)
  #      clean_text = re.sub(r'https?\S+', '', clean_text)
   #     clean_text = clean_text.replace("\n", " ")


# Mostrando os tweets

for tweet in tweets:
    print(tweet.text)



# Nova busca , com nome e localização

tweets = tw.Cursor(api.search, 
                           q=new_search,
                           lang="en",
                           since=date_since).items(15)

users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text, tweet.created_at] for tweet in tweets]

#Testando o API, tem que retornar apenas Nome usuário e localização

users_locs


# Formatando os tweets minerados

tweet_text = pd.DataFrame(data=users_locs,  # Utilizar os valores coletados da variável users_locs NOME e LOCALIZAÇÃO
                    columns=['Usuarios', "Localizacao" , "Texto" , "Postado em"]) # Define o nome das colunas

# Testa o resultado
tweet_text








