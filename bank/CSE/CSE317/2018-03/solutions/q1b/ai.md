---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Sensors: LIDAR (laser), cameras (mono/stereo), radar, ultrasonic (sonar), GPS, IMU/odometry. Laser gives accurate 3-D range (obstacles, free space, localization against a map) but no colour or text; cameras give colour, texture and semantics (lanes, signs, lights, pedestrians) but poor depth. Fusing them (camera classifies, LIDAR measures distance) gives safer, smoother driving."
sources: ["AIMA 4e sec. 26.2 (robot hardware: sensors) and 26.4 (localization and mapping)"]
---
**Types of sensors in an autonomous vehicle** (5 marks):

| Sensor | Measures |
|:--|:--|
| **LIDAR** (laser range finder) | 3-D point cloud: distances to surrounding objects by laser time-of-flight |
| **Cameras** (mono, stereo, surround) | colour images: lanes, traffic signs and lights, vehicles, pedestrians |
| **Radar** | range and relative speed (Doppler) of vehicles; works in rain and fog |
| **Ultrasonic** (sonar) | short-range distances, for parking |
| **GPS** | global position |
| **IMU, wheel encoders** (odometry) | acceleration, rotation, speed: dead reckoning between GPS fixes |

These are a mix of *range-finding*, *imaging* and *proprioceptive* sensors.

**Using laser and camera together** (5 marks):

- *Laser (LIDAR)* gives precise 3-D geometry, day or night. It is used for obstacle detection and free-space mapping, for measuring the distance to the car ahead (adaptive cruise control, emergency braking), and for localizing against a pre-built 3-D map (SLAM or particle filters). It cannot read colours or text.
- *Camera* gives rich appearance: lane markings, traffic-light colour, sign text, and classification of objects (a pedestrian versus a pole) with CNNs. Its depth estimates are poor, especially at long range and in poor light.
- *Sensor fusion:* project LIDAR points onto the camera image. The camera says **what** an object is, the laser says **where** it is and how far. Probabilistic fusion (Kalman or particle filters) tracks objects more reliably than either sensor alone. The result is fewer false alarms and smoother braking and steering: a safer, more comfortable ride. Redundancy also covers each sensor's weaknesses (camera glare, LIDAR in heavy rain).
