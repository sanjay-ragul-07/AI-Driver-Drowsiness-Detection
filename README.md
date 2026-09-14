# AI-Based Driver Drowsiness Detection System

A real-time computer vision system designed to detect prolonged driver eye closure using a webcam. When the driver's eyes remain closed continuously for more than 3 seconds, the system identifies a possible drowsiness condition and activates an audio alarm.

## Project Overview

Driver drowsiness is a major safety concern, particularly during long-distance and night-time driving. This project provides a software-based solution that continuously monitors the driver's face and eyes through a webcam.

The system analyzes the driver's eye state in real time and measures the duration of continuous eye closure. If the eyes remain closed beyond the defined threshold, an audio warning is activated to alert the driver.

## Key Features

- Real-time webcam-based monitoring
- Face detection
- Eye detection
- Continuous eye-closure timing
- 3-second drowsiness threshold
- Real-time drowsiness status display
- Audio alarm alert
- Mirror camera view
- No additional hardware required
- Runs on a standard computer with a webcam

## System Workflow

```text
Webcam
   ↓
Video Frame Capture
   ↓
Face Detection
   ↓
Eye Detection
   ↓
Eye Closure Monitoring
   ↓
Continuous Closure > 3 Seconds?
   ↓
Yes ──→ Drowsiness Detected
   ↓
Audio Alarm
