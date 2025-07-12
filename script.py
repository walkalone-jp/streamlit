import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

# Streamlit UI 設定
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

        # Pygwalker Streamlit専用レンダラ
        pyg_app = StreamlitRenderer(df)
        pyg_app.explorer()

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
