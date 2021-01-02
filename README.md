# Robotic Manipulation

* The REALRobot environment is a standard gym environment.
It includes a 7 DOF Kuka arm with a 2 DOF gripper, a table with 3 objects on it and a cameralooking at the table from the top.

* The gripper has four touch sensors on the inner parts of its links.

#### Action

* The action attribute of env.step must be a vector of 9 joint position in radians. The first 7 joints have a range between -pi/2 to pi/2.

* The two gripper joints have a range between 0 and pi/2.

#### Observation

The observation object returned by env.step is a dictionary:
* obs["joint_position"] is a vector containing the current angles of the 9 joints
* obs["touch_sensors"] is a vector containing the current touch intensity at the four touch sensors.
* obs["retina"] is a 240*320*3 array with the current top camera image
* obs["goal"] is a 240*240*3 array with the target top camera image

#### Reward

The reward is always put to 0.

#### Done

The done value returned is set to true only when an intrinsic or estrinsic phase is concluded.

### Intrinsic and extrinsic phase

* The environment is set to run as an "intrinsic phase" for a certain number of timesteps (env.intrinsic_timesteps , default 15M).
* During the intrinsic phase, no goal is observed.

* After env.intrinsic_timesteps have passed the intrinsic phase ends (done is set to True).

* When using real_robots.evaluate, after the intrinsic phase ends, a number of extrinsic trials will be run.

* Each extrinsic trial lasts env.extrinsic_timesteps (default: 10000).

* During each extrinsic trial, a different goal is set and it will be displayed in the observation.

* Each goal consists in moving the objects from a certain starting position to another position on the table.

* The goal observation shows how the objects should appear when reaching the final position.

* At the end of each extrinsic trial, real_robots.evaluate calls env.evaluateGoal to score that goal achievement.

* Goals are loaded from an external goal dataset file (which can be chosen using env.set_goals_dataset_path).

* A new goal dataset can be generated using the real-robots-generate-goals utility.
