import streamlit as st
import mysql.connector
from mysql.connector import Error
import json
import pandas as pd
from insert import insert_money



def main():
    st.title('돈 저금 기록 프로그램')

    menu=['기록','변경','삭제']
    choice=st.sidebar.selectbox('메뉴',menu)

    if choice=='기록':
        insert_money()



if __name__=='__main__':
    main()