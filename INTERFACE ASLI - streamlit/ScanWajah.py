import streamlit as st

def page_ScanWajah():
    st.markdown("# Scan Wajah Anda")
    st.sidebar.header("Scan Wajah")
    st.write(
        """
        Hadapkan wajah ke kamera, tunggu hingga scan selesai.
        """
    )
    kamera = st.checkbox("Aktifkan Kamera")
    if kamera == True:
        st.image('contoh_webcam.jpeg', width=400)
        st.success("Kehadiran berhasil tercatat.")
    else:
        pass
    
    # col1,col2,col3 = st.columns(3)
    # with col1:
    #     st.write('')
    # with col2:
    #     st.image('contoh_webcam.jpeg', width=400)
    # with col3:
    #     st.write('')
