import streamlit as st

h = st.header('My Web Site')
s = st.subheader('บ่บอก')
p = st.write('เว็บไซต์นี้แลกมาด้วยความหิวและเร็วที่จับไม่ได้')
# banner = st.image()
b = st.button('click me')
text = st.text_input('prompt : ')
if text : 
    st.write(f'คงเหลือแค่ความคิดถึง เป็นที่พึ่งยามท้อ ... จาก "{text}"')
    b = st.button('จะไปต่อหรือพอแค่นี้...')