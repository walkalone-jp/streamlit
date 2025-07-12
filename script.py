import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components
from pathlib import Path

# Streamlit UI
st.set_page_config(page_title="CSV EDA Viewer", layout="wide")
st.title("CSV EDA Viewer with Pygwalker")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロード", type=["csv"])

if uploaded_file is not None:
    # CSV読み込み
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"CSVの読み込みに失敗しました: {e}")
    else:
        st.success("CSVの読み込みに成功しました")

        # PygwalkerのHTML生成
        html_content = pyg.to_html(df)

        # ライトモード強制CSS
        light_mode_css = """
        <style>
            :root {
                color-scheme: light !important;
            }
            body[data-theme="dark"] {
                background: white !important;
                color: black !important;
            }
        </style>
        """

        # 結合して表示
        full_html = light_mode_css + html_content
        components.html(full_html, height=800, scrolling=True)

        # df.head() 結果表示
        st.markdown("---")
        st.markdown('<span style="font-size: 16px;"><b>冒頭５行 (df.head())</b></span>', unsafe_allow_html=True)
        st.dataframe(df.head())

        # describe() 結果表示
        st.markdown("---")
        st.markdown('<span style="font-size: 16px;"><b>統計概要 (df.describe())</b></span>', unsafe_allow_html=True)
        st.dataframe(df.describe(include='all'))

else:
    st.info("CSVファイルをアップロードしてください")
