import requests

import json

import mysql.connector

try:

    mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'userdb')

except mysql.connector.Error as e:

    print("sql connection error",e)



mycursor = mydb.cursor()



data=requests.get("https://jsonplaceholder.typicode.com/users").text




data_info=json.loads(data)



#print(data_info)



#user_list=[]



for i in data_info:

    sql="INSERT INTO `users`(`name`, `email`, `phone`) VALUES ('"+i['name']+"','"+i['email']+"','"+i['phone']+"')"

    mycursor.execute(sql)

    mydb.commit()

    print("data inserted succesfully",i["name"])



    #print(user_list)