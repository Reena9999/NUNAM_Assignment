# Landing/ Home page with the app is executed
import streamlit as st
import plotly.express as px

def main():
    st.set_page_config(layout="wide")
    # calculating the state of health for cell 5308 and 5329 from information given in the assignment pdf
    SoH_5308=(2992.02/3000)*100
    SoH_5329=(2822.56/3000)*100

    # page header
    st.subheader("State of Health")

    # creating two pie charts to show the state of health of each battery 
    fig_5308=px.pie(values=[SoH_5308,100-SoH_5308],names=['Healthy','Degraded'],width=400,hole=.5,title="Cell 5308 State of Health" )
    fig_5329=px.pie(values=[SoH_5329,100-SoH_5329],names=['Healthy','Degraded'],width=400, hole=.5,title="Cell 5329 State of Health")

    # aligning graph title to the center
    fig_5308.update_layout(title_x=0.5)
    fig_5329.update_layout(title_x=0.5)

    # dividing page into two columns and using containers for structure in the UI
    col1, col2 = st.columns(2)
    con1 = col1.container(border=True)
    con2 = col2.container(border=True)

    # displaying the graphs
    con1.plotly_chart(fig_5308)
    con2.plotly_chart(fig_5329)


if __name__=="__main__":
    main()
