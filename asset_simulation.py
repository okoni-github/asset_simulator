import streamlit as st
import pandas as pd

radio = st.sidebar.radio(
'機能を選択してください',
('資産運用シミュレーション', '簡易収支計算'))

if radio == ('資産運用シミュレーション') :

    st.title('資産運用シミュレーション')
    st.sidebar.title('積立設定')

    tmtt_money = st.sidebar.number_input('毎月いくら積み立てますか？', 0, step = 1000)
    tmtt_year = st.sidebar.number_input('何年間積み立てしますか？', 0, step = 1 )
    re_turn = st.sidebar.number_input('年間の想定利回りはどれくらいですか？', 0.00, step = 0.1)
    answer = st.sidebar.button('計算')

    st.sidebar.write('streamlit公式サイトURL')
    st.sidebar.write('https://docs.streamlit.io/en/stable/')

    tmtt_month = tmtt_year * 12

    re_turn = (re_turn/100)/12
    tmtt_ganpon = 0
    rieki = 0
    rieki_total = 0
    unyou_total = 0
    unyou_total = unyou_total
    now_month = 1
    now_year = 1
    unyou_total += tmtt_money
    now_month += 1

    lists1 = []
    lists2 = []

    lists1.append(0)
    lists2.append(0)

    if answer == True and tmtt_money == 0 and tmtt_year == 0 :
        st.sidebar.write('積立額と積立期間の入力は必須です！')

    elif answer == True and tmtt_money == 0 :
        st.sidebar.write('もっと入金しよう！')

    elif answer == True and tmtt_year == 0 :
        st.sidebar.write('最低でも1年は積み立てよう！')

    elif answer == True :

        if re_turn == 0 :

            while now_month <= tmtt_month :
                rieki = unyou_total * re_turn
                unyou_total += rieki
                unyou_total += tmtt_money
                rieki_total += rieki

                if now_month == 12 * now_year :
                    unyou_total = round(unyou_total)

                    rieki_total = round(rieki_total)
                    lists1.append(rieki_total)

                    tmtt_ganpon = round(unyou_total) - round(rieki_total)
                    lists2.append(tmtt_ganpon)

                    now_year += 1

                now_month += 1
        
            st.sidebar.write('ただの貯金だけど大丈夫？')
            st.write(now_year - 1, '年後の資産運用額は', unyou_total, '円です')

            df = pd.DataFrame({
            '運用利益' : lists1,
            '元本合計' : lists2
            })

            st.bar_chart(df)

        else :

            while now_month <= tmtt_month :
                rieki = unyou_total * re_turn
                unyou_total += rieki
                unyou_total += tmtt_money
                rieki_total += rieki

                if now_month == 12 * now_year :
                    unyou_total = round(unyou_total)

                    rieki_total = round(rieki_total)
                    lists1.append(rieki_total)

                    tmtt_ganpon = round(unyou_total) - round(rieki_total)
                    lists2.append(tmtt_ganpon)

                    now_year += 1

                now_month += 1

            st.write(now_year - 1, '年後の資産運用額は', unyou_total, '円です')

            df = pd.DataFrame({
            '運用利益' : lists1,
            '元本合計' : lists2
            })
            
            st.bar_chart(df)
elif radio == ('簡易収支計算') :

    st.title('簡易収支計算')

    st.sidebar.title('収入入力欄')

    kyuryo = st.sidebar.number_input('毎月の給料はいくらくらいですか？', 0, step = 1000)
    bonus = st.sidebar.number_input('年間のボーナスはいくらくらいですか？', 0, step = 10000)

    st.sidebar.title('支出入力欄')

    st.sidebar.write('固定費')

    st.sidebar.write('変動費')

    answer2 = st.sidebar.button('計算')

    #left_column, right_column = st.beta_columns(2)


else :
     st.title('こんにちは')
     st.title('条件を入力して検索してください！')