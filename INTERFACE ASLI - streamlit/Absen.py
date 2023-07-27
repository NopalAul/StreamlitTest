# Library
import streamlit as st
from streamlit_option_menu import option_menu #pip install streamlit-option-menu
from PIL import Image
import requests
from streamlit_lottie import st_lottie  #pip install streamlit-lottie

# Parting
import ScanWajah as SW
import RegisterWajah as RW

iconAtas = Image.open('people.png')

st.set_page_config(
    page_title="Absenskutt",
    page_icon=iconAtas,
)


## kalo mau jadi navbar:
selected = option_menu(
        menu_title=None,
        options=["Homepage", "Scan Wajah", "Register Wajah",],
        icons=["house", "camera", "card-checklist"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            # "container": {"padding": "0!important", "background-color": "#00000"},
            # "icon": {"color": "orange", "font-size": "25px"}, 
            # "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            # "nav-link-selected": {"background-color": "green"},
        }
    )

# st.sidebar.success("Halaman:")

# # kalo mau jadi sidebar:
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu",
#         options=["Homepage", "Scan Wajah", "Register Wajah"],
#         icons=["house", "camera", "card-checklist"],
#         menu_icon="cast",
#         default_index=0,
#     )

# ---- HOMEPAGE ----
if selected == "Homepage":
    # [theme]
    # font = "Helvetica Neue"
    st.markdown("<h1 style='text-align: center;'>ABSENSI MAHASISWA</h1>", unsafe_allow_html=True)

    ### link
    # https://assets3.lottiefiles.com/packages/lf20_sycl9imh.json
    # https://assets3.lottiefiles.com/packages/lf20_jrpzvtqz.json
    def load_lottieur1(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_hello = load_lottieur1("https://assets3.lottiefiles.com/packages/lf20_jrpzvtqz.json")
    st_lottie(
        lottie_hello,
        key="hello1",
        loop=True,
    )

    st.markdown("***")
    st.text("")
    st.markdown(
        """
        Selamat datang di website **absensi**
        <h2 style='text-align: center;'>Mulai Scan Wajah</h2>

        Belum terdaftar?
        <h2 style='text-align: center;'>Daftarkan Wajah</h2>
        """, unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["korban bencana", "osilasi hati"])
    with tab1:
        st.write('barang siapa')
    with tab2:
        st.write('barang saya')
        
# ---- SCAN WAJAH ----
if selected == "Scan Wajah":
    SW.page_ScanWajah()

# ---- REGISTER WAJAH ----
if selected == "Register Wajah":
    RW.page_RegisterWajah()

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)