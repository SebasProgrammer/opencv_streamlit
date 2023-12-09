from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import streamlit as st
import av

def callback(frame: av.VideoFrame) -> av.VideoFrame:
    return frame
st.title("New APP")

webrtc_streamer(key="key", video_frame_callback=callback)

