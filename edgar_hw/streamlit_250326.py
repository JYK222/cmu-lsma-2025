import streamlit as st
import pydeck as pdk

st.title("Simple Streamlit Map Example (CMU, Pittsburgh)")

# Define the initial viewport location for CMU, Pittsburgh
initial_view = pdk.ViewState(
    latitude=40.4444,
    longitude=-79.9436,
    zoom=14,   # 원하시는 확대 레벨에 따라 조정 가능
    pitch=0
)

# Example data (just a single point near CMU)
data = [
    {"name": "CMU Campus", "position": [-79.9436, 40.4444]}
]

# Define a pydeck layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position="position",
    get_radius=200,         # 원하시는 반경에 따라 조정 (단위: 미터)
    get_fill_color=[255, 0, 0],
    pickable=True
)

# Render the deck.gl map in Streamlit
r = pdk.Deck(
    layers=[layer],
    initial_view_state=initial_view,
    tooltip={"text": "{name}"}
)

st.pydeck_chart(r)
