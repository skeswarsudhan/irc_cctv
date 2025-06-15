from irc_class import *
import os
import random
import cv2, time, pandas
from datetime import datetime

## IRC Config
server = "192.168.15.166"  # Provide a valid server IP/Hostname
port = 6667
channel = "#7"
user = "cctv1"
userpass = "guido"
botpass = "<%= @guido_password %>"
irc = IRC()
irc.connect(server, port, channel, user, botpass, userpass)

while True:

    static_back = None


    motion_list = [None, None]

    time = []

    df = pandas.DataFrame(columns=["Start", "End"])

    # Capturing video
    video = cv2.VideoCapture(0)


    while True:
        # Reading frame(image) from video
        check, frame = video.read()

        # Initializing motion = 0(no motion)
        motion = 0

        # Converting color image to gray_scale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Converting gray scale image to GaussianBlur
        # so that change can be find easily
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # In first iteration we assign the value
        # of static_back to our first frame
        if static_back is None:
            static_back = gray
            continue

        # Difference between static background
        # and current frame(which is GaussianBlur)
        diff_frame = cv2.absdiff(static_back, gray)

        # If change in between static background and
        # current frame is greater than 30 it will show white color(255)
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        # Finding contour of moving object
        cnts, _ = cv2.findContours(thresh_frame.copy(),
                                   cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            motion = 1

            (x, y, w, h) = cv2.boundingRect(contour)
            # making green rectangle around the moving object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Appending status of motion
        motion_list.append(motion)
        if motion == 1:
            irc.send(channel, "Motion_detected!")
    key=input()
    if key == ord('q'):
        break