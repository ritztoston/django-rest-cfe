import requests
import json
import os

ENDPOINT = 'http://localhost:8000/api/status/'

# def do(method='get', data={}, id=1, is_json=True):
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT + '?id=' + str(id), data=data)
#     print(r.text)
#     return r
#
# do(data={'id': 6})

image_path = os.path.join(os.getcwd(), 'Chris_Inglis.png')

def do_img(method='get', data={}, id=1, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    if img_path is not None:
        with open(img_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    return r

do_img(method='post', data={'user':1, 'content': ''}, is_json=False, img_path=image_path)
