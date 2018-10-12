import requests
import json
import os
AUTH_ENDPOINT = 'http://localhost:8000/api/auth/jwt/'
REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
ENDPOINT = 'http://localhost:8000/api/status/'

headers = {
    'Content-Type': 'application/json',
}

data = {
    'username': 'ritztoston',
    'password': 'Kimritzter1'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers = headers)
token = r.json()['token']

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'JWT ' + token,
}
print(headers)

post_data = json.dumps({'content': 'Some random content'})
posted_response = requests.post(ENDPOINT, data=post_data, headers=headers)
print(posted_response.text)

# REFRESH JWT TOKEN
# refresh_data = {
#     'token': token
# }
#
# token = r.json()['token']
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers = headers)
# new_token = new_response.json()['token']
#
# print(new_response.json())


# def do(method='get', data={}, id=1, is_json=True):
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT + '?id=' + str(id), data=data)
#     print(r.text)
#     return r
#
# do(data={'id': 6})

# image_path = os.path.join(os.getcwd(), 'Chris_Inglis.png')

# def do_img(method='get', data={}, id=1, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#
#     if img_path is not None:
#         with open(img_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     return r
#
# do_img(method='put', data={'id': 7, 'user': 1,'content': 'Some new great content'}, is_json=False, img_path=image_path)

# get_endpoint = ENDPOINT + str(12)


# r = requests.get(get_endpoint)
# print(r.text)
#
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
#
# post_headers = {
#     'content-type': 'application/json'
# }
#
# post_responds = requests.post(ENDPOINT, data=post_data, headers = post_headers)
# print(post_responds.text)
