from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import streamlit as st
import av

def callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")
    return av.VideoFrame.from_ndarray(img, format="bgr24")
st.title("New APP")

webrtc_streamer(key="key", video_frame_callback=callback)

