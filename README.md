# Sign-language-control-of-home-appliances
This project presents an intelligent Sign Language-Based Home Appliance Control System designed to assist deaf and speech-impaired individuals in controlling household devices independently. The system uses a webcam to capture hand gestures based on American Sign Language &amp;  processes them using CV &amp; Deep Learning techniques (CNN + LSTM).

## Welcome
Welcome to this project! 
This repository presents an intelligent **Sign Language–Based Home Appliance Control System** designed to help **deaf and speech-impaired individuals** control household devices independently using hand gestures.

## Objectives
- Enable **gesture-based control** of home appliances  
- Provide a **non-contact, non-voice interface**  
- Improve **accessibility and independence**  
- Implement **real-time gesture recognition using AI**

## Features
- Real-time hand gesture recognition  
- Supports **static and dynamic gestures**  
- No wearable devices required  
- Cost-effective and user-friendly  
- Scalable for multiple appliances  
- Seamless integration of AI and hardware  

## Technologies Used
- **Programming Language:** Python  
- **Libraries:** OpenCV, MediaPipe, NumPy, CVZone  
- **Deep Learning:** CNN, LSTM (TensorFlow/Keras)  
- **Hardware:** Arduino Uno / ESP32, Relay Module  
- **Communication:** Serial (UART)

## System Architecture
1. Webcam captures hand gestures  
2. Image preprocessing (noise removal, segmentation, normalization)  
3. Hand detection using MediaPipe / CVZone  
4. Feature extraction using CNN  
5. Sequence recognition using LSTM  
6. Gesture classification (Softmax)  
7. Command mapping  
8. Signal sent to Arduino  
9. Relay controls appliances

## Working Flow
Gesture → Camera → Preprocessing → CNN → LSTM → Classification → Command → Arduino → Appliance  

## Hardware Requirements
- Webcam  
- Arduino Uno / ESP32  
- Relay Module (4-channel recommended)  
- Light / Fan (or LED, Motor for demo)  
- Jumper Wires  
- Power Supply  
- Breadboard (optional)

## Software Requirements
- Python 3.x  
- OpenCV  
- MediaPipe / CVZone  
- TensorFlow / Keras  
- NumPy  
- PySerial  

## Applications
- Smart home automation  
- Assistive technology for disabled individuals  
- Human-computer interaction systems  
- AI-based accessibility solutions  

## Limitations
- Performance depends on lighting conditions  
- Requires proper hand positioning  
- Limited gesture set (can be expanded)  
- Background noise may affect detection  

## Conclusion
This project enables **gesture-based control of home appliances** using AI and computer vision, providing a **simple, real-time, and accessible solution** for deaf and speech-impaired users.

