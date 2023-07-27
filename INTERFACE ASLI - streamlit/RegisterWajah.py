import streamlit as st

def page_RegisterWajah():
    st.markdown("# Register Wajah")
    st.sidebar.header("Register Wajah")
    st.write("***")

    if "Nama" not in st.session_state:
        st.session_state["Nama"] = ""
    if "NIM" not in st.session_state:
        st.session_state["NIM"] = ""

    Nama = st.text_input("Nama", st.session_state["Nama"])
    NIM = st.text_input("NIM", st.session_state["NIM"])

    st.write("Ambil Foto Wajah")
    kamera = st.checkbox("Aktifkan Kamera")
    if kamera == True:
        st.image('contoh_webcam.jpeg', width=400)
    else:
        pass

    # st.write("Ambil Foto Wajah")
    # kamera = st.button("Aktifkan Kamera")
    # if kamera:
    #     st.image('contoh_webcam.jpeg', width=400)
    # else:
    #     pass

    submit = st.button("Submit")
    if submit:
        st.session_state["Nama"] = Nama
        st.session_state["NIM"] = NIM
        st.write(f"{Nama.upper()} {NIM} tercatat.")