import av
from streamlit_webrtc import webrtc_streamer

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        return av.VideoFrame.from_ndarray(img, format="bgr4")

webrtc_streamer(key="key", video_processor_factory=VideoProcessor)

