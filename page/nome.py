import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(["pagina 1", "pagina 2", "pagine 3"])

tab1.write("""## Primeira pagina""")

df = pd.read.csv("")
tab2.line_char(df, x="linguagem", y= "desenvolvedores")

with tab2:
    st.video(https://www.youtube.com/watch?v=5kc0ysogL6c)
             
with tab3:
    
    