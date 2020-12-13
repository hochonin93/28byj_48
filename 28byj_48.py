from machine import Pin
import time
class _28byj_48:


    speed = 2


    STEPER_ROUND=512 


    ANGLE_PER_ROUND=STEPER_ROUND/360 

    def __init__(self,p1,p2,p3,p4):

        self.p1 = Pin(p1, Pin.OUT, value=0)
        self.p2 = Pin(p2, Pin.OUT, value=0)
        self.p3 = Pin(p3, Pin.OUT, value=0)
        self.p4 = Pin(p4, Pin.OUT, value=0)
    
    def Front(self):     
        self.p1.value(1)
        self.p2.value(1)
        self.p3.value(0)
        self.p4.value(0)
        time.sleep_ms(self.speed)

        self.p1.value(0)
        self.p2.value(1)
        self.p3.value(1)
        self.p4.value(0)
        time.sleep_ms(self.speed)

        self.p1.value(0)
        self.p2.value(0)
        self.p3.value(1)
        self.p4.value(1)
        time.sleep_ms(self.speed)

        self.p1.value(1)
        self.p2.value(0)
        self.p3.value(0)
        self.p4.value(1)
        time.sleep_ms(self.speed)
     
    def Back():       
        self.p1.value(1)
        self.p2.value(1)
        self.p3.value(0)
        self.p4.value(0)
        time.sleep_ms(self.speed)
         
        self.p1.value(1)
        self.p2.value(0)
        self.p3.value(0)
        self.p4.value(1)   
        time.sleep_ms(self.speed)
         
        self.p1.value(0)
        self.p2.value(0)
        self.p3.value(1)
        self.p4.value(1)
        time.sleep_ms(self.speed)
     
        self.p1.value(0)
        self.p2.value(1)
        self.p3.value(1)
        self.p4.value(0)
        time.sleep_ms(self.speed)
 
 
    def Stop(self):
        self.p1.value(0)
        self.p2.value(0)
        self.p3.value(0)
        self.p4.value(0)
         
    def Run(self,angle):
        #print(angle)
        val=self.ANGLE_PER_ROUND*abs(angle)
        if(angle>0):
            for i in range(0,val):
                self.Front()
        else:
            for i in range(0,val):
                self.Back()
        angle = 0
        self.Stop()

