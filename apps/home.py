import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Streamlit for Geospatial Applications")

    st.markdown(
        """
        This multi-page web app demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and open-source mapping libraries, 
        such as [leafmap](https://leafmap.org), [geemap](https://geemap.org), [pydeck](https://deckgl.readthedocs.io), and [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter).
        
        For Creating these time lapse go to: [TimeLapse](https://colab.research.google.com/drive/1VwDgdNiWK_U9Ovtd_Yzce93i_zwtKqPw?usp=sharing)
        """
    )

    st.info("Click on the left sidebar menu to navigate to the different apps.")

    st.subheader("Timelapse of Satellite Imagery")
    st.markdown(
        """
        The following timelapse animations were created using the Timelapse web app. Click `Create Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
    """
    )

    
    st.image("https://github.com/Akshat-kumar-jain/GeoSpatial_Stramlit/blob/main/132a2fee227448bf0e55995718e0fb77-89a1f02b89cab10ef8f63e140be40dde_getPixels%20(4).gif")
    st.image("https://github.com/Akshat-kumar-jain/GeoSpatial_Stramlit/blob/main/6cab6d96-4f7d-4819-a31e-ada7e283622f%20(1).gif")

    
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
