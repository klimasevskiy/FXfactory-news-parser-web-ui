import streamlit as st
from PIL import Image
import configparser
import main as backend

icon = Image.open('imgs/logo.png')
st.set_page_config(page_icon=icon, page_title="ForexNotion", layout="centered")

try:
    print(st.session_state.impact_filter)
except:
   st.session_state.impact_filter = ['yellow', 'orange', 'red']

try:
    print(st.session_state.currency_filter)
except:
    st.session_state.currency_filter = []
try:
    print(st.session_state.token)
except:
   st.session_state.token = 'xxx'

try:
    print(st.session_state.db_id)
except:
    st.session_state.db_id = 'xxx'

try:
    print(st.session_state.is_yellow)
except:
    st.session_state.is_yellow = False

try:
    print(st.session_state.is_orange)
except:
    st.session_state.is_orange = False

try:
    print(st.session_state.is_red)
except:
    st.session_state.is_red = False

try:
    print(st.session_state.is_aud)
except:
    st.session_state.is_aud = False

try:
    print(st.session_state.is_cad)
except:
    st.session_state.is_cad = False

try:
    print(st.session_state.is_chf)
except:
    st.session_state.is_chf = False

try:
    print(st.session_state.is_cny)
except:
    st.session_state.is_cny = False

try:
    print(st.session_state.is_eur)
except:
    st.session_state.is_eur = False

try:
    print(st.session_state.is_gbp)
except:
    st.session_state.is_gbp = False

try:
    print(st.session_state.is_jpy)
except:
    st.session_state.is_jpy = False

try:
    print(st.session_state.is_nzd)
except:
    st.session_state.is_nzd = False

try:
    print(st.session_state.is_usd)
except:
    st.session_state.is_usd = False

try:
    print(st.session_state.days_add)
except:
    st.session_state.days_add = 7

def save_settings():
    if not st.session_state.token:
        st.session_state.token = 'xxx'
    if not st.session_state.db_id:
        st.session_state.db_id = 'xxx'
    if not st.session_state.days_add:
        st.session_state.days_add = 7
    impact_list = []
    if st.session_state.is_yellow:
        impact_list.append("yellow")
    if st.session_state.is_orange:
        impact_list.append("orange")
    if st.session_state.is_red:
        impact_list.append("red")
    st.session_state.impact_filter = impact_list

    currency_list = []
    if st.session_state.is_aud:
        currency_list.append("AUD")
    if st.session_state.is_cad:
        currency_list.append("CAD")
    if st.session_state.is_chf:
        currency_list.append("CHF")
    if st.session_state.is_cny:
        currency_list.append("CNY")
    if st.session_state.is_eur:
        currency_list.append("EUR")
    if st.session_state.is_gbp:
        currency_list.append("GBP")
    if st.session_state.is_jpy:
        currency_list.append("JPY")
    if st.session_state.is_nzd:
        currency_list.append("NZD")
    if st.session_state.is_usd:
        currency_list.append("USD")
    st.session_state.currency_filter = currency_list
    
def load_tabs():
        notion_api, data_settings = st.tabs(["✍️ Notion API setting", "📑 Data Settings"])
        with notion_api:
            st.text_input(label="API Token:", type="password", value=st.session_state.token, key='token')
            st.text_input(label="DB Id:", type="password", value=st.session_state.db_id, key='db_id')
        with data_settings:
                col1, col2 = st.columns(2)
                st.number_input(label="Hours Shift:", value=st.session_state.days_add, key='days_add')
                with col1:
                    st.subheader("Impact")
                    st.checkbox("🟡", value=st.session_state.is_yellow, key='is_yellow')
                    st.checkbox("🟠", value=st.session_state.is_orange, key='is_orange')
                    st.checkbox("🔴", value=st.session_state.is_red, key='is_red')
                with col2:
                    st.subheader("Currency")
                    col1_1, col2_2 = st.columns(2)
                    with col1_1:
                        st.checkbox("AUD", value=st.session_state.is_aud, key='is_aud')
                        st.checkbox("CAD", value=st.session_state.is_cad, key='is_cad')
                        st.checkbox("CHF", value=st.session_state.is_chf, key='is_chf')
                        st.checkbox("CNY", value=st.session_state.is_cny, key='is_cny')
                        st.checkbox("EUR", value=st.session_state.is_eur, key='is_eur')
                    with col2_2:
                        st.checkbox("GBP", value=st.session_state.is_gbp, key='is_gbp')
                        st.checkbox("JPY", value=st.session_state.is_jpy, key='is_jpy')
                        st.checkbox("NZD", value=st.session_state.is_nzd, key='is_nzd')
                        st.checkbox("USD", value=st.session_state.is_usd, key='is_usd')
        save_api = st.button('Save Settings', use_container_width=True)            
        parse_data = st.button("Parse Data to Notion", use_container_width=True)
        if save_api:
            save_settings()
            info_placeholder = st.info(f'''Your Settings:  
                                       DB Name: {backend.get_page_name(st.session_state.token, st.session_state.db_id)},  
                                       impact({st.session_state.impact_filter}),  
                                       currency({st.session_state.currency_filter}).  
                                       Now you can parse data to notion''', icon="✅")
        if parse_data:
            ids = backend.create_pages_and_return_list_of_ids(st.session_state.token, st.session_state.db_id, st.session_state.impact_filter, st.session_state.currency_filter, st.session_state.days_add)
        st.success('''Author: https://github.com/klimasevskiy  
                      How to use: https://youtu.be/6Fr4sdUvYPs''', icon='🙃')
load_tabs()