#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Cars:
    def __init__(self):
        self.cartype = input("please enter if your car uses oil or electricity: ")
        self.__lock = int(input("please enter your car lock: "))
        self.fulltank = int(input("please enter your full tank charge or capacity: "))
        self.capacity = int(input("please enter your current tank: "))
        self.maxspeed = int(input("please enter your car max speed: "))
        self.speed = int(input("please enter your car current speed: "))
        self.newspeed = None
    
    def changespeed(self):
        self.newspeed = int(input("please enter new speed: "))
        if self.speed > self.maxspeed:
            print("this can`t be")
        if self.newspeed != self.speed:
            self.speed = self.newspeed
            print("your new speed is: ", self.speed)
        else:
            print("the new speed is same as the old speed")
            
    def openlock(self, lock):# why did we put (lock) with self just in this
        if lock == self.__lock:
            print("lock is right")
        else:
            print("please try again")
    
    def checkoil(self):
        if self.cartype == "oil":
            print("the current tank is filled with :", self.capacity)
            tofull = self.fulltank - self.capacity
            print("you need ", tofull , "for full tank")
        elif self.cartype == "electricity":
            print("the current battery is charged with :", self.capacity)
            tofull = self.fulltank - self.capacity
            print("you need ", tofull , "for full battery")
            
    def filltank(self):
        if self.cartype == "oil":
            if self.capacity == self.fulltank:
                print("sorry tank is full")
            elif self.capacity != self.fulltank:
                print("please open your tank")
                addoil = int(input("please enter the added oil: "))
                self.capacity += addoil
                print("your new capacity is: ", self.capacity)
            else:
                print("your car doesn`t support oil")
    def charge(self):
        if self.cartype == "electricity":
            if self.capacity == self.fulltank:
                print("sorry battery is full")
            elif self.capacity != self.fulltank:
                print("please open your battery")
                extracharge = int(input("please enter the added charge: "))
                self.capacity += extracharge
                print("your new capacity is: ", self.capacity)
            else:
                print("your car doesn`t support electricity")
            

    
    


# In[2]:


bmw= Cars()
bmw.openlock(123)
bmw.speed
bmw.changespeed()
bmw.filltank()
bmw.checkoil()
bmw.charge()


# In[3]:


TEsla= Cars()
TEsla.openlock(123)
TEsla.speed
TEsla.changespeed()
TEsla.filltank()
TEsla.checkoil()
TEsla.charge()


# In[ ]:




