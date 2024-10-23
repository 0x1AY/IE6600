import pandas as pd
import numpy as np
import streamlit as st


st.title('Class Demo')
st.write('Summary of the Penguin Dataset')
df = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/06821bd8c94f0f1a479ed2f215e1d60ccee62cb1/data/penguins.csv')

st.table(df.describe())

# scatter chart in streamlit
st.write('Scatter Chart')
st.scatter_chart(data=df, x='flipper_length_mm', y='body_mass_g', color='species')

st.write('Line Chart')
st.line_chart(data=df,  x='flipper_length_mm', y='body_mass_g', color = 'species')

st.write('Area Chart')
st.area_chart(data=df, x='flipper_length_mm', y='body_mass_g', color = 'species')

