from streamlit_webrtc import webrtc_streamer, WebRtcMode
import streamlit as st
import av

class VideoProcessor:

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")
st.title("New APP")

webrtc_streamer(key="key", video_processor_factory=VideoProcessor)

