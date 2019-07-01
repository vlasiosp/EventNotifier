import requests, bs4

s = requests.Session()
url = 'https://www.facebook.com/login'

res = s.get(url)
form_data = {'email': 'teipir@gmail.com',
             'pass' : '19eptalofou76'
            }
s.post(url, data=form_data)