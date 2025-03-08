import streamlit as st
from ubuai import Chatbot  # ✅ Import Chatbot จาก ubuai.py

# สร้างอินสแตนซ์ของ Chatbot
chatbot = Chatbot()

# ตั้งค่าหน้าเริ่มต้น
st.set_page_config(page_title="Ubu Chat Bot AI", layout="wide")

# แบ่งคอลัมน์ออกเป็น 3 ส่วน (ซ้าย, กลาง, ขวา)
col1, col_divider, col3 = st.columns([0.3, 0.03, 1], gap="medium")
with st.sidebar:
    st.title("Hi , it's My Profile")
    st.write("เกี่ยวกับเรา ผม นายธีรพล พูพวง ")
    st.write("รหัสนักศึกษา 67114540277 คณะ วิทยาศาสตร์ สาขา Dssi")
    st.write("My Contract")
    st.markdown(""" 
        <style>
            .button_link1 {
                margin-bottom: 10px;
            }
            .button_link2 {
                margin-bottom: 10px;
            }
            .button_link3 {
                margin-bottom: 10px;
            }
            .btn1 {
                background-color: #126ffd;
                transition: ease 0.3s, transform 0.3s, background 0.3s ;
            }
            .btn1:hover {
                transform: scale(1.2);
                background-color: blue;
            }
            .btn2 {
                background-color: #e82aa3; 
                transition: ease 0.3s, transform 0.3s, background 0.3s ;
            }
            .btn2:hover {
                transform: scale(1.2);
                background-color: pink;
            }
            .btn3 {
                background-color: #2d292b; 
                transition: ease 0.3s, transform 0.3s, background 0.3s ;
            }
            .btn3:hover {
                transform: scale(1.2);
                background-color: black;
            }
        </style> 
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="button_link1">
            <a href="https://www.facebook.com/profile.php?id=100085487510155" target="_blank">
                <button class="btn1" type="button">My Facebook</button>
            </a>
        </div>
        <div class="button_link2">
            <a href="https://www.instagram.com/t.rpnz/" target="_blank">
                <button class="btn2" type="button">My Instagram</button>
            </a>
        </div>
        <div class="button_link3">
            <a href="https://github.com/Ttub19" target="_blank">
                <button class="btn3" type="button">My GitHub</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

# ใช้ CSS เพื่อจัดรูปแบบ UI
with col1:
    def addchat():
        with col3:
            st.write("🤖 Ubu Chat Bot AI ")
            st.write("แชทบอทที่สามารถถามได้ทุกอย่างแต่ไม่สามารถตอบได้ทุกอย่าง")

            # ตรวจสอบว่า selected_topic มีค่าใน session_state แล้วหรือยัง
            if "selected_topic" not in st.session_state:
                st.session_state.selected_topic = "ไม่มีหัวข้อ"  # กำหนดค่าเริ่มต้น

            selected_topic = st.session_state.selected_topic  # ดึงค่าหัวข้อที่เลือกจาก session_state

            # ตรวจสอบว่ามีประวัติการสนทนาสำหรับหัวข้อนี้ไหม
            if selected_topic not in st.session_state:
                st.session_state[selected_topic] = []  # สร้างประวัติแชทสำหรับหัวข้อที่เลือก

            chat_container = st.container()  # สร้าง container สำหรับแสดงประวัติแชท
            with chat_container:
                st.markdown('<div class="chat-box">', unsafe_allow_html=True)  # ใช้ div สำหรับการแสดงแชท
                for sender, msg in st.session_state[selected_topic]:  # วนลูปแสดงข้อความของผู้ใช้และบอท
                    st.write(f" **{sender}**: {msg}")  # แสดงชื่อผู้ส่งและข้อความ
                st.markdown('</div>', unsafe_allow_html=True)  # ปิด div

        # จัดช่องพิมพ์ข้อความให้อยู่ทางขวา
        col_empty, col_input = st.columns([0.1, 0.9])  # ใช้ 2 คอลัมน์
        with col_input:
            with st.form(key="chat_form"):  # ใช้ form เพื่อจัดกลุ่มข้อความและปุ่มส่ง
                user_input = st.text_input("Entry Your Message Here", key="chat_input")  # ช่องกรอกข้อความ
                submitted = st.form_submit_button("Send")  # ปุ่มส่งข้อความ
                if submitted and user_input.strip():  # ถ้าผู้ใช้กรอกข้อความ
                    st.session_state[selected_topic].append(("User", user_input))  # เพิ่มข้อความของผู้ใช้
                    bot_response = chatbot.get_response(user_input)  # ✅ เรียกใช้ฟังก์ชัน get_response()
                    st.session_state[selected_topic].append(("Bot", bot_response))  # เพิ่มข้อความของบอท
                    st.rerun()  # รีเฟรช

            clear = st.button("ล้างการสนทนา")
            if clear:
                st.session_state[selected_topic] = []  # ล้างประวัติแชท
                st.rerun()  # รีเฟรชเพื่อแสดงข้อความใหม่

            st.file_uploader("อัปโหลดไฟล์", type=["pdf", "txt", "jpg", "png", "jpeg"])

        st.sidebar.title("หัวข้อการสนทนา")

        # กำหนดค่าเริ่มต้นสำหรับ topics ถ้ายังไม่มีใน session_state
        if 'topics' not in st.session_state:
            st.session_state.topics = {"ไม่มีหัวข้อ": []}  # ตั้งค่าเริ่มต้นให้มีหัวข้อ "ไม่มีหัวข้อ"

        selected_topic = st.sidebar.selectbox("เลือกหัวข้อ", list(st.session_state.topics.keys()))  # ให้เลือกหัวข้อจาก Sidebar
        st.sidebar.subheader("เลือกหัวข้อ")  # แสดงหัวข้อย่อยใน Sidebar
        for topic in list(st.session_state.topics.keys()):  # แสดงรายชื่อหัวข้อที่มี
            col1, col2 = st.sidebar.columns([4, 1])  # แบ่งคอลัมน์ (ชื่อหัวข้อ 4 ส่วน, ปุ่มลบ 1 ส่วน)

            with col1:  # แสดงชื่อหัวข้อในคอลัมน์แรก
                if st.session_state.get("selected_topic", "ไม่มีหัวข้อ") == topic:
                    st.markdown(f"*{topic}*")  # ไฮไลต์หัวข้อที่เลือก
                else:
                    st.write(topic)  # แสดงหัวข้อปกติ
            with col2:
                if topic != "ไม่มีหัวข้อ":  # ไม่ให้ลบหัวข้อหลัก
                    if st.button("🗑️", key=f"del_{topic}"):  # ใช้ key ป้องกันปุ่มซ้ำกัน
                        del st.session_state.topics[topic]  # ลบหัวข้อ
                        st.session_state.selected_topic = "ไม่มีหัวข้อ"  # รีเซ็ตหัวข้อที่เลือก
                        st.rerun()  # รีเฟรชหน้าเพื่ออัปเดตรายการหัวข้อ

        # เมื่อเลือกหัวข้อใหม่จะรีเซ็ตแชท
        if selected_topic != st.session_state.get("selected_topic", ""):
            st.session_state[selected_topic] = []  # ลบแชทเมื่อเลือกหัวข้อใหม่
            st.session_state.selected_topic = selected_topic  # เก็บหัวข้อที่เลือก

    new_topic = st.sidebar.text_input("สร้างหัวข้อใหม่")  # ช่องกรอกข้อความสำหรับสร้างหัวข้อใหม่
    if st.sidebar.button("เพิ่มหัวข้อ") and new_topic:  # ถ้ากดปุ่มเพิ่มหัวข้อ
        if new_topic not in st.session_state.topics:  # ถ้าหัวข้อไม่ซ้ำ
            st.session_state.topics[new_topic] = []  # สร้างหัวข้อใหม่
            selected_topic = new_topic  # เลือกหัวข้อใหม่

    # แสดงกล่องข้อความเฉพาะในหน้าแชทและเพิ่มแชท
    pages = [
        st.Page(addchat, title="เพิ่มแชทและคุยกับแชทบอท", icon="➕"),
    ]

    current_page = st.navigation(pages)  # สร้างการนำทางระหว่างหน้า
    current_page.run()  # รันหน้าที่เลือก

# เส้นแบ่งกลาง
with col_divider:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    .divider {
        border-left: 3px solid #333;  
        height: 200vh;
    }
    </style>
    """, unsafe_allow_html=True)
