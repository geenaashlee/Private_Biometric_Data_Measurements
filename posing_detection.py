import cv2
import mediapipe as mp
import numpy as np
from config import MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE

class PoseDetector: # Detecting body pose landmarks from video frames.
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )

    def detect(self, frame):
        """"
        Detect pose landmarks in frame.

        Args:
            frame: BGR image from OpenCV

        Returns:
            results: Mediapipe pose detection results
            """
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = self.pose.process(image_rgb)

        return results

    def draw_landmarks(self, frame, results):
        """
        Draw pose landmarks on the frame.

        Args:
        frame: BGR image from OpenCV
        results: MediaPipe pose detection results

        Returns:
        frame: Frame with landmarks drawn
        """
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )

        return frame
    def get_landmark_coordinates(self, results, frame_shape):
        """
        Extract landmark coordinates in pixel space.

        Args:
         results: MediaPipe pose detection results
         frame_shape: Shape of the frame (height, width, channels)

         Returns:
          dict: Dictionary of landmark names to (x,y) coordinates

        """
        if not results.pose_landmarks:
            return None

        h,w = frame_shape[:2]
        landmarks = {}

        # Key landmarks for body measurements
        landmark_indices = {
            'left_shoulder': self.mp_pose.PoseLandmark.LEFT_SHOULDER,
            'right_shoulder': self.mp_pose.PoseLandmark.RIGHT_SHOULDER,
            'left_hip': self.mp_pose.PoseLandmark.LEFT_HIP,
            'right_hip': self.mp_pose.PoseLandmark.RIGHT_HIP,
            'left_knee': self.mp_pose.PoseLandmark.LEFT_KNEE,
            'right_knee': self.mp_pose.PoseLandmark.RIGHT_KNEE,
            'left_ankle': self.mp_pose.PoseLandmark.LEFT_ANKLE,
            'right_ankle':self.mp_pose.PoseLandmark.RIGHT_ANKLE,
            'nose': self.mp_pose.PoseLandmark.NOSE,
        }

        for name, idx in landmark_indices.items():
            landmark = results.pose_landmarks.landmark[idx]
            landmarks[name] = (int(landmark.x * w), int(landmark.y * h))

        return landmarks

    def close(self):
        """Release resources."""
        self.pose.close()