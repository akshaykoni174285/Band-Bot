

import requests
import json


class BAND:
  def __init__(self, name, body, band_key, post_key="", do_push=True, locale="en_IN"):
    self.name = name
    self.body = body
    self.band_key = band_key
    self.post_key = post_key
    self.do_push = do_push
    self.locale = locale

  def  get_bands(self):
    url = 'https://openapi.band.us/v2.1/bands'
    params = {
        'access_token':access_token

    }
    response = requests.get(url, params=params)
    print(response.json())

  def get_posts(self):
    url= 'https://openapi.band.us/v2/band/posts'
    params = {
        'access_token':access_token,
        'band_key':self.band_key,
        'locale':self.locale,

    }
    response = requests.get(url, params=params)
    todos = json.loads(response.text)
    return todos['result_data']['items'][0]['post_key']

  def get_user_profile(self,band_key='AADXsUVwfSTevR41SjnZ9hlb'):
    url = 'https://openapi.band.us/v2/profile'

    params = {
        'access_token':access_token,
        'band_key': band_key,

    }
    print(band_key)
    response = requests.get(url, params=params)
    print(response.json())

  def write_comment(self,content):
    url = 'https://openapi.band.us/v2/band/post/comment/create'
    post_key = self.get_posts()
    params = {
      'access_token':access_token,
      'band_key':self.band_key,
      'body':content,
      'post_key':post_key
      
    }
    response = requests.post(url, params=params)
    print(response.json())

  def delete_latest_post(self):
    url = 'https://openapi.band.us/v2/band/post/remove'
    post_key = self.get_posts()
    params = {
      'access_token':access_token,
      'band_key':self.band_key,
      'post_key':post_key,
    }
    response = requests.post(url, params=params)
    print(response.json())
    
  def create_post(self):
    url = 'https://openapi.band.us/v2.2/band/post/create'
    
    params = {
    'access_token': access_token,
    'band_key': self.band_key,
    'content': self.body,
    'do_push': self.do_push
    }

    response = requests.post(url,params=params)
    print(response)
    print(response.json())
       
bot_testing = BAND("bot_testing","testing","AADXsUVwfSTevR41SjnZ9hlb",True)
# bot_testing.get_posts()
# bot_testing.create_post()
hello=bot_testing.get_posts()
print(hello)
# bot_testing.delete_latest_post()

# bot_testing.write_comment("hello adding comment from bot yay")
# bot_testing.create_post()

def test():
  print("hello this is testing and its kinda coo")
  url = ""
  params = {
    'band_key': 
  }





