from time import sleep

from CodingRider.drone import *
from CodingRider.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    print("TakeOff")
    drone.sendTakeOff()
    sleep(0.01)

    print("Hovering")
    drone.sendControlWhile(0, 0, 0, 0, 6400)
    sleep(0.01)

    print("Throttle down")
    drone.sendControlWhile(0, 0, 0, -25, 3600)
    sleep(0.01)

    print("Stop")
    drone.sendStop()
    sleep(0.01)


    drone.close()