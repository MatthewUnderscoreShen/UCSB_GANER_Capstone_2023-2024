from pyrplidar import PyRPlidar

print("Starting Test")

lidar = PyRPlidar()
print("Attempting Connection")
lidar.connect(port="/dev/ttyUSB3", baudrate=256000, timeout=3)
print("Attempt Complete")

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

print("Disconnecting")
lidar.disconnect()