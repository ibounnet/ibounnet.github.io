import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeline as DP

h = st.header('Diffussion.AI')
s = st.subheader('เว็บนี้แปลงข้อควมเปงภาพพพ')
p = st.write('เว็บไซต์นี้แลกมาด้วยความหิวและเร็วที่จับไม่ได้')
text = st.text_input('prompt : ')
if text : 
   dp = DP.from_pretrained('runwayml/stable-diffussion-v1-5' , 
                            torch_dtype=torch.float16)
   
   image_data = dp(text).image[0]
   image = Image.fromarry(image_data)
   image.show()