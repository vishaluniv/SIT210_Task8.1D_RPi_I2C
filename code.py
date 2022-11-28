##add libraries: time and smbus. Time is essentially used for using the sleep function, inorder to put a delay in code
##smbus is used to carry out the I2C communication
import time
import smbus
##sensor's default address is 0x23
SENSOR = 0X23
##one time low res mode has the register address: 0x23
ONE_TIME_LOW_RES_MODE = 0X23
##Creating a new instance of smbus, port is set: 1
bus=smbus.SMBus(1)

##new function named sense is defined
##this function is responsible to retrieve the data at register-one time low res mode, i.e., 0x23, of the sensor attached at 0x23 address; in the I2C communication line.

def sense():
    data = bus.read_i2c_block_data(SENSOR,ONE_TIME_LOW_RES_MODE)
    ##sensor's two bit value is converted into a decimal value using the following formula and then returned
    return ((data[1] + (256*data[0]))/1.2)

##as per the sensor values - the terminal output is changed
##this is an infinite loop
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



    


