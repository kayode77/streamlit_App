import streamlit as st    # web development
import numpy as np
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff
import base64

st.set_page_config(
    page_title='Interactive Dashboard',
    page_icon='⏳',
    layout='wide')
st.header('Dashboard Display of Population and GDP Rate')
st.markdown("""
<style>
.css-opdfv4.e1ewe7hr3
{
  visibility:hidden;
}
.css-lnea4b.e1g8pov61         
{
  visibility:hidden;
}
</style>
""",unsafe_allow_html=True)
df = pd.read_csv('PRO.csv')

# Adding background to the side bar
def sidebar_bg(side_bg):
   side_bg_ext = 'jpg'
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = 'image2.jpg'
sidebar_bg(side_bg)

nav=st.sidebar.radio('Choose your options below',options=('Description of the Table','Interactive Plots'))
if nav == 'Description of the Table':
   if st.checkbox('Show Description'):
      st.subheader('Population Growth')
      st.write('Population growth refers to the increase in the number of individuals in a population over time. It is typically measured as a percentage increase in the population size over a specific period. Population growth is a key demographic indicator and has significant implications for various aspects of society, including economic development, social services, and environmental sustainability.')
      st.image('images.jpeg',caption="image of GDP",width=500)
      st.subheader('The overview of the table')
      if st.checkbox('The Table'):
        st.table(df.head(6)) 
      st.subheader('The description of the above dataset')
      if st.checkbox('The Description'):
        st.write(df.describe())


if nav == 'Interactive Plots':
    Graph=st.selectbox('Types of interactive graph',options=('Population/Year','Total_GDP','GDP Value','Density Plot'))
    if Graph == 'Population/Year':
      trace_Population = go.Bar(x=df.Year, y=df.Population_Total)
      data = [trace_Population]
      layout=go.Layout(title="Total Population verses Year")
      fig = plotly.subplots.make_subplots(rows=1,cols=1)
      fig.add_trace(trace_Population,row=1,col=1)
      fig.update_layout(height=500, width=600,title="Population over the years",
                        xaxis=dict(title='Year'),yaxis=dict(title='Total Population'))
      st.write(fig)
    elif Graph == 'Total_GDP':
      df['logTotal_GDP']=df['Total_GDP'].apply(np.log)
      trace_GDP = go.Bar(x=df.Year,y=df['logTotal_GDP'], yaxis='y')
      data = [trace_GDP]
      layout=go.Layout(title="Total GDP verses Year")
      fig = plotly.subplots.make_subplots(rows=1,cols=1)
      fig.add_trace(trace_GDP,row=1,col=1)
      fig.update_layout(height=500, width=600,title="Total GDP over the years",
                xaxis=dict(title= 'Year'),yaxis=dict(title='logTotal_GDP'))
      st.write(fig)
    
    elif Graph == 'Density Plot':
       x=df.Year
       y=df.Total_GDP
       fig = ff.create_2d_density( x, y)
       fig.update_layout(height=500, width=600,title="Density plot")
       st.plotly_chart(fig)
  
    else:
      x=df.Total_GDP
      data=go.Box(x=x,boxpoints='suspectedoutliers', boxmean='sd')
      layout=go.Layout(title="Total GDP value")
      fig=go.Figure(data, layout)
      st.plotly_chart(fig)
