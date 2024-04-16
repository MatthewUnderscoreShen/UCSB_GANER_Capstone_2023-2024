import serial # Serial Communication with Arduino for Camera (Pixy2)
import numpy as np


class Pixy2_Camera():
    def __init__(self,serial_port):
        # Define Serial Port Location
        self.serial_port = serial_port
        # Create Serial Object
        self.ser = serial.Serial(serial_port, 115200, timeout=0.1)
        self.serial_array_size = 15

    def sig(self):
        arr_location = 3 # x is the 5th element in the array once converted
        arr = np.array([0]) # establish empty array
        while len(arr) < self.serial_array_size: # Wait for useful data
            # Read Camera input from Arduino # Decode Serial # Split string into array
            arr = self.ser.readline().decode('utf-8').split()
            if len(arr) == 0:arr = [-1];arr_location = 0;break # if no object is detected --> return -1
        return int(arr[arr_location])

    def x_coord(self):
        arr_location = 5 # x is the 5th element in the array once converted
        arr = np.array([0]) # establish empty array
        while len(arr) < self.serial_array_size: # Wait for useful data
            # Read Camera input from Arduino # Decode Serial # Split string into array
            arr = self.ser.readline().decode('utf-8').split()
            if len(arr) == 0:arr = [-1];arr_location = 0;break # if no object is detected --> return -1
        return int(arr[arr_location])

    def y_coord(self):
        arr_location = 7 # y is the 7th element in the array once converted
        arr = np.array([0]) # establish empty array
        while len(arr) < self.serial_array_size: # Wait for useful data
            # Read Camera input from Arduino # Decode Serial # Split string into array
            arr = self.ser.readline().decode('utf-8').split()
            if len(arr) == 0:arr = [-1];arr_location = 0;break # if no object is detected --> return -1
        return int(arr[arr_location])

    def width(self):
        arr_location = 9 # width is the 9th element in the array once converted
        arr = np.array([0]) # establish empty array
        while len(arr) < self.serial_array_size: # Wait for useful data
            # Read Camera input from Arduino # Decode Serial # Split string into array
            arr = self.ser.readline().decode('utf-8').split()
            if len(arr) == 0:arr = [-1];arr_location = 0;break # if no object is detected --> return -1
        return int(arr[arr_location])

    def height(self):
        arr_location = 11 # height is the 11th element in the array once converted
        arr = np.array([0]) # establish empty array
        while len(arr) < self.serial_array_size: # Wait for useful data
            # Read Camera input from Arduino # Decode Serial # Split string into array
            arr = self.ser.readline().decode('utf-8').split()
            if len(arr) == 0:arr = [-1];arr_location = 0;break # if no object is detected --> return -1
        return int(arr[arr_location])