import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")
st.title('Exploratory data analysis for tips')

st.write("""
  Всем привет! Я сделал сайт с анализом данных, собранных одним официантом. [ссылка на сам код](https://github.com/SSanchay/example) 
\n Данный стримлит предназначен для наглядной демонстрации простого способа разведочного анализа данных (Exploratory data analysis - EDA) на примере данных tips.csv.
\n **Данные**: [tips.csv](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv)
""")

#Читаем датасет в tips
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)

st.subheader('Посмотрим на данные')



#--------------------- Покажем сам датасет ------------------------



row1_space1, row1_1, row1_space2, row1_2, row1_space3, row1_3, row1_space4 = st.columns((.1, 1, .1, 1, .1, 1, .1))
with row1_1:
    if st.checkbox('Показать данные'):
        st.dataframe(tips.head())
with row1_2:
    # Выведем название всех столбцов (features)
    if st.checkbox('Название столбцов'):
        st.write(pd.DataFrame(tips.columns, columns = ['Columns name']))
with row1_3:
    #Выведем типы данных датасета
    if st.checkbox('Типы данных'):
        st.write(pd.DataFrame(tips.dtypes.astype('str'), columns=['Columns type']))



#--------------------- Строим графики ------------------------------



st.subheader('Строим графики')


### Гистограммы распределений Total bill и Tip

row2_space1, row2_1, row2_space2, row2_2, row2_space3 = st.columns((.1, 1, .1, 1, .1))

with row2_1:
    st.subheader('Распределение счета (total bill)')
    fig, ax = plt.subplots()
    fig = plt.figure()
    ax = sns.histplot(data = tips, x = tips['total_bill'], bins = 30, kde = True)
    ax.set_xlabel('Total bill')
    sns.set(style='darkgrid')
    st.pyplot(fig)

with row2_2:
    st.subheader("Распределение чаевых (tip) в ланч и обед (time)")
    fig, ax = plt.subplots()
    fig = plt.figure()
    ax = sns.histplot(tips, y = 'tip', hue = 'time', multiple='dodge', kde = True)
    ax.set(
        xlabel = 'Count',
        ylabel = 'Tip'
    )
    sns.set(style='darkgrid')
    st.pyplot(fig)

st.markdown('Заметно, что люди часто кушают в районе 10-20 долларов и оставляют чаевых на от 1 до 6 долларов.\
     График показывает, что распределение счета является более нормальным, чем чаевых.')


### Графики scatterplot, показывающие связь Total bill и Tip

row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns((.1, 1, .1, 1, .1))

with row3_1:
    st.subheader('Связь между размером счета (total bill) и чаевых(tip)')
    fig, ax = plt.subplots() 
    ax = sns.scatterplot(x = 'tip', y = 'total_bill', hue='sex', data=tips)
    ax.set(
        xlabel = 'tip',
        ylabel ='Total bill'
    )
    sns.set(style='darkgrid')
    st.pyplot(fig)

with row3_2:
    st.subheader('Связь между размером счета (total bill), чаевых (tip) и количеством людей (size)')
    fig, ax = plt.subplots() 
    ax = sns.scatterplot(x = 'tip', y = 'total_bill', size = 'size', data = tips)
    ax.set(
        xlabel = 'tip',
        ylabel ='Total bill'
    )
    sns.set(style='darkgrid')
    st.pyplot(fig)

st.markdown('Связь между счетом и "минимальным" чаевым является линейным.\
     И в основном мужчины платят больше женщин и также небольшие группы тратят не больше 25 долларов и оставляют не больше 4 долларов.')


### Графики scatterplot, показывающие связь между размером счета (Total bill), чаевых (Tip) и курящим клиентом (Smoker)

row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns((.1, 1, .1, 1, .1))

