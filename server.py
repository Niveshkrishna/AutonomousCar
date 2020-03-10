import bluetooth
import time

target_name = None
target_address = None
port =1

print("Searching for devices...")
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices()
#Run through all the devices found and list their name
num = 0
print ("Select your device by entering its coresponding number...")
print(nearby_devices)
for i in nearby_devices:
	num+=1
	print (num , ": " , bluetooth.lookup_name( i ))

#Allow the user to select their Arduino
#bluetooth module. They must have paired
#it before hand.
if nearby_devices == []:
    print("No devices found, exiting...!")
    exit()
selection = int(input("> ")) - 1
target_name = bluetooth.lookup_name(nearby_devices[selection])
print ("You have selected", target_name)
bd_addr = nearby_devices[selection]


for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bd_addr ):
        target_address = bdaddr
        break

if target_address is not None:
    print ("found target bluetooth device with address ", target_address)
else:
    print ("could not find target bluetooth device nearby")
    exit()
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM) 
s.connect((target_address,port)) 
s.send("HELLO")

time.sleep(10)
s.close()