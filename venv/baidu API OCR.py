from aip import AipOcr
import re


APP_ID = '11374661'
API_KEY = 'WfTRrnFsPYLdOZHUpZ1KXOO7'
SECRET_KEY = 'HIh3G6R5MnCOr8LgAMxM70eNNdevHWgU'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

ia=open(r'C:\Users\CBJ\Desktop\TIM截图20180714115135.png', 'rb')
ima=ia.read()
message=client.basicGeneral(ima)
for i in message.get('word_result_num',message):
  print(message.get('word', message))
