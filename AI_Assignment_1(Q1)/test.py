import os,csv
import aiml,random,requests,decimal
import mysql.connector
from flask import Flask, request, jsonify
import sqlite3
import pandas as pd

kernel = aiml.Kernel()
kernel.learn("basic.aiml")
#kernel.learn("inbuilt.aiml")

person = []
conversation = []

while True:
    input_text = input("Human> ")
    person.append("Human : ")
    conversation.append(input_text)  
    if(input_text=="Bye"):
        print("Bye Have a nice day")
        break
    response = kernel.respond(input_text)
    person.append("Bot : ")
    conversation.append(response)

    if(response[:85]=='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a'):
        city = response[85:]
        api = response[:85] + "&q=" + city
        json_data = requests.get(api).json()
        print("Weather for the "+city+" has temperature = "+ str((json_data['main']['temp'])-273)[:6] + " Celsius," + " having the conditions "+json_data['weather'][0]['main']+ " and humidity "+str((json_data['main']['humidity']))[:6])
    else:
        print("Bot> "+response)

#df = pd.DataFrame(conversation)
df = pd.DataFrame(list(map(list, zip(person,conversation))))
df.to_csv('chats.csv')
