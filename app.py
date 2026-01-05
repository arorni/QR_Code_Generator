import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image


st.set_page_config(page_title="QR Code Generator", page_icon="🔳")
st.title("QR Code Generator")
st.write("Paste URL here and this app will generate a scannable QR code.")

form_url = st.text_input("URL", placeholder="https://forms.gle/9BvLNCisL1hADVFa8")

if st.button("Generate QR Code"):
    if not form_url.strip():
        st.error("Please enter a valid URL")
        st.stop()

    if not (form_url.startswith("http://") or form_url.startswith("https://")):
        st.error("URL must start with http:// or https://")
        st.stop()

    qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=4
        )
    qr.add_data(form_url.strip())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    st.image(Image.open(buf), caption="Scan to open the URL.", width=220)

    st.download_button(label="⬇️ Download QR as PNG", data=buf.getvalue(), file_name="qr_code.png",mime="image/png")
