import streamlit as st
from PIL import Image
import io

def main():
    st.title("vidibebapps")
    st.image("President_University_Logo (2).png",width=150)

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
        download_format = st.radio("Format file:", ("PNG", "JPG"))

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

if __name__ == "__main__":
    main()
