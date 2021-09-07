import requests
import untitled10

    


params = {
    'access_token': access_token,
    'band_key': 'AADXsUVwfSTevR41SjnZ9hlb',
    'content': 'hello from python code ',
    'do_push':True
}
url = 'https://openapi.band.us/v2.2/band/post/create'



response = requests.post(url, params=params)
response_json = response.json()
print(response)
print(response.json())