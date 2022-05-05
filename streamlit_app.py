import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload, vector  # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com
# Updated file

apps = {
    "home": {"title": "Home", "icon": "house"},
    "heatmap": {"title": "Heatmap", "icon": "map"},
    "upload": {"title": "Upload", "icon": "cloud-upload"},
    "vector": {"title": "Vector", "icon": "map-fill"},
}

titles = [app["title"] for app in apps.values()]
icons = [app["icon"] for app in apps.values()]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://share.streamlit.io/akshat-kumar-jain/geospatial_stramlit/main) is maintained by [Akshat Kumar Jain](https://github.com/Akshat-kumar-jain). You can follow me on social media:
            [GitHub](https://github.com/Akshat-kumar-jain) | [Twitter](https://twitter.com/AkjderB) | [LinkedIn](https://www.linkedin.com/in/akshat-kumar-jain-3a2a09132/).
        
        Source code: <https://github.com/Akshat-kumar-jain/GeoSpatial_Stramlit>

        More menu icons: <https://icons.getbootstrap.com>
    """
    )

for app in apps:
    if apps[app]["title"] == selected:
        eval(f"{app}.app()")
        break
