# Privacy-First Body Measurement Extraction

**A demonstration that biometric data processing doesn't require centralization**

## Overview

This project addresses a critical gap in privacy-preserving technologies: most virtual try-on and body measurement systems require uploading full-body video to centralized servers. This prototype demonstrates that body measurements can be extracted **entirely on the user's device**, proving that centralized biometric collection is an architectural choice, not a technical necessity.

**Key Privacy Principle:** Your body never leaves your device.

## The Problem

Current virtual try-on technologies in fashion and AR/VR require users to:
1. Upload continuous video streams of their bodies to company servers
2. Trust that biometric data is handled appropriately
3. Accept that compliance frameworks (SOC2, HIPAA) audit *how* data is handled, not *whether* it should be collected at all

This creates unnecessary privacy risks. If measurements can be extracted locally, why centralize sensitive biometric data?

## This Solution

This application demonstrates **local-first biometric processing**:

- ✅ All video processing happens on your device
- ✅ Pose detection runs locally using MediaPipe
- ✅ Only final measurements (numbers) are stored
- ✅ Video frames are **never** saved or transmitted
- ✅ Zero server communication required

### Privacy Architecture Comparison

| Approach | Data Transmitted | Privacy Risk |
|----------|------------------|--------------|
| **Traditional centralized** | 1,800 video frames/minute (30fps) | High - full biometric stream exposed |
# Privacy-First Body Measurement Extraction

**A demonstration that biometric data processing doesn't require centralization**

## Overview

This project addresses a critical gap in privacy-preserving technologies: most virtual try-on and body measurement systems require uploading full-body video to centralized servers. This prototype demonstrates that body measurements can be extracted **entirely on the user's device**, proving that centralized biometric collection is an architectural choice, not a technical necessity.

**Key Privacy Principle:** Your body never leaves your device.

## The Problem

Current virtual try-on technologies in fashion and AR/VR require users to:
1. Upload continuous video streams of their bodies to company servers
2. Trust that biometric data is handled appropriately
3. Accept that compliance frameworks (SOC2, HIPAA) audit *how* data is handled, not *whether* it should be collected at all

This creates unnecessary privacy risks. If measurements can be extracted locally, why centralize sensitive biometric data?

## This Solution

This application demonstrates **local-first biometric processing**:

- ✅ All video processing happens on your device
- ✅ Pose detection runs locally using MediaPipe
- ✅ Only final measurements (numbers) are stored
- ✅ Video frames are **never** saved or transmitted
- ✅ Zero server communication required

### Privacy Architecture Comparison

| Approach | Data Transmitted | Privacy Risk |
|----------|------------------|--------------|
| **Traditional centralized** | 1,800 video frames/minute (30fps) | High - full biometric stream exposed |
| **This local approach** | ~10 measurements/session | Minimal - only derived statistics |
| **Data reduction** | 99.9% less data | Fundamentally different threat model |

## Technical Implementation

**Stack:**
- Python 3.8+
- OpenCV - webcam capture and display
- MediaPipe Pose - local pose estimation
- NumPy - geometric calculations

**Key Components:**
1. `pose_detector.py` - Detects body landmarks from video frames
2. `measurement_calculator.py` - Calculates measurements from landmark coordinates
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

This project is the foundation for my intended research in **privacy-preserving streaming biometric systems**. At graduate school, I plan to extend this work to:

1. Implement **temporal differential privacy** for streaming pose data
2. Explore **secure enclave processing** for cryptographic guarantees
3. Develop **streaming federated learning** architectures for model updates without centralization
4. Build production-ready systems that can process 30fps biometric streams with formal privacy guarantees

This prototype demonstrates I understand:
- The biometric processing pipeline
- Why local processing matters for privacy
- The gap between current solutions and what's needed
- How to build working systems, not just theoretical models

## Why This Matters

**For Fashion (my background with BÁJ):** Virtual try-on should democratize access to proper sizing without requiring surveillance of users' bodies.

**For Healthcare:** Remote patient monitoring shouldn't require streaming unencrypted biometric data to cloud providers.

**For AR/VR:** Immersive experiences shouldn't come at the cost of permanent biometric data collection.

**Broader Principle:** Privacy engineering isn't just about compliance—it's about building systems where surveillance is **architecturally unnecessary**, not just procedurally restricted.

## Contributing

This is a learning project and portfolio piece for graduate school applications. Suggestions and improvements welcome via issues or pull requests.

## License

MIT License - feel free to use this code for educational purposes.

## Contact

Geena Greene  
[GitHub](https://github.com/geenaashlee) | [LinkedIn](https://linkedin.com/in/yourprofile)

---

**Note to Reviewers:** This project demonstrates my commitment to building privacy-preserving systems and my understanding of the gap between operational security and true privacy protection. The limitations section honestly acknowledges what I don't yet know—which is why I'm pursuing graduate studies in Privacy Engineering.