with row4_1:
    st.subheader('Связь между размером счета (Total bill), чаевых (Tip) и курящим клиентом-женщиной (Smoker)')
    fig, ax = plt.subplots() 
    ax = sns.scatterplot(data = tips[tips['sex'] == 'Female'], x = 'tip', y = 'total_bill', hue = 'smoker')
    ax.set(
        xlabel = 'Tip',
        ylabel ='Total bill'
    )
    sns.set(style='darkgrid')
    st.pyplot(fig)

with row4_2:
    st.subheader('Связь между размером счета (Total bill), чаевых (Tip) и курящим клиентом-мужчиной (Smoker)')
    fig, ax = plt.subplots() 
    ax = sns.scatterplot(data = tips[tips['sex'] == 'Male'], x = 'tip', y = 'total_bill', hue = 'smoker')
    ax.set(
        xlabel = 'Tip',
        ylabel ='Total bill'
    )
    sns.set(style='darkgrid')
    st.pyplot(fig)

st.markdown('Связь между размером счета и чаевых среди некурящих клиентов является линейным и размер чаевых можно легко найти, если знать на сколько они закажут еду.\
    А курящие клиенты могут оставить меньше чаевых несмотря на то, что они могут заказывать на такую же сумму, как и некурящие клиенты.')


### Графики scatterplot, показывающие связь между днем недели (day) и размерами счета (Total bill) и чаевых (Tip)

row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns((.1, 1, .1, 1, .1))

with row5_1:
    st.subheader('Связь между размером счета (total bill) и днем недели (day)')
    fig, ax = plt.subplots()
    ax = sns.scatterplot( x = 'day', y = 'total_bill', data=tips, hue='size')
    ax.set(
        xlabel = 'day',
        ylabel ='Total bill'
    )
    sns.set(style='darkgrid')
    st.pyplot(fig)

with row5_2:
    st.subheader('Связь между размером чаевых (tip) и днем недели (day)')
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x = 'tip', y = 'day', hue = 'sex', data = tips)
    ax.set(
        xlabel = 'Tip',
        ylabel ='Day'
    )
    sns.set(style='darkgrid')
    st.pyplot(fig)

st.markdown('Заметим, что наш оффициант записывал данные только с середины недели. В пятницу меньше всего клиентов приходят, чем в выходные и в четверг, \
    и только по-одному. Также клиенты заказывают от 10 до 40 долларов равномерно и по-одному. Если бы добавили еще с детьми приходят или нет, то можно было \
    определить семейным является кафе или нет.')

### График формы распределения BoxPlot с суммой всех счетов (Total bill) и чаевых (Tip) за каждый день (day)

row6_space1, row6_1, row6_space2, row6_2, row6_space3 = st.columns((.1, 1, .1, 1, .1))

with row6_1:
    st.subheader('График формы распределения "ящик с усами" с суммой всех счетов (Total bill) за каждый день (day)')
    fig, ax = plt.subplots() 
    fig = plt.figure()
    plt.ticklabel_format(style='plain')
    ax = sns.boxplot(x = 'day', y = 'total_bill', hue = 'time', data = tips)
    st.pyplot(fig)

with row6_2:
    st.subheader('График формы распределения "ящик с усами" с суммой всех чаевых (Tip) за каждый день (day)')
    fig, ax = plt.subplots() 
    fig = plt.figure()
    plt.ticklabel_format(style='plain')
    ax = sns.boxplot(x = 'day', y = 'tip', hue = 'time', data = tips)
    st.pyplot(fig)

st.write('*BoxPlot* - показывает медиану (линия внутри ящика), нижний (25%) и верхний квартили(75%),\
     минимальное и максимальное значение выборки (усы) и ее выбросы.')
expander_bar = st.expander('Подробнее о квартиле')
expander_bar.info(''' 
Квартили -  значения, которые делят данные на 4 группы (25%,50%,75%,100%), содержащие приблизительно равное количество наблюдений. 
\nПо сути, это то же самое, что и перцентиль. То есть нижний квартиль - 25 перцентиль, а верхний квартиль - 75 перцентиль
''')



