import DHT
import time
import pigpio
import sqlite3
import sys

connection = sqlite3.connect("/home/pi/apps/dht11/dht.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS DHT  (time TEXT, temp TEXT, humidity TEXT)") 
connection.commit()
pin = 4
pi = pigpio.pi()
sensor = DHT.sensor(pi, pin)
while True:
  sensorarray = sensor.read()
  #sys.stdout.write(f"Code: {sensorarray[2]}\n")
  if sensorarray[2] == 0:
    temp_c = sensorarray[3]
    humidity = sensorarray[4]
    cursor.execute(f"INSERT INTO DHT VALUES ('{sensorarray[0]}', '{temp_c}', '{humidity}')")
    connection.commit()
    sys.stdout.write(f"temperature: {temp_c}*C\n")
    sys.stdout.write(f"humidity:    {humidity}%\n")
    time.sleep(30)
