#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import pygame,sys
import math
 
AD_Clk = 7
AD_Dat = 8  
AD_CS = 24   


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(AD_CS,GPIO.OUT)
GPIO.setup(AD_Dat,GPIO.IN)
GPIO.setup(AD_Clk,GPIO.OUT)
GPIO.output(AD_Clk,GPIO.LOW)
GPIO.output(AD_CS,GPIO.HIGH)
time.sleep(20/10e6)
GPIO.output(AD_CS,GPIO.LOW)

def ADein():
    sample = 0
    for x in range(0,8):
        sample = sample << 1
        sample = sample + GPIO.input(AD_Dat)
        GPIO.output(AD_Clk,GPIO.HIGH)
        time.sleep(5/10e6)
        GPIO.output(AD_Clk,GPIO.LOW)
        time.sleep(5/10e6)
	
    return result

def Umrechnung(Wert):
    value=Wert
    value=value*1960 #fuer 5V  
    value=value/1000
    pic_value=value/2 #
    einer=value/100
    rest_z=value % 100
    zehntL=rest_z/10
    hundertL=rest_z%10
    return einer, zehntL, hundertL, pic_value,value
    



while True:
	
    Wert=ADein()
       
    value_tmp=Wert
       
    #Umrechnung(Wert)
    einer,zehntL,hundertL,pic_value,value=Umrechnung(Wert)
    print("Original: %d") %(Wert)    
    time.sleep(1)
     
GPIO.Cleanup()	
