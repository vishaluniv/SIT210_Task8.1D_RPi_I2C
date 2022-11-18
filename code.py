import time
import smbus

SENSOR = 0X23

ONE_TIME_LOW_RES_MODE = 0X23

bus=smbus.SMBus(1)

def sense():
    data = bus.read_i2c_block_data(SENSOR,ONE_TIME_LOW_RES_MODE)
    return ((data[1] + (256*data[0]))/1.2)


while True:
    light=sense()
    print("Light intensity: " + str(light))
    if(light>=500):
        print("Too Bright")
    elif(200<light<500):
        print("Bright")
    elif(50<light<200):
        print("Medium")
    elif(20<light<50):
        print("Dark")
    else:
        print("Too Dark")
    time.sleep(1)



    


