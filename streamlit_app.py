import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np
import io

# Judul aplikasi
st.title("Alat Transformasi Gambar")

# Upload gambar
uploaded_image = st.file_uploader("Upload gambar (PNG atau JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Baca gambar
    image = Image.open(uploaded_image)

    # Tampilkan gambar asli
    st.subheader("Gambar Asli")
    st.image(image, use_column_width=True)

    # **1. Rotasi Gambar**
    rotation_angle = st.slider("Rotasi Gambar (derajat)", 0, 360, 0)
    rotated_image = image.rotate(rotation_angle)

    # **2. Translasi Gambar**
    translate_x = st.slider("Translasi Horizontal (pixel)", -100, 100, 0)
    translate_y = st.slider("Translasi Vertikal (pixel)", -100, 100, 0)
    translated_image = rotated_image.transform(
        rotated_image.size, Image.AFFINE, (1, 0, translate_x, 0, 1, translate_y)
    )

    # **3. Skala Gambar**
    scale_factor = st.slider("Faktor Skala (persen)", 50, 200, 100) / 100
    width, height = translated_image.size
    scaled_image = translated_image.resize((int(width * scale_factor), int(height * scale_factor)))

    # **4. Kemiringan Gambar (Shear)**
    shear_x = st.slider("Kemiringan Horizontal", -1.0, 1.0, 0.0)
    shear_y = st.slider("Kemiringan Vertikal", -1.0, 1.0, 0.0)
    shear_matrix = (1, shear_x, 0, shear_y, 1, 0)
    sheared_image = scaled_image.transform(scaled_image.size, Image.AFFINE, shear_matrix)

    # **5. Kecerahan Gambar**
    brightness_factor = st.slider("Atur Kecerahan", 0.0, 2.0, 1.0)
    brightness_enhancer = ImageEnhance.Brightness(sheared_image)
    brightened_image = brightness_enhancer.enhance(brightness_factor)

    # Tampilkan gambar hasil transformasi
    st.subheader("Gambar Setelah Transformasi")
    st.image(brightened_image, use_column_width=True)

    # **Tombol Unduh**
    st.subheader("Download Gambar")
    
    # Simpan gambar sebagai PNG
    buffer_png = io.BytesIO()
    brightened_image.save(buffer_png, format="PNG")
    st.download_button(
        label="Download sebagai PNG",
        data=buffer_png.getvalue(),
        file_name="transformed_image.png",
        mime="image/png",
    )

    # Simpan gambar sebagai JPG
    buffer_jpg = io.BytesIO()
    brightened_image.convert("RGB").save(buffer_jpg, format="JPEG")
    st.download_button(
        label="Download sebagai JPG",
        data=buffer_jpg.getvalue(),
        file_name="transformed_image.jpg",
        mime="image/jpeg",
    )

    # Simpan gambar sebagai PDF
    buffer_pdf = io.BytesIO()
    brightened_image.convert("RGB").save(buffer_pdf, format="PDF")
    st.download_button(
        label="Download sebagai PDF",
        data=buffer_pdf.getvalue(),
        file_name="transformed_image.pdf",
        mime="application/pdf",
    )
