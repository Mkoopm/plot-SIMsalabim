from turtle import width
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


data_var = pd.read_csv('SimSS/Var.dat', delim_whitespace=True)
data_jv = pd.read_csv('SimSS/JV.dat', delim_whitespace=True)

with st.sidebar:
    options = st.multiselect(
        'Which parameters would you like to plot on the y-axis?',
        list(data_var.columns),
        ['V'])

    scale_y = ['linear','log']
    choice_y_scale = st.selectbox('y-scale', scale_y)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax2.set_yscale(choice_y_scale)
sns.scatterplot(data=data_jv, x='Vext', y='Jext', ax=ax1)
for y_var in options:
    sns.scatterplot(data=data_var, x='x', y=y_var, ax=ax2, label=y_var)


st.pyplot(fig1, format='png')
st.pyplot(fig2, format='png')