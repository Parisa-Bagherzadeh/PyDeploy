import requests
import json
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
        window.lbl_temp.setText("Temperature : " + temp)

        tomorrow = response.text.split(',')[4].split(':')[1].strip()
        tomorrow = [char for char in tomorrow if char not in ('"', "'")]
        tomorrow = ''.join(tomorrow)
        window.lbl_day1.setText(f"Tomorrow : {tomorrow}")


QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication([])
loader = QUiLoader()
window = loader.load("main.ui")
window.show()

window.btn_search.clicked.connect(search)

app.exec()