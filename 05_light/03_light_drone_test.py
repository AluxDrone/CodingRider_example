from time import sleep

from CodingRider.drone import *
from CodingRider.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    drone.sendLightModeColor(LightModeDrone.BodyHold, 200, 0, 200, 200)
    sleep(1)


    # sendLightModeColor*
    drone.sendLightModeColor(LightModeDrone.BodyDimming, 3, 0, 0, 200)
    sleep(3)
    
    # sendLightEventColor*
    drone.sendLightEventColor(LightModeDrone.BodyDimming, 3, 5, 200, 200, 200)
    sleep(3)
    

    drone.close()