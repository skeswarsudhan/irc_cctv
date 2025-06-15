# 📹 CCTV Motion Detection with IRC Notification

This project implements a motion detection system using OpenCV and sends alerts to an IRC channel when motion is detected. It captures video from the default webcam, detects motion by comparing frames, and uses an IRC bot to send messages to a Raspberry Pi-hosted IRC server.

---

## 🚀 Features

- ✅ Real-time motion detection using OpenCV  
- 📢 Motion alert notifications sent via IRC  
- 🍓 Connects to an IRC server running on Raspberry Pi  

---

## 📦 Requirements

- Python 3.x  
- `opencv-python` (`cv2`)  
- `pandas`  
- IRC server (e.g., hosted on Raspberry Pi)  

---

## 🔧 Installation

1. Clone the repository or copy the files.

2. Install the required Python packages:

   ```bash
   pip install opencv-python pandas
   ```

3. Update the following parameters in `cctv.py` with your IRC server details:

   ```python
   server = "YOUR_RASPBERRY_PI_IP"
   port = 6667
   channel = "#your_channel"
   user = "your_username"
   userpass = "your_user_password"
   botpass = "your_bot_password"
   ```

---

## ▶️ Usage

Run the script with:

```bash
python cctv.py
```

- A green rectangle will highlight detected motion in the video feed.  
- A message `"Motion_detected!"` will be sent to the specified IRC channel hosted on the Raspberry Pi when motion is detected.

---

## 📁 File Overview

| File         | Description                                                   |
|--------------|---------------------------------------------------------------|
| `cctv.py`    | Main script for motion detection and IRC message sending      |
| `irc_class.py` | IRC client class used to connect and communicate with the IRC server on the Raspberry Pi |

---

## 📜 License

This project is intended for **educational/demo purposes**.  
Feel free to **modify and reuse** it in your own projects!

