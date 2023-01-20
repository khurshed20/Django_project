import requests 

def API_Response():
    url='http://api.github.com/search/repositories?q=language:python & sort=stars'
    headers={'Accept':'application/vnd.github.v3+json'}
    r=requests.get(url, headers=headers)
    print("Status code : ",r.status_code)
    response_dict=r.json()
    print(response_dict.keys())
    #x="This is api_response_py"
    return response_dict