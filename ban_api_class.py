import requests

access_token = 'ZQAAAXMyrZS9z1YfkWsVXRdZtvcAAQ4zvhT1S2aoD5id-SHV7w_2o406552mz8S8IcF-RWIYMdwbXvMngvcdVxCmIrKs8eRPNoz-sD3UvIqG3OFa'

class BAND:
  def _init_(self, name, body, band_key, post_key="", do_push=True):
    self.name = name
    self.body = body
    self.band_key = band_key
    self.post_key = post_key
    self.do_push = do_push

  def create_post(self):
    url = 'https://openapi.band.us/v2.2/band/post/create'
    
    params = {
        'access_token': access_token,
        'band_key': self.band_key,
        'content': self.body,
        'do_push': self.do_push
    }

    print(params)
    response = requests.post(url,params=params)
    print(response)
    print(response.json())
       
bot_testing = BAND("bot_testing","This is not hardcoded content","AADXsUVwfSTevR41SjnZ9hlb",True)
bot_testing.create_post()