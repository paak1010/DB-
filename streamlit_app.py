# streamlit_app.py
import streamlit as st

# st.connection("mydb")를 호출하면, Streamlit이
# 자동으로 .streamlit/secrets.toml 파일에서 [connections.mydb] 섹션의
# 정보를 찾아 연결을 생성합니다.
conn = st.connection("mydb", type="sql")

df = conn.query("SELECT * FROM mytable;")
st.dataframe(df)