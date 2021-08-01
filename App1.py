import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.title('Food Demand Forecasting')


@st.cache
def load_data(nrows):
    data = pd.read_csv('train.csv', nrows=nrows)
    return data


@st.cache
def load_center_data(nrows):
    data = pd.read_csv('fulfilment_center_info.csv', nrows=nrows)
    return data


@st.cache
def load_meal_data(nrows):
    data = pd.read_csv('meal_info.csv', nrows=nrows)
    return data


data_load_state = st.text('Loading data...')
weekly_data = load_data(1000)
center_info_data = load_center_data(1000)
meal_data = load_meal_data(1000)

#BAR CHART
st.subheader('Weekly Demand Data')
st.write(weekly_data)
st.bar_chart(weekly_data['num_orders'])

#HISTOGRAM
df=pd.DataFrame(weekly_data[:200],columns=['num_orders','checkout_price','base_price'])
df.hist()
plt.show()
st.pyplot()

#LINE CHART
st.line_chart(df)

#AREA CHART
chart_data=pd.DataFrame(weekly_data[:40], columns=['num_orders','base_price'])
st.area_chart(chart_data)

st.subheader('Fulfillment Center Information')
if st.checkbox('Show Center Information data'):
    st.subheader('Center Information data')
    st.write(center_info_data)
#st.write(center_info_data)

st.bar_chart(center_info_data['region_code'][:40])
st.bar_chart(center_info_data['center_type'][:10])


#DISTRIBUTION

hist_data=[center_info_data['center_id'],center_info_data['region_code']]
group_labels=['Center Id', 'Region Code']
fig= ff.create_distplot(hist_data, group_labels, bin_size=[10,25])
st.plotly_chart(fig, use_container_width=True)

st.subheader('meal Information')
st.write(meal_data)

st.bar_chart(meal_data['cuisine'][:10])

agree=st.button('Click to view meal categories')
if agree:
    st.bar_chart(meal_data['category'][:10])
