"""wall_follower controller."""

from controller import Robot

def run_robot(robot):

    timestep = int(robot.getBasicTimeStep())

    max_speed = 6.28
    THRESHOLD = 80

    # Correct motor initialization
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')

    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))

    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    # Proximity sensors
    proxy_sensors = []

    for i in range(8):
        sensor_name = 'ps' + str(i)
        sensor = robot.getDevice(sensor_name)
        sensor.enable(timestep)
        proxy_sensors.append(sensor)

    while robot.step(timestep) != -1:

        sensor_values = [sensor.getValue() for sensor in proxy_sensors]

        left_wall = sensor_values[5] > THRESHOLD
        front_wall = sensor_values[7] > THRESHOLD

        left_speed = max_speed
        right_speed = max_speed


        if front_wall:
            print("Turn right")
            left_speed = max_speed
            right_speed = -max_speed

        elif not left_wall:
            print("Turn left")
            left_speed = max_speed * 0.5
            right_speed = max_speed

        else:
            print("Follow wall")

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)


if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)