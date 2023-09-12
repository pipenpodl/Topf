import sys
from PyQt5 import QtWidgets
from topf import Ui_Topf
from time import sleep
import RPi.GPIO as GPIO
from threading import Thread
from adafruit_sht31d import SHT31D
import board
import settings
import pump
from led import led_off
from datetime import datetime, time


i2c = board.I2C()
sensor = SHT31D(i2c)


GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(5, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(6, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)


read_d = settings.read_data()

light_start = read_d['light_start']
light_end = read_d['light_end']

auto_check = read_d['auto_check']

pump_work = int(read_d['pump_work'])
pump_count_day = int(read_d['pump_count_day'])
pump_count_night = int(read_d['pump_count_night'])

count = int(read_d['count'])
led_regim = int(read_d['led_regim'])
days = int(read_d["days"])

start_pump = "10:00"
end_pump = "20:00"

is_day = True
tumb = True 


def led_on():
    global led_regim
    
    while True:
        led_off(led_regim)
        sleep(1)
    
    
def loop_time():
    while True:
        application.time_date()
        sleep(1)


def loop_button():
    global light_start, light_end, auto_check, count, is_day
    global start_pump, end_pump, tumb, days
    
    count = 0
    
    if auto_check:
        application.topf.toolButton_3.setChecked(1)
    
    else: 
        application.topf.toolButton_3.setChecked(0)  
                
    while True:
        # Режим светодиодов

        if application.state_button()[2] == 1:
            application.topf.toolButton_4.setDisabled(1)
            application.topf.toolButton_2.setDisabled(1)
            application.topf.lineEdit.setDisabled(0)
            application.topf.lineEdit_2.setDisabled(0)
            application.topf.lineEdit_3.setDisabled(0)
            application.topf.lineEdit_4.setDisabled(0)
            auto_check = True
            
        else:
            application.topf.toolButton_4.setDisabled(0)
            application.topf.toolButton_2.setDisabled(0)
            application.topf.lineEdit.setDisabled(1)
            application.topf.lineEdit_2.setDisabled(1)
            application.topf.lineEdit_3.setDisabled(1)
            application.topf.lineEdit_4.setDisabled(1)
            auto_check = False
                
        
        if not auto_check:
             #Управление реле
            if application.state_button()[0] == 1:
                GPIO.output(20, GPIO.LOW)
            
            else:
                GPIO.output(20, GPIO.HIGH)
                
                
            if application.state_button()[1] == 1:
                GPIO.output(21, GPIO.LOW)
            
            else:
                GPIO.output(21, GPIO.HIGH) 
                 
        else:
            #Управление работой ламп 
            try:
                if datetime.strptime(light_start, "%H:%M").time() < datetime.now().time() < datetime.strptime(light_end, "%H:%M").time():
                    GPIO.output(20, GPIO.LOW)
                    is_day = True
                
                else:
                    GPIO.output(20, GPIO.HIGH) 
                    is_day = False
                    
            except:
                pass
                GPIO.output(20, GPIO.HIGH) 
                
                
            if is_day:
                time_list = pump.check_pump(light_start, light_end, pump_count_day, pump_work, is_day)
                if tumb:
                    count = 0 
                    tumb = False
                
            else:  
                time_list = pump.check_pump(light_start, light_end, pump_count_night + 1, pump_work, is_day)
                del time_list[0]
                if not tumb:
                    count = 0
                     
                    # дни
                    days += 1
                    application.topf.lineEdit_5.setText(str(days))
                    
                    tumb = True    
                      
            #работа насоса
            try:
                if time_list[count][0] < datetime.now() < time_list[count][1]:
                    GPIO.output(21, GPIO.LOW)
        
                else:
                    if time_list[count][1] < datetime.now() and len(time_list) > (count + 1):
                        count += 1 
                    GPIO.output(21, GPIO.HIGH) 
                
                start_pump = str(time_list[count][0])[11:16]
                end_pump = str(time_list[count][1])[11:16]   
                
            except:
                print("ошибка насоса")    
                GPIO.output(21, GPIO.HIGH)
                count = 0    
                
        sleep(0.1)
                
def loop():
    global count, led_regim, light_start, light_end, pump_work, pump_count_day, pump_count_night, days
    
    while True:
        application.set_state()
        temperature = sensor.temperature
        humidity = sensor.relative_humidity
        application.change_sensor(temperature, humidity)
        application.topf.label_18.setText("Прошло дней: " + str(days))
        save = {
            "light_start": light_start,
            "light_end":light_end,
            "auto_check": str(auto_check),
            "pump_work": int(pump_work),
            "pump_count_day": int(pump_count_day),
            "pump_count_night": int(pump_count_night),
            "count": count,
            "led_regim": led_regim,
            "days": days
        }
        settings.write_data(save)
        
        sleep(10)        


class Topf(QtWidgets.QMainWindow):
    def __init__(self):
        super(Topf, self).__init__()
        self.setWindowOpacity(0.6)
        self.topf = Ui_Topf()
        self.topf.setupUi(self)
        self.init_ui()
        self.save()
        self.next_page()
        self.next_page_main()
      
        
    def init_ui(self):
        self.topf.lineEdit.setText(light_start)
        self.topf.lineEdit_2.setText(light_end)
        self.topf.lineEdit_3.setText(str(pump_count_day) + '-' + str(pump_count_night))
        self.topf.lineEdit_4.setText(str(pump_work))
        self.topf.lineEdit_5.setText(str(days))
        self.topf.stackedWidget.setCurrentIndex(0)
        
        
    def time_date(self):
        self.topf.label_3.setText(datetime.now().strftime("%I:%M:%S")) 
        self.topf.label_15.setText(datetime.now().strftime("%d %B")) 
    
    
    def next_page(self):  
        self.topf.pushButton_3.clicked.connect(self.page_1) 
         
    def next_page_main(self):  
        self.topf.pushButton.clicked.connect(self.page_0) 
    
    def page_1(self):
        self.topf.stackedWidget.setCurrentIndex(1)
        
    def page_0(self): 
        self.topf.stackedWidget.setCurrentIndex(0)   
            
        
    def change_sensor(self, temperature, humidity):
        self.topf.label_2.setText(str(round(temperature, 1)) + " °C")  
        self.topf.label.setText(str(round(humidity, 1)) + " %")  

    
    def set_state(self):
        self.topf.label_4.setText("Свет: " + str(light_start) + ' - ' + str(light_end))
        self.topf.label_12.setText("Кол-во аэраций: " + str(pump_count_day)) 
        self.topf.label_13.setText("Аэрации: " + start_pump + ' - ' + end_pump)  
        
        
    def state_button(self):
        return self.topf.toolButton_2.isChecked(), self.topf.toolButton_4.isChecked(), self.topf.toolButton_3.isChecked(),
    
    
    def save(self):
        self.topf.pushButton_2.clicked.connect(self.get_data)
        
    
    def get_data(self):
        global light_start, light_end, pump_count_day, pump_count_night, pump_work, days
        
        try:
            days = int(self.topf.lineEdit_5.text())
            light_start = self.topf.lineEdit.text()
            light_end = self.topf.lineEdit_2.text()
            pump_count_day = int(self.topf.lineEdit_3.text().split('-')[0])
            pump_count_night = int(self.topf.lineEdit_3.text().split('-')[1])
            pump_work = int(self.topf.lineEdit_4.text())

        except:
            light_start = "06:00"
            light_end = "23:00"
            pump_count_day = 3
            pump_count_night = 1
            pump_work = 10
            days = 0
                

def start():
    cycle = Thread(target=loop, daemon=True)
    cycle_two = Thread(target=loop_time, daemon=True)
    cycle_three = Thread(target=loop_button, daemon=True)
    cycle_four = Thread(target=led_on, daemon=True)
    cycle.start()
    cycle_two.start()
    cycle_three.start()
    cycle_four.start()
    application.show()
    app.exec()         


app = QtWidgets.QApplication([])
application  = Topf()          
        
if __name__ == "__main__":
    start()
       