# Prosthetic-arm-using-OpenCV# 🦾 Prosthetic Arm using OpenCV & STM32

A low-cost **prosthetic arm** project built using **STM32 microcontroller**, **PCA9685 PWM driver**, and **servo motors**, controlled via **hand gesture recognition with OpenCV**.  
This project demonstrates how computer vision and embedded systems can work together to create affordable assistive technology.

---

## 📷 Demo
![WhatsApp Image 2025-08-28 at 1 15 27 AM](https://github.com/user-attachments/assets/89916a01-60c6-41c2-94f8-f4af77b1f625)


---

## 🔧 Features
- Real-time **gesture detection** using OpenCV (Python).  
- **UART communication** between Raspberry Pi/PC and STM32.  
- **Servo motor control** via PCA9685 (16-channel PWM).  
- Modular design (easy to scale for more DOF).  
- Affordable hardware (< INR 5000).  

---

## 🗂️ Repository Structure
prosthetic-arm-opencv-stm32/
│
├── firmware/ # STM32 embedded firmware
│ └── Core/
│ └── main.c
│
├── hardware/ # Schematics
│ └── schematic.jpg
│
├── vision/ # OpenCV gesture recognition
│ └── gesture_control.py
│
└── README.md # Project documentation

---

## ⚙️ Hardware Components
- **STM32F407 / STM32 Blue Pill (F103)** – Microcontroller.  
- **PCA9685** – 16-channel PWM driver for servos.  
- **Servo Motors** – SG90 / MG996R (depending on strength needed).  
- **Raspberry Pi / PC** – Runs OpenCV for gesture recognition.  
- **USB Camera / Pi Camera** – Captures hand gestures.  
- Power Supply: 5V @ 2–3A.  

---

## 💻 Software & Tools
- **STM32CubeIDE** → for STM32 firmware development.  
- **OpenCV (Python)** → gesture recognition.  
- **I2C & UART drivers** → for communication.  
- **KiCad / EasyEDA** → circuit & PCB design.  

---

## 🚀 How It Works
1. Camera captures **hand gesture** in real-time.  
2. OpenCV classifies the gesture (e.g., fist, open hand, point).  
3. Command is sent to STM32 over **UART**.  
4. STM32 controls **servo motors** via **PCA9685**.  
5. Prosthetic arm replicates the hand gesture.  

![System Architecture]![WhatsApp Image 2025-08-28 at 1 23 39 AM](https://github.com/user-attachments/assets/984419bf-a30a-4458-a09d-67eaa1c629e0)


---

## 🛠️ Setup & Usage

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/username/prosthetic-arm-opencv-stm32.git
cd prosthetic-arm-opencv-stm32
