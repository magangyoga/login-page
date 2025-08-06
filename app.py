import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Login Dashboard Vandana", layout="wide")

# ========= DATA USER ===========
users = {
    "admin": {
        "password": "12345",
        "role": "Admin",
        "dashboard_url": "https://lookerstudio.google.com/u/0/reporting/bb415b3a-1386-4237-b9d6-ee0608cf4c1d/page/p_cv5af3utud/edit"
    },
    "user": {
        "password": "abcde",
        "role": "User",
        "dashboard_url": "https://lookerstudio.google.com/u/0/reporting/bb415b3a-1386-4237-b9d6-ee0608cf4c1d/page/p_cv5af3utud"
    }
}

# ========= SESSION ============
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# ========= FUNGSI LOGIN ============
def login(username, password):
    username = username.strip()
    password = password.strip()
    return username in users and users[username]["password"] == password

# ========= CSS CERAH ============
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #fffefc !important;
            color: #333333;
            font-family: "Segoe UI", sans-serif;
            font-size: 18px;
        }

        .stTextInput>div>input {
            background-color: #ffffff;
            color: #333333;
            font-size: 16px;
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 8px;
        }

        .stButton>button {
            background-color: #7BE495;
            color: #ffffff;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            transition: background-color 0.3s;
        }

        .stButton>button:hover {
            background-color: #57cc8a;
        }

        .custom-dashboard-button {
            background-color: #FFB562;
            color: white;
            font-size: 20px;
            padding: 12px 30px;
            border-radius: 10px;
            border: none;
            text-decoration: none;
            display: inline-block;
        }

        .custom-dashboard-button:hover {
            background-color: #ffaa3c;
        }
    </style>
""", unsafe_allow_html=True)

# ========= FORM LOGIN ============
if not st.session_state.logged_in:
    st.title("🔐Login ke Dashboard Vandana")
    st.write("Masukkan username dan password anda!")

    with st.form("login_form"):
        username = st.text_input("👤 Username").strip()
        password = st.text_input("🔑 Password", type="password").strip()
        submit = st.form_submit_button(" Masuk")

        if submit:
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("✅ Login berhasil!")
                st.rerun()
            else:
                st.error("❌ Username atau password salah.")

# ========= TAMPILAN DASHBOARD ============
if st.session_state.logged_in:
    user_info = users[st.session_state.username]

    with st.sidebar:
        st.success(f"👋 Login sebagai: **{st.session_state.username}** ({user_info['role']})")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()

    st.title(f"📊 {user_info['role']} Dashboard")
    st.write("Klik tombol di bawah untuk membuka dashboard Anda:")

    st.markdown(f"""
        <a href="{user_info['dashboard_url']}" target="_blank">
            <button style='font-size:20px;padding:12px 30px;border-radius:10px;background-color:#3399ff;color:white;border:none;'>
                🚀 Buka Dashboard Vandana
            </button>
        </a>
    """, unsafe_allow_html=True)


