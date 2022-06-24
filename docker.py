import requests
url = 'https://talktohelp.herokuapp.com/webhooks/rest/webhook'
myobj = {
"message": "hi",
"sender": 1,
}
x = requests.post(url, json = myobj)
print(x.text)