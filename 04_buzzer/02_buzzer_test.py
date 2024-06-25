from time import sleep

from CodingRider.drone import *
from CodingRider.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    
    drone.sendBuzzer(BuzzerMode.MuteInstantly, BuzzerScale.Mute.value, 100)
    sleep(0.2)
    
    drone.sendBuzzerScale(BuzzerScale.G4, 300)     
    sleep(0.4)
    drone.sendBuzzerScale(BuzzerScale.G4, 300)     
    sleep(0.4)
    drone.sendBuzzerScale(BuzzerScale.A4, 300)     
    sleep(0.4)
    drone.sendBuzzerScale(BuzzerScale.A4, 300)     
    sleep(0.4)
    drone.sendBuzzerScale(BuzzerScale.G4, 300)     
    sleep(0.4)
    drone.sendBuzzerScale(BuzzerScale.G4, 300)     
    sleep(0.4)
    drone.sendBuzzerScale(BuzzerScale.E4, 300)     
    sleep(0.4)

    drone.close()