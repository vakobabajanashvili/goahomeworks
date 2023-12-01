import requests

payload = {
    "content": "გასასპამი ტექსტი"
}

header = {
    'authorization': 'h4EjcfGjNHiYWnR3vA0emk7Moeo='
}

for i in range (2):
   payload = {
      'content': "გასასპამი ტექსტი"
   }
   r = requests.post('https://www.instagram.com/api/graphql/', data=payload, headers=header)