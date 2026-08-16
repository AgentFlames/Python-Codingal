from abc import ABC,abstractmethod

class Smartdevice(ABC): 
    def show_device(self,device_name):
        print(f"Device: {device_name}")

    @abstractmethod
    def turn_on():
        pass

class smart_light(Smartdevice):
    def turn_on(self):
        print("Smart light is now ON")
    

class smart_fan(Smartdevice):
    def turn_on(self):
        print("Smart fan is now ON")

class smart_speaker(Smartdevice):
    def turn_on(self):
        print("Smart speaker is now ON")

light = smart_light()
fan = smart_fan()
speaker = smart_speaker()

light.show_device("Kitchen light")
light.turn_on()

fan.show_device("Bedroom Fan")
fan.turn_on()

speaker.show_device("Jack's Speaker")
speaker.turn_on()

class security_camera: 
    def check_status(self): 
        print("security cameras are recording")

class door_lock: 
    def check_status(self): 
        print("doot is locked")
    
house_list = [security_camera(),door_lock()]
print("\n--------------- house status ---------------- \n")
for i in house_list: 
    i.check_status()

print("\n", "-"*20)

