# E-Puck Robot Simulation in Webots software

E-Puck Robot Simulation in Webots software

## Project Structure

```
four_wheel_robot/
├── controllers/
│   └── wall_follower/
│       └── wall_follower.py     # Wall follower controller
├── libraries/
│                               # Additional libraries
├── worlds/
│   └── four_wheel_robot_world.wbt  # Robot world simulation
├── image/
│   └── Readme/
│       └── e-puck-world.png
└── Readme.md
```

## Requirements

- [Webots](https://www.cyberbotics.com/) (2023 or later recommended)

## Running the Simulation

1. Open Webots
2. Open the world file: `worlds/four_wheel_robot_world.wbt`
3. Run the simulation using the play button

## Controller

The project includes a wall follower controller in `controllers/wall_follower/wall_follower.py`.

To customize the controller:

1. Edit `controllers/wall_follower/wall_follower.py`
2. Add sensor reading and actuator control logic
3. The controller template provides access to:
   - `Robot` class for robot instance
   - `timestep` for simulation time step

Example sensor/actuator usage:

```python
from controller import Robot, Motor, DistanceSensor

# Get device instances
motor = robot.getDevice('motor_name')
ds = robot.getDevice('ds_name')
ds.enable(timestep)

# In main loop
value = ds.getValue()
motor.setPosition(10.0)
```

## License

MIT
