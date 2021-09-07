import json
import requests

access_token = 'ZQAAAXMyrZS9z1YfkWsVXRdZtvcAAQ4zvhT1S2aoD5id-SHV7w_2o406552mz8S8IcF-RWIYMdwbXvMngvcdVxCmIrKs8eRPNoz-sD3UvIqG3OFa'

# class comments:
#     def get_comments(self,band_key,post_key):
#         counter=""
#         url = 'https://openapi.band.us/v2/band/post/comments'
#         params = {
#             'access_token': access_token,
#             'band_key': band_key,
#             'post_key': post_key,

#         }
#         response = requests.get(url, params=params)
#         response_json = json.loads(response.text)
#         print(type(len(response_json['result_data']['items'][1]['content'])))
#         print(response_json['result_data']['items'][1])
        
#         for i in range(len(response_json['result_data']['items'])):
#             counter = counter + response_json['result_data']['items'][i]['author']['name'] , response_json['result_data']['items'][1]['content'], response_json['result_data']['items'][1]['comment_key']

#         return counter

#     def delete_comments(self):
#         # url = 'https://openapi.band.us/v2/band/post/comment/remove'
#         comment = self.get_comments('AADXsUVwfSTevR41SjnZ9hlb','AACeZ0rWMY6KnCNtgTv6ZNaF')
#         # index = input("which comment u wanna delete (0 means latest)")
#         # comment_key = response_json['result_data']['items'][index]['comment_key']
#         print(comment)
        

#         # params = {
#         #     'access_token': access_token,
#         #     'band_key': band_key,
#         #     'post_key': post_key,
#         #     'post_key': comment_key
#         # }
#         # response = requests.post(url , params=params)
#         # print(response.json())

       



# bot_testig = comments()
# bot_testig.delete_comments()

url = 'https://openapi.band.us/v2/band/post/comment/remove'

params = {
    'access_token':access_token,
    'band_key':'AADXsUVwfSTevR41SjnZ9hlb',
    'post_key':'AACeZ0rWMY6KnCNtgTv6ZNaF',
    'post_key':'AAC6BX4X4vfcxrBGtomcNcIf'
}
response = requests.post(url, params=params)
print(response.json())