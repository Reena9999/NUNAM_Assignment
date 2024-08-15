import streamlit as st
import plotly.express as px

def main():
    st.set_page_config(layout="wide")
    SoH_5308=(2992.02/3000)*100
    SoH_5329=(2822.56/3000)*100

    st.subheader("State of Health")

    fig_5308=px.pie(values=[SoH_5308,100-SoH_5308],names=['Healthy','Degraded'],width=400,hole=.5,title="Cell 5308 State of Health" )
    fig_5329=px.pie(values=[SoH_5329,100-SoH_5329],names=['Healthy','Degraded'],width=400, hole=.5,title="Cell 5329 State of Health")
    
    fig_5308.update_layout(title_x=0.5)
    fig_5329.update_layout(title_x=0.5)


    # Create two columns
    col1, col2 = st.columns(2)
    con1 = col1.container(border=True)
    con2 = col2.container(border=True)

    con1.plotly_chart(fig_5308)
    con2.plotly_chart(fig_5329)


if __name__=="__main__":
    main()
