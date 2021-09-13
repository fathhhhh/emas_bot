# import requests module
import requests
from datetime import datetime

# Making a get request
response = requests.get('api')

# print json content
result = response.json()

# scrap result from json
matawang = result["currency"]
harga = result["gappricepergram"]
hargaMYR = result["gapgramperprice"]

# masa 
now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")
current_day = now.strftime("%d-%h-%y")

def telegram_bot_sendtext(bot_message):
    
    bot_token = 'token'
    bot_chatID = 'id'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    final = requests.get(send_text)

    return final.json()

my_message = " HARGA EMAS HARI INI \nMasa : "+ current_day + " "+ current_time + "\nHarga RM100 : " + hargaMYR + " gram" +  "\nHarga per gram : RM" + harga  
telegram_bot_sendtext(my_message)
