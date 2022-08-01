import streamlit as st

st.title('アレルギー発見ツール')
st.caption('これはアレルギー成分を成分表から見つけるツールです')
ale = st.text_input("指定する成分") #引数に入力内容を渡せる
zen = st.text_area('全成分')  #引数に入力内容を渡せる

Button = st.button("実行")
if Button:

    if ale in zen:
        st.markdown(f'## この商品には{ale}が入っています。')
    
    else:
        st.markdown(f'## この商品に問題の成分は入っていません。')  