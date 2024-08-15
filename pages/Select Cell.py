import streamlit as st
import requests
import plotly.express as px
import pandas as pd

BASE_URL = "http://127.0.0.1:8080"

def main():
    st.set_page_config(layout="wide")
    selection = st.sidebar.selectbox(
        "Select Cell by its ID",
        (5308, 5329))
    
    endpoint = f"{BASE_URL}/read_data/{selection}"

    try:
        # Making the GET request to the API
        response = requests.get(endpoint)
        
        # Check if the response was successful
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df['absolute_time'] = pd.to_datetime(df['absolute_time']).dt.strftime('%Y-%m-%d %H:%M:%S')

            print_charts(df)
        elif response.status_code == 404:
            st.error("Data not found")
        else:
            st.error(f"Error: {response.status_code}, {response.json()}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

   
def print_charts(df):
    fig1 = px.line(df,x='absolute_time', y='voltage_v',height=300,width=450,color_discrete_sequence=["#ff97ff"])
    fig1.update_layout(title='Time v. Voltage',xaxis_title="Time", yaxis_title="Voltage (V)", title_x=0.5)

    fig2 = px.line(df,x='absolute_time', y='curent_mA',height=300,width=450,color_discrete_sequence=["#00ffff"])
    fig2.update_layout(title='Time v. Current',xaxis_title="Time", yaxis_title="Current (mA)", title_x=0.5)

    fig3 = px.line(df,x='absolute_time', y='auxilary_channel_TU1_temperature',height=300,width=450,color_discrete_sequence=["#F68A8A"])
    fig3.update_layout(title='Time v. Temperature',xaxis_title="Time", yaxis_title="Temperature (*C)", title_x=0.5)

    fig4 = px.line(df,x='absolute_time', y='capacity_mAh',height=300,width=450,color_discrete_sequence=["#8AF6AA"])
    fig4.update_layout(title='Time v. Capacity',xaxis_title="Time", yaxis_title="Capacity (mAh)", title_x=0.5)


    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2) 

    con1 = c1.container(border=True)
    con2 = c2.container(border=True)
    con3 = c3.container(border=True)
    con4 = c4.container(border=True)

    with st.container():
        con1.plotly_chart(fig1)
        con2.plotly_chart(fig2)
        con3.plotly_chart(fig3)
        con4.plotly_chart(fig4)


if __name__=="__main__":
    main()
