import requests
import json
import datetime
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QPixmap

def search():
    day_list = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
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
        
        weather = response.text.split(',')[2].split(':')[1].strip()
        weather = [char for char in weather if char not in ('"', "'")]
        weather = ''.join(weather)
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

        temp = response.text.split(',')[0].split(':')[1].strip()
        temp = [char for char in temp if char not in ('"', "'")]
        temp = ''.join(temp)
        

        wind = response.text.split(',')[1].split(':')[1].strip()
        wind = [char for char in wind if char not in ('"', "'", "]", "}")]
        wind = ''.join(wind)

        window.lbl_today.setText(f"Temperature : {temp}\nWind : {wind}")

        today = datetime.date.today()
        day1 = today + datetime.timedelta(days=1)
        day1 = day1.strftime("%A")
        day2 = today + datetime.timedelta(days=2)
        day2 = day2.strftime("%A")
        day3 = today + datetime.timedelta(days=3)
        day3 = day3.strftime("%A")


        day1_temp = response.text.split(',')[4].split(':')[1].strip()
        day1_temp = [char for char in day1_temp if char not in ('"', "'","]")]
        day1_temp = ''.join(day1_temp)
        day1_wind = response.text.split(',')[5].split(':')[1].strip()
        day1_wind = [char for char in day1_wind if char not in ('"', "'", "]", "}")]
        day1_wind = ''.join(day1_wind)
        window.lbl_day1.setText(f"{day1}\n\n Temperature : {day1_temp}\n Wind : {day1_wind}")


        day2_temp = response.text.split(',')[7].split(':')[1].strip()
        day2_temp = [char for char in day2_temp if char not in ('"', "'")]
        day2_temp = ''.join(day2_temp)
        day2_wind = response.text.split(',')[8].split(':')[1].strip()
        day2_wind = [char for char in day2_wind if char not in ('"', "'", "]", "}")]
        day2_wind = ''.join(day2_wind)
        window.lbl_day2.setText(f"{day2}\n\n Temperature : {day2_temp}\n Wind : {day2_wind}")


        day3_temp = response.text.split(',')[10].split(':')[1].strip()
        day3_temp = [char for char in day3_temp if char not in ('"', "'")]
        day3_temp = ''.join(day3_temp)
        day3_wind = response.text.split(',')[11].split(':')[1].strip()
        day3_wind = [char for char in day3_wind if char not in ('"', "'", "]", "}")]
        day3_wind = ''.join(day3_wind)
        window.lbl_day3.setText(f"{day3}\n\n Temperature : {day3_temp}\n Wind : {day3_wind}")






QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication([])
loader = QUiLoader()
window = loader.load("main.ui")
window.show()

window.btn_search.clicked.connect(search)

app.exec()