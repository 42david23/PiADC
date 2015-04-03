#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import pygame,sys
import math
#ADW_PTR7.py
# Programmlisting vom  November 2013
# Es laesst sich sicher teilweise noch vereinfachen. 
 
#GPIO-Pins,die mit dem TLC549 verbunden sind
AD_Dat  = 24  # 
AD_Clk = 8
AD_CS = 7   #

#GPIO-Festlegungen
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#TLC549
GPIO.setup(AD_CS,GPIO.OUT)
GPIO.setup(AD_Dat,GPIO.IN)
GPIO.setup(AD_Clk,GPIO.OUT)

def ADein():
	
    GPIO.output(AD_Clk,GPIO.LOW)# AD_Clk auf 0
    AD_res=0
    for n in range(10):
        time.sleep(0.05)        		
        GPIO.output(AD_CS,GPIO.HIGH)# AD_CS auf 1
        MSB=128
        time.sleep(0.001)
        GPIO.output(AD_CS,GPIO.LOW)# AD_CS auf 0
        time.sleep(0.0005)
        AD_Wert=0
        for z in range(8):
            if (GPIO.input(AD_Dat)):
                AD_Wert=AD_Wert+MSB 
            GPIO.output(AD_Clk,GPIO.HIGH)# AD_Clk auf 1
            time.sleep(0.0005)
            GPIO.output(AD_Clk,GPIO.LOW)# AD_Clk auf 0	 
            MSB=MSB>>1
            time.sleep(0.0005)
            Ergebnis=AD_Wert
        GPIO.output(AD_CS,GPIO.HIGH)# AD_CS auf 1    
        AD_res=AD_res+AD_Wert
    AD_res=AD_res/10
    Ergebnis=AD_res    
    return Ergebnis

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
    print("%d,%d%d V \n Original: %d") %(einer, hundertL, zehntL, Wert)    
     
GPIO.Cleanup()	
