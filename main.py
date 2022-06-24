import requests
url = 'http://talktohelp.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
"message": "hi",
"sender": "Ashish",
}
x = requests.post(url, json = myobj)
print(x.text)