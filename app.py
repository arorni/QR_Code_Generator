import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image


st.set_page_config(page_title="QR Code Generator", page_icon="🔳")
st.title("QR Code Generator")
st.write("Paste URL here and this app will generate a scannable QR code.")

form_url = st.text_input("URL", placeholder="https://forms.gle/9BvLNCisL1hADVFf9")

if st.button("Generate QR Code"):
    if not form_url.strip():
        st.error("Please enter a valid Google form URL")
        st.stop()
    qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=2
        )
    qr.add_data(form_url.strip())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    st.image(Image.open(buf), caption="Scan to open the google form", width=220)

    st.download_button(label="⬇️ Download QR as PNG", data=buf.getvalue(), file_name="google_form_qr.png",mime="image/png")
