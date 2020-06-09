import streamlit as st

def main():
    
    """Streamlit and video """
    
    st.title("Streamlit")
    
    video_file = open('radar.mp4', 'rb')
    video_bytes = video_file.read()

    if st.button("Video"):
       st.video(video_bytes)


if __name__ == '__main__':
    main()
