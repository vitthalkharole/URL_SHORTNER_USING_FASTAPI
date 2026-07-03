import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000/url"

st.set_page_config(
    page_title="URL Shortener",
    page_icon="🔗",
    layout="wide"
)

st.title("🔗 URL Shortener")
st.write("FastAPI + Streamlit")

menu = st.sidebar.selectbox(
    "Choose",
    [
        "Create Short URL",
        "All URLs",
        "Redirect",
        "Delete URL"
    ]
)

# -------------------------
# CREATE
# -------------------------

if menu == "Create Short URL":

    st.header("Create Short URL")

    original_url = st.text_input("Enter Long URL")

    if st.button("Generate"):

        if original_url == "":
            st.warning("Enter URL")
        else:

            response = requests.post(
                f"{BASE_URL}/shorten",
                json={
                    "original_url": original_url
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Short URL Created")

                st.write("Original URL")
                st.code(data["original_url"])

                st.write("Short Code")
                st.code(data["short_code"])

                st.write("Short URL")
                st.code(data["short_url"])

            else:
                st.error(response.text)

# -------------------------
# GET ALL
# -------------------------

elif menu == "All URLs":

    st.header("All URLs")

    if st.button("Load URLs"):

        response = requests.get(f"{BASE_URL}/all")

        if response.status_code == 200:

            urls = response.json()

            st.dataframe(urls)

        else:
            st.error(response.text)

# -------------------------
# REDIRECT
# -------------------------

elif menu == "Redirect":

    st.header("Open Original URL")

    code = st.text_input("Short Code")

    if st.button("Open"):

        if code:

            url = f"http://127.0.0.1:8000/url/short_url?short_code={code}"

            st.markdown(
                f"[Click Here to Open Original URL]({url})"
            )

# -------------------------
# DELETE
# -------------------------

elif menu == "Delete URL":

    st.header("Delete URL")

    code = st.text_input("Short Code")

    if st.button("Delete"):

        response = requests.delete(
            f"{BASE_URL}/delete/{code}"
        )

        if response.status_code == 200:
            st.success("Deleted Successfully")
        else:
            st.error(response.text)