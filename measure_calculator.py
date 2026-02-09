# Calculate body measurements from pose landmarks.

import numpy as np

from config import REFERENCE_HEIGHT_CM

class MeasurementCalculator:
   # Calculates body measurements from detected landmarks.
   def __init__(self, user_height_cm=REFERENCE_HEIGHT_CM):
       """
       Initialize calculator with user's actual height for calibration.

       Args:
            user_height_cm: User's actual height in centimeters
       """
       self.user_height_cm = user_height_cm
       self.pixels_per_cm = None

def calculate_distance(self, point1, point2):
        """
        Calculate distance between two points.

        Args:
           point1: (x, y) tuple
           point2: (x, y) tuple

        Returns:
        float: Distance in pixels
        """
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calibrate(self, landmarks):
        """
        Calibrate pixel-to-cm ratio using detected body height.

        Args:
            landmarks:Dictionary of landmark coordinates
        """
        if not landmarks:
            return False

        #Calculatebody height in pixels(nose to average ankle position)
        nose = landmarks['nose']
        left_ankle = landmarks['left_ankle']
        right_ankle = landmarks['right_ankle']

        avg_ankle = (
            (left_ankle[0] + right_ankle[0] / 2,
            (left_ankle[1] + right_ankle[1]) / 2)
        )

        body_height_pixels = self.calculate_distance(nose, avg_ankle)

        if body_height_pixels > 0:
            self.pixels_per_cm = body_height_pixels / self.user_height_cm
            return True
        return False

def calculate_measurements(self, landmarks):
        """
        Calculate body measurements from landmarks.

        Args:
        landmarks: Dictionary of landmark coordinates

        Returns:
        dict: Dictionary of measurements in centimeters
        """
        if not landmarks or self.pixels_per_cm is None:
            return None

        measurements = {}

        # Shoulder width
        shoulder_width_px = self.calculate_distance(
            landmarks['left_shoulder'],
            landmarks['right_shoulder']
        )
        measurements['shoulder_width_cm'] = shoulder_width_px / self.pixels_per_cm

        # Torso length (shoulder to hip)
        left_torso_px = self.calculate_distance(
            landmarks['left_shoulder'], # Changed from 'right_shoulder'
            landmarks['left_hip']       # Changed from 'right_hip'
        )
        right_torso_px = self.calculate_distance(
            landmarks ['right_shoulder'],
            landmarks['right_hip']
        )
        avg_torso_px = (left_torso_px + right_torso_px) / 2
        measurements['torso_length_cm'] = avg_torso_px / self.pixels_per_cm

        # Hip width
        hip_width_px = self.calculate_distance(
            landmarks['left_hip'],
            landmarks['right_hip']
        )
        measurements['hip_width_cm'] = hip_width_px / self.pixels_per_cm

        # Inseam (hip to ankle)
        left_inseam_px = self.calculate_distance(
            landmarks['left_hip'],
            landmarks['lef_ankle']
        )
        right_inseam_px = self.calculate_distance(
            landmarks['right_hip'],
            landmarks['right_ankle']
        )
        avg_inseam_px = (left_inseam_px + right_inseam_px) / 2
        measurements['inseam_cm'] = avg_inseam_px / self.pixels_per_cm

        return measurements


