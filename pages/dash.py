import requests
import pandas as pd
import numpy as np
import math
import prettytable
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import plotly.graph_objects as go
from streamlit_navigation_bar import st_navbar
from st_aggrid import AgGrid, GridOptionsBuilder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
import dash_prep as dp


def show_dash():
    m = dp.metrics_prep()
    m1 = m.m1
    m2 = m.m2
    m3 = m.m3
    m4 = m.m4
    
    fig_m1 = go.Figure()
    st.metric(label="Total Number of Issues", value=m1)

    fig_m2 = go.Figure()
    st.metric(label="Total Number of Issues", value=m1)



    # Display the plots in Streamlit using columns
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_m1, use_container_width=True)

    with col2:
        
         st.plotly_chart(fig_m2, use_container_width=True)
        
        # Second row with two columns
    # col3, col4 = st.columns(2)
    
    # with col3:
    #     st.plotly_chart(fig_m3, use_container_width=True)

    # with col4:
    #     st.plotly_chart(fig_m4, use_container_width=True)



    
# cd /Users/t0l0bkk/Documents/TTL/github/survey-tool/
# streamlit run streamlit_run.py 