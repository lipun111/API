import requests
import json
BASE_URL='http://127.0.0.1:8000/'
# ENDPOINT = 'apiall/'
ENDPOINTS = 'api/'

# def get_resources(id=None):
#     data ={}
#     if id is not None:
#         data ={
#         'id':id
#         }
#     resp = requests.get(BASE_URL+ENDPOINTS,data = json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resources(1)
# #
# #
# def get_all():
#     resp = requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())

def create_record():
    new_emp = {
        'eno':106,
        'ename':'Hari lal',
        'esal':60000,
        'eaddr':'keonjhar gada',
    }
    resp = requests.post(BASE_URL+ENDPOINTS, data = json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
create_record()

# def update_record(id):
#     new_emp = {
#         'id':id,
#         'ename':'Sunny1',
#         'esal':10000,
#
#     }
#     resp = requests.put(BASE_URL+ENDPOINTS, data = json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_record(2)
# #
# def delete_record(id):
#     data = {
#     'id':id
#     }
#     resp = requests.delete(BASE_URL+ENDPOINTS,data = json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete_record(4)
