import streamlit as st
from PIL import Image
import io

# Judul aplikasi
st.title("Unggah untuk Merotasi Gambar by.triokacamata")

# Upload gambar
uploaded_image = st.file_uploader("Upload gambar (PNG atau JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Baca gambar
    image = Image.open(uploaded_image)

    # Tampilkan gambar asli
    st.subheader("Gambar Asli")
    st.image(image, use_column_width=True)

    # **Rotasi Gambar**
    rotation_angle = st.slider("Rotasi Gambar (derajat)", 0, 360, 0)
    rotated_image = image.rotate(rotation_angle)

    # Tampilkan gambar hasil rotasi
    st.subheader("Gambar Setelah Rotasi")
    st.image(rotated_image, use_column_width=True)

    # **Tombol Unduh**
    st.subheader("Download Gambar")

    # Simpan gambar sebagai PNG
    buffer_png = io.BytesIO()
    rotated_image.save(buffer_png, format="PNG")
    st.download_button(
        label="Download sebagai PNG",
        data=buffer_png.getvalue(),
        file_name="rotated_image_by.triokacamata.png",
        mime="image/png",
    )

    # Simpan gambar sebagai JPG
    buffer_jpg = io.BytesIO()
    rotated_image.convert("RGB").save(buffer_jpg, format="JPEG")
    st.download_button(
        label="Download sebagai JPG",
        data=buffer_jpg.getvalue(),
        file_name="rotated_image_by.triokacamata.jpg",
        mime="image/jpeg",
    )

    # Simpan gambar sebagai PDF
    buffer_pdf = io.BytesIO()
    rotated_image.convert("RGB").save(buffer_pdf, format="PDF")
    st.download_button(
        label="Download sebagai PDF",
        data=buffer_pdf.getvalue(),
        file_name="rotated_image_by.triokacamata.pdf",
        mime="application/pdf",
    )
