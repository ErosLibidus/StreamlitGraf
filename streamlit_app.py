from doctest import DONT_ACCEPT_TRUE_FOR_1
import imp
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
import psycopg2
import os 
import xlrd
import openpyxl
from PIL import Image
from funiconGraf import tipoenerW, tipoenerA, barPlot, lineal2Plot, tipoenerB, lineal2Plot2, linealTwh, emisionco2, emisionco_22, mapa, co2Menos, co2menostab

# #0DF205
# #A7F235


with st.sidebar:
    choose = option_menu("Menu", ["Inicio", "Gráficos"],
                         icons=['house', "house"],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "8!important", "background-color": "#202022"},
        "icon": {"color": "#0DF205", "font-size": "15px"}, 
        "nav-link": {"font-size": "18px", "text-align": "down", "margin":"0px", "--hover-color": "#363333"},
        "nav-link-selected": {"background-color": "#B4D930"},
    }
    )

if choose == "Inicio":
    #st.title("Emission Map")
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color:#A7F235;} 
    </style> """, unsafe_allow_html=True)
    col1, col2 = st.columns([2,0.8])
    logo = Image.open("archivos/logo_imagen.png")
    logo1 = Image.open("archivos/logo_letra.png")
    with col1:
        st.image(logo1, width=500)
    with col2:
        st.image(logo, width=100)

    st.markdown('<p class="font">Emisiones de CO2 hoy</p>', unsafe_allow_html=True)
    #st.header("Emisiones de CO2 hoy")
    fig = mapa()
    st.plotly_chart(fig)

if choose == "Gráficos":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color:#A7F235;} 
    </style> """, unsafe_allow_html=True)
    
    
    st.markdown('<p class="font">Energía</p>', unsafe_allow_html=True)
    tab1, tab5= st.tabs(["Consumo de energía", "Consumo de energía por país"])
    with tab1:
        fig = tipoenerW()
        st.plotly_chart(fig)
    
    with tab5:
        fig5 = tipoenerB()
        st.plotly_chart(fig5)



    st.markdown("----")

    st.markdown('<p class="font">Emisiones</p>', unsafe_allow_html=True)
    tab6, tab3 = st.tabs(["Emisiones CO2 mayores", "Tabla Mayor"])
    with tab6:
        fig7 = emisionco2()
        st.plotly_chart(fig7)
    with tab3:
        df1 = emisionco_22()
        st.table(df1)
        
        

    
    tab7, tab2 = st.tabs(["Emisiones CO2 menores", "Tabla Menor"])
    with tab7:
        fig10 = co2Menos()
        st.plotly_chart(fig10)
    with tab2:
        df2 = co2menostab()
        st.table(df2)

    st.markdown("----")
    
    st.markdown('<p class="font">CO2</p>', unsafe_allow_html=True)
    tab4, tab5 = st.tabs(["Huella Ecologica vs Biocapacidad PerCap", "CO2 vs Temperatura"])
    with tab4:
        fig4 = lineal2Plot()
        st.plotly_chart(fig4)  
    with tab5:
        fig7 = lineal2Plot2()
        st.plotly_chart(fig7)








