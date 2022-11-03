import requests
import json
import mysql.connector
import sys

try:
    mydb = mysql.connector.connect(host = 'localhost', user = 'root',password = '',database = 'userdb')
except mysql.connector.Error as e:
    sys.exit("exception in mydb connection")
mycursor =mydb.cursor()

data = requests.get("https://jsonplaceholder.typicode.com/posts").text

data_info = json.loads(data)
for i in data_info:
    id = str(i['id'])
    sql = "INSERT INTO `post`(`user_id`, `title`, `body`) VALUES ('"+id+"','"+i['title']+"','"+i['body']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("data inserted successfully" ,i['id'])