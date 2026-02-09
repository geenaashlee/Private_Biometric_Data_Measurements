"""
Body Measurement Extraction, Demonstrating data without centralization
"""
import cv2
import time
from datetime import datetime
from posing_detection import PoseDetector
from measure_calculator import MeasurementCalculator
from config import (
    CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT,
    SHOW_LANDMARKS, SAVE_FRAMES
)
def main ():
    """
    Main application loop.

    """
    print("=" * 60)
    print("Privacy-First Body Measurement System")
    print("=" * 60)
    print("\nPRIVACY ARCHITECTURE:")
    print("Processing locally on device")
    print("Only final measurements are stored")
    print("=" * 60)

    # Receive user's height for calibration
    while True:
        try:
            user_height = float(input("\nEnter your height in centimeters(e.g., 170): "))
            if user_height > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

        # Initialize all components
        detector = PoseDetector()
        calculator = MeasurementCalculator(user_height_cm=user_height)

        # Open Webcam
        cap = cv2.VideoCapture(CAMERA_INDEX)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        if not cap.isOpened():
             print("Erro: Could not open camera.")
             return
        print("\nCamera opened successfully!")
        print("Stand in front of camera with full body visibility.")
        print("Press 'c' to calibrate,'m' to measure,'q' to 'quit.")

        calibrated = False
        frame_count = 0
        start_time = time.time()

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break
            frame_count += 1

            # Privacy demonstration: Frame is processed but never saved
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]

            # Pose detection
            results = detector.detect(frame)

            # Draw landmarks if enabled
            if SHOW_LANDMARKS:
                frame = detector.draw_landmarks(frame,results)

            # Get landmark coordinates
            landmarks = detector.get_landmark_coordinates(results, frame.shape)

            # Display privacy information on frame
            cv2.putText(frame, f"Frame {frame_count} - Processed at {timestamp}",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 0), 2)
            cv2.putText(frame, "DISCARDED (not saved)",
                        (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
            if calibrated:
                cv2.putText(frame, "Calibrated - Press 'm' to measure",
                            (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,255,0), 2)
            else:
                cv2.putText(frame, "Press 'c' to calibrate",
                            (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,255,0,0), 2)

            # Show frame
            cv2.imshow('Privacy-First Body Measurements', frame)

        print("\n" + "=" * 60)
        print("PRIVACY SUMMARY:")
        print(f" Total frames processes: {frame_count}")
        print(f" Total frames saved: 0")
        print(f" Data transmitted: 0 bytes (all processing local)")
        print(f" Session duration: {elapsed:.1f} seconds")
        print("=" * 60)

    if __name__ == "__main__":
        main()






