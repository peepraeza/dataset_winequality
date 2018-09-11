import serial
import time
import requests
import json
firebase_url = 'https://data-log-fb39d.firebaseio.com/'
#Connect to Serial Port for communication
ser = serial.Serial('COM5', 9600, timeout=0)
#Setup a loop to send Temperature values at fixed intervals
#in seconds
fixed_interval = 5
while 1:
  try:
    #temperature value obtained from Arduino + LM35 Temp Sensor          
    read = ser.readline()
    data = read.decode("utf-8").split(" ")

    power = data[0]
    current = data[1]
    time_now = datetime.datetime.now()
    #current time and date
    # time_hhmmss = time.strftime('%H:%M:%S')
    # date_mmddyyyy = time.strftime('%d/%m/%Y')
    
    #current location name
    data_location = 'My-Dorm';
    print(time_now + ',' + power + ',' + current)
    
    #insert record
    data = {'time':time_now,'power':power,'current':current}
    result = requests.post(firebase_url + '/' + data_location + '/data.json', data=json.dumps(data))
    
    print('Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text)
    time.sleep(fixed_interval)
  except IOError:
    print('Error! Something went wrong.')
  time.sleep(fixed_interval)