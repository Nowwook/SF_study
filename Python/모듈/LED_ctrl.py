# 숫자를 2진수 형태로 LED에 표시

import RPi.GPIO as GPIO        # 라즈베리파이 보드의 GPIO 관련 모듈
import time                    # 시간 관련 모듈

GPIO.setwarnings(False)        # warning 메세지를 비활성화
GPIO.setmode(GPIO.BOARD)       # BOARD: 라즈베리파이 핀번호, BCM:브로드컴 번호

LED = [3,5,23,11,13,15,19,21]
LED_NUM = 8

for i in range(len(LED)):
    GPIO.setup(LED[i], GPIO.OUT, initial=GPIO.LOW)   # GOIO의 입출력을 설정

try:
    while True:
        # 프로그램 작성
        num = int(input("숫자를 입력하세요: "))
        print(num)
        
        bin_num = bin(num)[2:]      # '0b'를 빼낸다.
        
        while True:
            if len(bin_num) <= LED_NUM:
                bin_num = '0' + bin_num
            else:
                bin_num = bin_num[-8:]
                break
        # 2진수 리스트를 LED에 표시
        for i in range(LED_NUM):
            GPIO.output(LED[i], int(bin_num[(LED_NUM-1)-i]))
               
        print(bin_num)
        print(type(bin_num))
     
        
finally:
    GPIO.cleanup()       # GPIO에 대한 권한을 해제
    print("cleanup")
    print("finally")
