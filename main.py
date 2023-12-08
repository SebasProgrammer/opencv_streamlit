import av
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        return av.VideoFrame.from_ndarray(img, format="bgr4")

webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
                rtc_configuration=RTCConfiguration(
                    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
                ))

