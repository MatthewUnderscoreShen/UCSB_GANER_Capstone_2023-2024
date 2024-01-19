from pyrplidar import PyRPlidar

lidar = PyRPlidar()
lidar.connect(port="/dev/ttyUSB0", baudrate=256000, timeout=3)

info = lidar.get_info()
print("info : ", info)

health = lidar.get_health()
print("health : ", health)

samplerate = lidar.get_samplerate()
print("samplerate : ", samplerate)

scanmodes = lidar.get_scan_modes()
print("scan modes : ", scanmodes)
for scanmode in scanmodes:
    print(scanmode)

lidar.disconnect()