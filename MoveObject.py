import time
from Arm_Lib import Arm_Device

# Get DOFBOT object
Arm = Arm_Device()
time.sleep(0.1)

# Define positions for different actions
p_Depot = [130, 25, 66, 40, 270]
p_Pick = [90, 45, 30, 40, 270]

def arm_move(p, s_time=500):
    for i in range(5):
        id = i + 1
        if id == 5:
            Arm.Arm_serial_servo_write(id, p[i], int(s_time * 1.2))
        else:
            Arm.Arm_serial_servo_write(id, p[i], s_time)
        time.sleep(0.01)


def event_servo (params):
    for arg in params:
        Arm.Arm_serial_servo_write(arg[0], arg[1], arg[2])
        time.sleep(1)

def main():
    global Arm  # Declare Arm as a global variable

    try:
        Arm = Arm_Device()
        time.sleep(0.1)


        event_servo(
            [
                (6, 0, 1000),
                (1, 89, 1000),
                (2, 60, 1000),
                (3, 6, 1000),
                (4, 50, 1000),
                (5, 270, 1000),
                (6, 140, 1000),
                (4, 60, 1000),
                (3, 60, 1000),
                (2, 100, 1000),
                (1, 130, 1000),
                (2, 39, 1000),
                (3, 30, 1000),
                (1, 130, 1000),
                (6, 56, 1000),
                (6, 0, 1000),
            ]
        )

        for i in range(6):
            aa = Arm.Arm_serial_servo_read(i + 1)
            print(aa)
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("Program closed!")

    finally:
        if Arm is not None:
            del Arm  # Release DOFBOT object if Arm is assigned

if __name__ == "__main__":
    main()