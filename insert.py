import streamlit as st
import mysql.connector
from mysql.connector import Error
import json
import pandas as pd

def insert_money():
    st.title('오늘은 얼마나 저금하셨나요?')

    column_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    choice=st.selectbox('요일을 선택하세요',column_list)

    for choice_list in column_list:
        if choice_list==choice:
            saved_money=st.number_input('입력해주세요',min_value=0)
    
       
    
    if st.button('저장'):
        st.write('오늘 '+str(saved_money)+'원 저금하였습니다.')

        try:

            connection=mysql.connector.connect(
                host= 'database-1.c2djwdwt1ijq.ap-northeast-2.rds.amazonaws.com',   
                database='yhdb',
                user='Streamlit',
                password='jinwoo510'
                )

            if connection.is_connected():
                cursor=connection.cursor(dictionary=True)


                query="""insert into money_library(%s) values(%s);"""

                data=(choice,saved_money)

                cursor.execute(query,data)

                connection.commit()
        
        except Error as e:
            print('디비 관련 에러 발생',e)

        finally:
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')
            



if __name__=='__main__':
    main()