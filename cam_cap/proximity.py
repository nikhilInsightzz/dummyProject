import time
import sys, select, os
import serial
import datetime

try:
    ser = serial.Serial('/dev/ttyACM0',9600,timeout = 1)
    time.sleep(3)
except:
    try:
        ser = serial.Serial('/dev/ttyACM1',9600,timeout = 1)
        time.sleep(3)
    except:
        try:
            ser = serial.Serial('/dev/ttyACM2',9600,timeout = 1)
            time.sleep(3)
        except Exception as e:
            try:
                ser = serial.Serial('/dev/ttyACM3',9600,timeout = 1)
                time.sleep(3)
            except Exception as e:
                try:
                    ser = serial.Serial('/dev/ttyACM4',9600,timeout = 1)
                    time.sleep(3)
                except Exception as e:
                    print("Ardiuno Error :"+str(e))

while True:
    #====== pressing enter will break loop ===========#
#    os.system('cls' if os.name == 'nt' else 'clear')
    # if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
    #     line = raw_input()
    #     break
    try:
        #=========== For machine input =========#
        try:
            ard_value = int(ser.readline())
            print(ard_value)
            print(type(ard_value))
        except:
            print("no value")

    except:
        try:
            ser = serial.Serial('/dev/ttyACM0',9600,timeout = 1)
            time.sleep(3)
        except:
            try:
                ser = serial.Serial('/dev/ttyACM1',9600,timeout = 1)
                time.sleep(3)
            except:
                try:
                    ser = serial.Serial('/dev/ttyACM2',9600,timeout = 1)
                    time.sleep(3)
                except Exception as e:
                    try:
                        ser = serial.Serial('/dev/ttyACM3',9600,timeout = 1)
                        time.sleep(3)
                    except Exception as e:
                        print("Ardiuno Error :"+str(e))

