from time import sleep

from CodingRider.drone import *
from CodingRider.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    print("TakeOff")
    drone.sendTakeOff()
    for i in range(5, 0, -1):
        print("{0}".format(i))
        sleep(1)

    print("Hovering")
    for i in range(3, 0, -1):
        print("{0}".format(i))
        drone.sendControlWhile(0, 0, 0, 0, 1000)
        sleep(0.01)

    print("Landing")
    drone.sendLanding()
    for i in range(5, 0, -1):
        print("{0}".format(i))
        sleep(1)

    drone.close()