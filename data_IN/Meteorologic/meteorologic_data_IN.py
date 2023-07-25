import json
import requests
import django
import os
import http.cookiejar
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.test import Client


URL = 'http://localhost:8000/meteorologicData/insert24h'



#programa
class Meteo_24h():
    def __init__(self,timestamp,temp_avg,temp_max,temp_min,hrel_avg,pressao_avg,pnmm_avg,precip_tot):
        super().__init__()
        self.timestamp = timestamp
        self.temp_avg = temp_avg
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.hrel_avg = hrel_avg
        self.pressao_avg = pressao_avg
        self.pnmm_avg = pnmm_avg
        self.precip_tot = precip_tot

data_24H_array = []
data_24H_file = open("Dados24h.dat","r")
flag = 0
for line in data_24H_file:
    flag = flag + 1
    if flag <= 4:
        continue

    list = line.split(",")

    data_24H_array.append(Meteo_24h(list[0].strip('"'),list[3],list[4],list[5],list[7],list[11],list[15],list[30]))


data_24H_file.close()

data_24H_json = json.dumps(data_24H_array,default=lambda o: o.__dict__, indent=2)

data_24H_json_file = open("data_24h_json.json","w")
data_24H_json_file.write(data_24H_json)
data_24H_json_file.close()

#csrf token

client = requests.session()
client.get(URL)
csrftoken = client.cookies['csrftoken']
my_cookies = {"X-CSRFToken":csrftoken}
#print(my_cookies)
r =client.post(URL,data = data_24H_json,headers=my_cookies)
#print(r.text)


    
    