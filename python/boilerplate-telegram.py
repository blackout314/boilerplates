import requests

def send_telegram(message, chatid, botapi):
  requests.get("https://api.telegram.org/bot"+botapi+"/sendMessage?chat_id="+chatid+"&text='"+message+"'")
