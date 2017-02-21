import json, requests

def student_list():
    result = requests.get('http://127.0.0.1:8000/studentapi')
    return result.json()
