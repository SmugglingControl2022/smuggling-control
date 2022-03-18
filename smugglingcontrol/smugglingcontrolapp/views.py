from django.shortcuts import render
import pyrebase
import time
from django.http import HttpResponse
import time
from datetime import datetime
from datetime import timedelta

def about_view(request):
    return render(request,'about.html')

def view_name(request):
    return render(request, 'template_name.html', {})
# todayDate = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
# print(todayDate)

  # Smuggling Control in forest
  # 'apiKey': "AIzaSyBwWyWzNy42nCdsWhO6GFezby3CMIamWOo",
  # 'authDomain': "smuggling-control-in-forest.firebaseapp.com",
  # 'databaseURL': "https://smuggling-control-in-forest-default-rtdb.firebaseio.com",
  # 'projectId': "smuggling-control-in-forest",
  # 'storageBucket': "smuggling-control-in-forest.appspot.com",
  # 'messagingSenderId': "523031324484",
  # 'appId': "1:523031324484:web:91b3bbae7fe1558fca5911",
  # 'measurementId': "G-K0N27MY318"

# Test case
# firebaseConfig = {
#   'apiKey': "AIzaSyAJlvRSHozj6lQDExnrWQLZCgxmc6TG3JA",
#   'authDomain': "test1-5515f.firebaseapp.com",
#   'databaseURL': "https://test1-5515f-default-rtdb.firebaseio.com",
#   'projectId': "test1-5515f",
#   'storageBucket': "test1-5515f.appspot.com",
#   'messagingSenderId': "884241588022",
#   'appId': "1:884241588022:web:3913c0e658cc78a49c1d97",
#   'measurementId': "G-VQWCQP0WRF"
#   }

# Real Time
firebaseConfig = {
  "apiKey": "AIzaSyB0MBpt8PPSp7LTwKm_Q-yBMg-UIiDs0hU",
  "authDomain": "realtimedata-2024d.firebaseapp.com",
  "databaseURL": "https://realtimedata-2024d-default-rtdb.firebaseio.com",
  "projectId": "realtimedata-2024d",
  "storageBucket": "realtimedata-2024d.appspot.com",
  "messagingSenderId": "506837837067",
  "appId": "1:506837837067:web:bb4557d3ae582bcbc3ee0e",
  "measurementId": "G-E57ZXBXV02"
}

# firebaseConfig = {
#   'apiKey': "AIzaSyBwWyWzNy42nCdsWhO6GFezby3CMIamWOo",
#   'authDomain': "smuggling-control-in-forest.firebaseapp.com",
#   'databaseURL': "https://smuggling-control-in-forest-default-rtdb.firebaseio.com",
#   'projectId': "smuggling-control-in-forest",
#   'storageBucket': "smuggling-control-in-forest.appspot.com",
#   'messagingSenderId': "523031324484",
#   'appId': "1:523031324484:web:91b3bbae7fe1558fca5911",
#   'measurementId': "G-K0N27MY318"

#   }


# Create your views here.
firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()



def index(request):
    IST = time.localtime()
    current_time = time.strftime("%H:%M:%S", IST)
    todayDate = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    #object_detection = database.child('Object Detection').child('person').get().val()
    object_detection = database.child('Smuggling Control Of Trees In Forest').child('CAMERA').child('DATA').get().val()  
    flame = database.child('Smuggling Control Of Trees In Forest').child('FLAME').child('DATA').get().val()  
    flex = database.child('Smuggling Control Of Trees In Forest').child('FLEX').child('DATA').get().val()  
    gpsLatitude = database.child('Smuggling Control Of Trees In Forest').child('GPS').child('LATITUDE').get().val()  
    gpsLongitude = database.child('Smuggling Control Of Trees In Forest').child('GPS').child('LONGITUDE').get().val()  
    mpuAcceleromter = database.child('Smuggling Control Of Trees In Forest').child('MPU').child('Acceleromter').get().val() 
    mpuGYROROTATION = database.child('Smuggling Control Of Trees In Forest').child('MPU').child('GYRO ROTATION').get().val() 
    mpuTEMPERATURE = database.child('Smuggling Control Of Trees In Forest').child('MPU').child('TEMPERATURE').get().val()    
    PHsensor = database.child('Smuggling Control Of Trees In Forest').child('PHsensor').child('DATA').get().val() 
    
    return render(request,'index.html',{
      "object_detection":object_detection,
      "flame":flame,
      "flex":flex,
      "gpsLatitude":gpsLatitude,
      "gpsLongitude":gpsLongitude,
      "mpuAcceleromter":mpuAcceleromter,
      "mpuGYROROTATION":mpuGYROROTATION,
      "mpuTEMPERATURE":mpuTEMPERATURE,
      "PHsensor":PHsensor,

        # "flame_sensor":flame_sensor,
        # "gps_sensor":gps_sensor,
        # "mpu_sensor":mpu_sensor,
        # "ph_sensor":ph_sensor,

        # "user_name":#user_name,
        # "user_college":user_college,
        # "flex_sensor":flex_sensor,
        # "gps_sensor":gps_sensor,
        # "mpu_sensor":mpu_sensor,
        
    }) 
    
    
    
    # user_name = database.child('Data').child('Name').get().val()
    # user_college = database.child('Data').child('college').get().val()
    # flex_sensor = database.child('Fex').child('Flex sensor').get().val()
    # gps_sensor = database.child('Gps').child('Latitude').get().val()
    # mpu_sensor = database.child('MPU').child('Acceleration').child('Ax').get().val()

    # flame_sensor = database.child('Flame sensor data').child('2022:02:27 15:59:10').get().val()
    # gps_sensor = database.child('GPS').child('GPS data latitude_in_degrees').child('2022:02:27 21:28:46').get().val()
    # mpu_sensor = database.child('MPU').child().child('Acceleration').child('2022:02:27 15:58:54').get().val()
    # ph_sensor = database.child('PHsensor').child('2022:02:27 16:04:51').get().val()