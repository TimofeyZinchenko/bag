import RPi.GPIO as GPIO # Импортирует модули времени и работы
import time
GPIO.setmode(GPIO.BCM) # Обращение ко всем GPIO пинам
led = 26 # Номер подключенного пина
GPIO.setup(led, GPIO.OUT) # Настроили как цифровой выход
pwm = GPIO.PWM(led, 200) # Объект управления ШИМ сигналом с частотой 200
duty = 0.0 # Текущий коэффициент заполения
pwm.start(duty) # Запуск генерации ШИМ - сигнала на GPIO выходе
while True:
    pwm.ChangeDutyCycle(duty) #Изменяет коэффициент заполнения
    time.sleep(0.5) # Пауза после установки коэффициента заполнения

    duty += 1.0
    if duty > 100.0:
        duty = 0 # Сбрасываем в ноль