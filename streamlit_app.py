import streamlit as st
from PIL import Image
import io
from fpdf import FPDF

def main():
    st.title("vidibebapps")

    st.write("Unggah gambar Anda dan pilih derajat rotasi untuk melihat hasilnya.")

    # Upload file
    uploaded_file = st.file_uploader("Unggah gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Baca gambar
        image = Image.open(uploaded_file)

        # Tampilkan gambar asli
        st.subheader("Gambar Asli:")
        st.image(image, caption="Gambar asli yang diunggah", use_column_width=True)

        # Input derajat rotasi
        degree = st.slider("Pilih derajat rotasi", min_value=0, max_value=360, value=0)

        # Rotasi gambar
        rotated_image = image.rotate(-degree, expand=True)

        # Tampilkan gambar hasil rotasi
        st.subheader("Gambar Setelah Dirotasi:")
        st.image(rotated_image, caption=f"Gambar setelah dirotasi {degree} derajat", use_column_width=True)

        # Pilih format unduhan
        st.subheader("Pilih Format Unduhan:")
        download_format = st.radio("Format file:", ("PNG", "JPG", "PDF"))

        # Simpan file ke buffer
        buf = io.BytesIO()

        if download_format == "PNG":
            rotated_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(
                label="Unduh Gambar Hasil Rotasi (PNG)",
                data=byte_im,
                file_name="gambar_dirotasi.png",
                mime="image/png",
            )
        elif download_format == "JPG":
            rotated_image = rotated_image.convert("RGB")  # Ensure no alpha channel for JPG
            rotated_image.save(buf, format="JPEG")
            byte_im = buf.getvalue()
            st.download_button(
                label="Unduh Gambar Hasil Rotasi (JPG)",
                data=byte_im,
                file_name="gambar_dirotasi.jpg",
                mime="image/jpeg",
            )
        elif download_format == "PDF":
            pdf = FPDF()
            pdf.add_page()
            rotated_image = rotated_image.convert("RGB")
            buf_pdf = io.BytesIO()
            rotated_image.save(buf_pdf, format="JPEG")
            pdf.image(buf_pdf, x=10, y=10, w=190)
            pdf_buf = io.BytesIO()
            pdf.output(pdf_buf)
            pdf_data = pdf_buf.getvalue()
            st.download_button(
                label="Unduh Gambar Hasil Rotasi (PDF)",
                data=pdf_data,
                file_name="gambar_dirotasi.pdf",
                mime="application/pdf",
            )

if __name__ == "__main__":
    main()
