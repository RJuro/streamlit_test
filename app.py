import streamlit as st
import streamlit.components.v1 as components
import time
import numpy as np
import pandas as pd


st.set_page_config(page_title='DeBJARNEfy',
page_icon="😈",
layout='wide')

norm = pd.read_csv('norm.csv')
norm.columns = ['Activity','Senior','Junior']
norm.index = norm.Activity

st.sidebar.header("Who are you and what did you do? 🤓")

level = st.sidebar.selectbox('Select your level?', ['Senior','Junior'])
activities = st.sidebar.multiselect("What did you do?", norm['Activity'].unique() )

hours = []
for i in range(len(activities)):
     _ = st.sidebar.number_input(activities[i],step=1)
     hours.append(_)


hours_cours = sum(norm.loc[activities,level].values * np.array(hours))



'''
# Calculating some hours 🧮️

'''

calculated = st.button(label="Calculate - Bip-Bap-Bup")
if calculated:
    if hours_cours < 5:
        st.header(f'{hours_cours} hourses - meh! Teach more!')
    else:

        st.header(f'{hours_cours} hourses - well done 🚀')
        components.html("""
        <iframe src="https://giphy.com/embed/BYoRqTmcgzHcL9TCy1" 
        width="477" height="480" frameBorder="0" class="giphy-embed" 
        allowFullScreen></iframe><p>
        <a href="https://giphy.com/gifs/thank-you-thanks-thumbs-up-BYoRqTmcgzHcL9TCy1">via GIPHY</a></p>""", height=800)


# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

#st.table(norm)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
#st.button("Re-run")