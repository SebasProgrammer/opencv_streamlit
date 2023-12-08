import cv2
import streamlit as st
import numpy as np
import tempfile
import av
from streamlit_webrtc import webrtc_streamer

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        return av.VideoFrame.from_ndarray(img, format="bgr4")

st.title("Prueba")

frame_placeholder = st.empty()

stop_button_pressed = st.button("Stop")

option = st.selectbox(
        'Selecciona tarea a realizar',
        ('None', 'Prender camara', 'Upload photo'))

    # Start with app logic:
if option == 'Prender camara':
    webrtc_streamer(key="key", video_processor_factory=VideoProcessor)
    # cap = cv2.VideoCapture(0)
