import untitled10
import requests
import json

class BAND:
    """
    contains info af all different bands 
    """
    def __init__(self, name, body, band_key, post_key="", do_push=True):

        self.name = name
        self.body = body
        self.band_key = band_key
        self.post_key = post_key

    def get_bands(self):
        url = 'https://openapi.band.us/v2.1/bands'
        params = {
            'access_token':access_token
        }
        response = requests.get(url, params=params)
        print(response.json())

    def create_post(self):
        url = 'https://openapi.band.us/v2.2/band/post/create'
        params = {
            'access_token': access_token,
            'band_key': self.band_key,
            'body':self.body,
            'do_push':True
        }
        response = requests.post(url, params=params)
        print(response.json())
        
def info():
        
        choice = int(input("opertaion options\n1) GET INFO OF ALL BANDS\n2) CREATE A POST : "))
        if choice == 1:
            bot_testings.get_bands()
        elif choice == 2:
            create_post()
        else:
            print("bad input")
# band 1) bot_testing
bot_testings = BAND("bot_testing", "hey this post is created by latest code written in python if you see this then its woking yay", 'AADXsUVwfSTevR41SjnZ9hlb') 
info()


