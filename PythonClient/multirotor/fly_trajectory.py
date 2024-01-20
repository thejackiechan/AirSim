import setup_path 
import airsim
import cv2
import numpy as np
import os
import pprint
import tempfile

# Use below in settings.json with Blocks environment
"""
{
	"SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/main/docs/settings.md",
	"SettingsVersion": 1.2,
	"SimMode": "Multirotor",
	"ClockSpeed": 1,
	
	"Vehicles": {
		"Drone1": {
		  "VehicleType": "SimpleFlight",
		  "X": 4, "Y": 0, "Z": -2
		},
		"Drone2": {
		  "VehicleType": "SimpleFlight",
		  "X": 8, "Y": 0, "Z": -2
		}

    }
}
"""

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

client.takeoffAsync().join()
client.hoverAsync().join()

client.moveToPositionAsync(-5, 25, -10, 2).join() # modify this

# or use this
# result = client.moveOnPathAsync([airsim.Vector3r(125,0,z),
#                                 airsim.Vector3r(125,-130,z),
#                                 airsim.Vector3r(0,-130,z),
#                                 airsim.Vector3r(0,0,z)],
#                         12, 120,
#                         airsim.DrivetrainType.ForwardOnly, airsim.YawMode(False,0), 20, 1).join()


z = 3
client.moveToZAsync(-z, 2).join()
client.hoverAsync().join()
client.landAsync().join()

airsim.wait_key('Press any key to reset to original state')

client.armDisarm(False)
client.reset()

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)


