import cv2
import numpy as np
from PIL import Image
import streamlit as st


st.title("Image Blur App")

with st.sidebar:
    blur_amount = st.slider("چقدر میخوای تصویر مات بشه؟",
                                min_value=1,
                                max_value=199,
                                value=21,
                                step=2)

uploaded_file = st.file_uploader("Choose and image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.success("فایل با موفقیت بارگزاری شد")


    image = Image.open(uploaded_file)
    st.image(image, "Input")

    
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


    #process
 
                            
    result_image = cv2.blur(image, (blur_amount, blur_amount))

    #postprocessing
    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    result_image = Image.fromarray(result_image)

    st.image(result_image, "Output")


else:
    st.info("هیچ فایلی بارگزاری نشده است")    
