# Privacy First Body Measurement Extraction

**A demonstration that biometric data processing without centralization**

## Overview

Most virtual try-on and body measurement systems require uploading full-body video to centralized servers. This prototype demonstrates that body measurements can be extracted on the user's advice,therefore proving that centralized biometric collection can be an architectural choice


## The Problem

Current virtual try-on technologies in fashion and AR/VR require users to:
1. Upload continuous video streams of their bodies to company servers
2. Trust that biometric data is handled appropriately
3. Accept that compliance frameworks (SOC2, HIPAA) audit *how* data is handled, not *whether* it should be collected at all


## This Solution

This application demonstrates local-first biometric processing:

-  Video processing happens on your device
- Pose detection runs locally using MediaPipe
- Only final measurements (numbers) are stored
- Video frames are never saved and zero server communication 


## Technical Implementation
Stack:
- Python 3.8+
- OpenCV - webcam capture and display
- MediaPipe Pose - local pose estimation
- NumPy - geometric calculations

Key Components:
1. `pose_detector.py` - Detecting body landmarks from video frames
2. `measurement_calculator.py` - Calculating measurements from landmark coordinates
3. `main.py` - Orchestrates local processing pipeline

**What makes this privacy-preserving:**
- Frames are processed in memory and immediately discarded
- No frame persistence (check the code - no `cv2.imwrite()` calls)
- No network calls (check the code - no API requests)
- Measurements only logged to console (easily extended to local file storage)

## Installation
```bash
# Clone the repository
git clone https://github.com/geenaashlee/Private_Biometric_Data_Measurements.git
cd Private_Biometric_Data_Measurements

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Usage

1. Run `python main.py`
2. Enter your height in cm when prompted (for calibration)
3. Stand in front of your webcam with your full body visible
4. Press **'c'** to calibrate (establishes pixel-to-cm ratio)
5. Press **'m'** to extract measurements
6. Press **'q'** to quit

**Example Output:**
```
[14:23:45.123] MEASUREMENTS EXTRACTED:
----------------------------------------
  shoulder_width_cm: 42.3 cm
  torso_length_cm: 58.7 cm
  hip_width_cm: 36.2 cm
  inseam_cm: 81.4 cm
----------------------------------------
NOTE: Only these measurements stored, frame discarded
```

## Current Limitations & Future Work

This is a **proof-of-concept** demonstrating feasibility, not a production system. Current limitations:

### Technical Limitations:
- **2D measurements only** - depth estimation is approximate
- **Requires good lighting** - pose detection degrades in poor conditions
- **Static calibration** - assumes user maintains distance from camera
- **No clothing/fabric consideration** - measures body, not how clothes fit

### Privacy Limitations (Why I'm Pursuing Graduate Studies):
- **Batch processing mindset** - this processes frames sequentially but doesn't address streaming privacy budgets
- **No formal privacy guarantees** - local processing reduces risk but doesn't provide differential privacy
- **Trust-based model** - users must trust the code does what it claims

### Research Questions This Raises:
1. How do we apply differential privacy to 30fps streaming biometric data?
2. Can we provide cryptographic guarantees that frames are never persisted?
3. How do we balance privacy budgets in continuous observation scenarios?
4. What are the tradeoffs between federated learning and local-only processing?

**These questions motivate my graduate research agenda in Privacy Engineering.**

## Connection to Graduate Research

This project is the foundation for my intended research in **privacy-preserving streaming biometric systems**. 

I plan to extend this work to:

1. Implement **temporal differential privacy** for streaming pose data
2. Explore **secure enclave processing** for cryptographic guarantees
3. Develop **streaming federated learning** architectures for model updates without centralization
4. Build production-ready systems that can process 30fps biometric streams with formal privacy guarantees


Geena Greene  
[GitHub](https://github.com/geenaashlee) | [LinkedIn](https://www.linkedin.com/in/geena-greene/)

---

**Note to Reviewers:** This project demonstrates my commitment to building privacy-preserving systems and my understanding of the gap between operational security and true privacy protection. The limitations section honestly acknowledges what I don't yet know. Suggestions and improvements are welcome via issues or pull requests.
