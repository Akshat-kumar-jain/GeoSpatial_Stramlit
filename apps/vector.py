import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Vector")
    
    m = leafmap.Map(center=[20, 0], zoom=1)
    lines = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
    m.add_geojson(lines, layer_name="Cable lines")
    


    m.to_streamlit(height=700)
