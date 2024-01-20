import setup_path
import airsim
from datetime import datetime
import cv2
import numpy as np
import os
import tempfile

'''
Simple script with settings to create a high-resolution camera, and fetching it

Settings used-
{
    "SettingsVersion": 1.2,
    "SimMode": "Multirotor",
    "Vehicles" : {
        "Drone1" : {
            "VehicleType" : "SimpleFlight",
            "AutoCreate" : true,
            "Cameras" : {
                "high_res": {
                    "CaptureSettings" : [
                        {
                            "ImageType" : 0,
                            "Width" : 4320,
                            "Height" : 2160
                        }
                    ],
                    "X": 0.50, "Y": 0.00, "Z": 0.10,
                    "Pitch": 0.0, "Roll": 0.0, "Yaw": 0.0
                },
                "low_res": {
                    "CaptureSettings" : [
                        {
                            "ImageType" : 0,
                            "Width" : 256,
                            "Height" : 144
                        }
                    ],
                    "X": 0.50, "Y": 0.00, "Z": 0.10,
                    "Pitch": 0.0, "Roll": 0.0, "Yaw": 0.0
                }
            }
        }
    }
}
'''

client = airsim.VehicleClient()
client.confirmConnection()
framecounter = 1

prevtimestamp = datetime.now()

while(True):
    if framecounter%30 == 0:
        responses1 = client.simGetImages([
            airsim.ImageRequest("4", airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGB array
        # print('Drone1: Retrieved images: %d' % len(responses1))
        responses2 = client.simGetImages([
            airsim.ImageRequest("3", airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGB array
        # print('Drone1: Retrieved images: %d' % len(responses2))

        tmp_dir1 = os.path.join(tempfile.gettempdir(), "airsim_drone", "Camera 4")
        tmp_dir2 = os.path.join(tempfile.gettempdir(), "airsim_drone", "Camera 3")

        print ("Saving images to %s and %s" % (tmp_dir1, tmp_dir2))
        try:
            os.makedirs(tmp_dir1)
            os.makedirs(tmp_dir2)

        except OSError:
            if not os.path.isdir(tmp_dir1):
                raise
            if not os.path.isdir(tmp_dir2):
                raise

        for idx, response in enumerate(responses1):

            filename = os.path.join(tmp_dir1, str(framecounter))

            if response.pixels_as_float:
                print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
                airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
            elif response.compress: #png format
                print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
            else: #uncompressed array
                # print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
                img_rgb = img1d.reshape(response.height, response.width, 3) #reshape array to 3 channel image array H X W X 3
                cv2.imwrite(os.path.normpath(filename + '.png'), img_rgb) # write to png

        for idx, response in enumerate(responses2):

            filename = os.path.join(tmp_dir2, str(framecounter))

            if response.pixels_as_float:
                print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
                airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
            elif response.compress: #png format
                print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
            else: #uncompressed array
                # print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
                img_rgb = img1d.reshape(response.height, response.width, 3) #reshape array to 3 channel image array H X W X 3
                cv2.imwrite(os.path.normpath(filename + '.png'), img_rgb) # write to png

    framecounter += 1
