import streamlit as st

st.set_page_config(page_title="テストアプリ")

st.sidebar.radio("利用目的を選んでください", ["社内文書検索", "社内問い合わせ"])

st.write("メイン画面です")

