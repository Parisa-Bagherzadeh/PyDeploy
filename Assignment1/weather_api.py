import requests
import json
import datetime
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QPixmap

def search():
    
    url = "https://goweather.herokuapp.com/weather"
    city = window.search_box.text()
   

    try:
        response = requests.get(f"{url}/{city}")
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error occurred: {errh}")  
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")    
    else:
   
        print(json.loads(response.text)) 
        weather = json.loads(response.text)['description']
       
        if weather == "Partly cloudy":
            image = QPixmap("icons/partly_cloudy.png")
            window.lbl_icon.setPixmap(image)
        elif weather == "Thunderstorm":
            image = QPixmap("icons/thunderstorm.png")
            window.lbl_icon.setPixmap(image)
        elif weather == "Clear":
            image = QPixmap("icons/clear.png")
            window.lbl_icon.setPixmap(image)  
        elif weather == "Light rain":
            image = QPixmap("icons/light_rain.png")
            window.lbl_icon.setPixmap(image) 

        temp = json.loads(response.text)['temperature']
        wind = json.loads(response.text)['wind']
        window.lbl_today.setText(f"Temperature : {temp}\nWind : {wind}")

        today = datetime.date.today()
        day1 = today + datetime.timedelta(days=1)
        day1 = day1.strftime("%A")
        day2 = today + datetime.timedelta(days=2)
        day2 = day2.strftime("%A")
        day3 = today + datetime.timedelta(days=3)
        day3 = day3.strftime("%A")

        forecast = json.loads(response.text)['forecast']

        day1_temp = forecast[0]['temperature']
        day1_wind = forecast[0]['wind']
        window.lbl_day1.setText(f"{day1}\n\n Temperature : {day1_temp}\n Wind : {day1_wind}")


        day2_temp = forecast[1]['temperature']
        day2_wind = forecast[1]['wind']
        window.lbl_day2.setText(f"{day2}\n\n Temperature : {day2_temp}\n Wind : {day2_wind}")


        day3_temp = forecast[2]['temperature']
        day3_wind = forecast[2]['wind']
        window.lbl_day3.setText(f"{day3}\n\n Temperature : {day3_temp}\n Wind : {day3_wind}")


QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication([])
loader = QUiLoader()
window = loader.load("main.ui")
window.show()

window.btn_search.clicked.connect(search)

app.exec()