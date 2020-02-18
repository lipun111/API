import requests

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='apijson'
resp = requests.get(BASE_URL+ENDPOINT)
data = resp.json()
print('Data From Django Application:')
print('#'*50)
print('Employee Number:', data['eno'])
print('Employee Name:', data['ename'])
print('Employee Salary:', data['esal'])
print('Employee Address:', data['eaddr'])
