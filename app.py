import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
hamza_anwar = Image.open("./images/2.png")
lottie_coding = load_lottieurl("https://lottie.host/3b0acd02-86a2-4939-b930-f5cd716a395d/NGjYPawqGn.json")
lottie_contact = load_lottieurl("https://lottie.host/124180e0-06dc-43ce-8002-908f2de27a2c/LXZiClt1xS.json")
snakerobot = Image.open("./images/snakerobot.jpg")
adrover = Image.open("./images/rover.png")
allenrobot = Image.open("./images/smart.png")

st.set_page_config(page_title="Streamlit_Project_1", page_icon=hamza_anwar, layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello! I am Hamza Anwar. :wave:")
    st.title("Roboticist | Data Scientist | Machine Learning Engineer")
    st.write("Engineer by chance, technologist by choice.")
    st.write("[Learn more about me](https://www.linkedin.com/in/hamza-anwar-32454a22b)")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do?")
        st.write("##")
        st.write("AI and robotics engineer with a passion for creating intelligent systems and solving complex problems.")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects.")
    st.write("##")
    with st.container():
        right_column, left_column = st.columns((1, 2))
        with left_column:
            st.header("Robotics")
            st.subheader("Snake robot")
            st.write("A snake robot which can be controlled by a mobile phone and be deployed at search and rescue operations.")
            st.write("ROS | AI | Robotics | Python | Raspberry Pi | IMU | Robotis Smart Servos")
        with right_column:
            st.image(snakerobot)
    with st.container():
        right_column, left_column = st.columns((1, 2))
        with left_column:
            st.subheader("SMART: Social Mobile Autonomous RoboT")
            st.subheader("Allen robot")
            st.write("A minion robot to run around in mall, guiding customers and communicating with them.")
            st.write("ROS | Depth sensing | OpenCR | Python | Jetson Nano | LLMs | Robotis Smart Servos")
        with right_column:
            st.image(allenrobot)
    with st.container():
        right_column, left_column = st.columns((1, 2))
        with left_column:
            st.subheader("+Rover")
            st.write("+Rover, pronounced as 'ad-rover', is a robotic platform which can be deployed in public places to guide and communicate with customers as well as provides advertisement services to the mall shops over a large HD screen.")
            st.write("ROS | Depth sensing | OpenCR | Python | Jetson Nano | LLMs | Robotis Smart Servos | Advertisement Services")
        with right_column:
            st.image(adrover)

# ---- Contact me! ----

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./style/styles.css")

contact_form = """
<form action="https://formsubmit.co/hamzaanwar5893@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""

st.write("---")
st.header("Contact me!")
st.write("##")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_contact, height=282, key="contact")
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)

st.write("---")
st.write("The images are just placeholders. They are not real.")