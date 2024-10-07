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
from data import dash_prep as dp
from st_aggrid import AgGrid, GridOptionsBuilder

def show_charts():
    
    m = dp.metrics_prep()
    m1 = m.m1
    m2 = m.m2
    m3 = m.m3
    m4 = m.m4
    
    fig_m1 = go.Figure()
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")