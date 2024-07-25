import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from plotly.subplots import make_subplots
from plotly import graph_objects as go

import time


#####################################################################################################################
### LOADING FILES

# LOAD DATAFRAME FUNCTION
# @st.cache_data
# def load_data(path):
#     df = pd.read_csv(path)
#     return df

# # LOAD GEIJASON FILE
# with open("data/arcs_json.geojson") as response:
#     arcs_json = json.load(response)

# with open("data/intersections_json.geojson") as response:
#     intersections_json = json.load(response)

# with open("data/sinkNodes_json.geojson") as response:
#     sinkNodes_json = json.load(response)


# houses = load_data("data/houses.csv")


#####################################################################################################################


import streamlit as st
import streamlit.components.v1 as components

# List of HTML files
html_files = ['data/test_0.html', 'data/test_1.html', 'data/test_2.html', 'data/test_3.html', 'data/test_4.html']

# Initialize session state if it doesn't exist
if 'current_phase' not in st.session_state:
    st.session_state.current_phase = 0

# Title
st.title("Mission Canyon Evacuation Optimization")




# Navigation buttons and current phase text
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button('Previous Phase', key='prev', help='Go to the previous phase. It might take some time.', type="secondary", use_container_width=True):
        if st.session_state.current_phase > 0:
            st.session_state.current_phase -= 1
with col3:
    if st.button('Next Phase', key='next', help='Go to the next phase. It might take some time.', type="primary", use_container_width=True):
        if st.session_state.current_phase < len(html_files) - 1:
            st.session_state.current_phase += 1




with col2:
    # Display the current phase in the middle column
    st.markdown(f"<p style='text-align: center;'>Current Phase: {st.session_state.current_phase+1} of 5</p>", unsafe_allow_html=True)



# Read and display HTML content based on the current phase
current_file = html_files[st.session_state.current_phase]
with open(current_file, 'r') as file:
    html_content = file.read()

components.html(html_content, width=1500, height=1200)















# tt = st.slider("Timesteps: 10 seconds interval", 0, 97, 0)

# print(tt)

# # if st.button('animate'):
# #     for x in range(97-tt):
# #         time.sleep(.5)
# #         # This API will take a little more work. 
# #         # Probably a couple more months after that.
# #         tt = st.slider("Timesteps: 10 seconds interval", 0, 97, tt)



# st.write("At step ", tt)

# fig = go.Figure()
# step_l = 6

# pl_deep=[[0.0, 'lightgrey'],
#          [0.1, 'rgb(0,153,0)'],
#          [0.2, 'rgb(0,204,0)'],
#          #[0.3, 'rgb(102, 194, 163)'],
#          [0.4, 'rgb(102,255,102)'],
#          [0.5, 'rgb(255,102,102)'],
#          [0.6, 'rgb(255,51,51)'],
#          [0.7, 'rgb(255,0,0)'],
#          [0.8, 'rgb(204,0,0)'],
#          #[0.9, 'rgb(153,0,0)'],
#          [1.0, 'rgb(153,0,0)']]
# MaxFlow=10


# #for tt in range(5):

# print(tt)

# arcs = load_data(f"data/arcs_{tt}.csv")
# intersections = load_data(f"data/intersections_{tt}.csv")
# sinkNodes = load_data(f"data/sinkNodes_{tt}.csv")

# flow_arcs = arcs.loc[arcs["value"] > 0]
# non_flow_arcs = arcs.loc[arcs["value"] == 0]

# departed_houses = houses.loc[houses.depart_time < tt]
# departing_houses = houses.loc[houses.depart_time == tt]
# to_depart_houses = houses.loc[houses.depart_time > tt]


# fig.add_trace(go.Choroplethmapbox(geojson=arcs_json, locations= non_flow_arcs['index'], z=non_flow_arcs["value"],
#                                     marker_opacity=1, marker_line_width=0,
#                                     colorscale=[[0, "lightgrey"], [1, "lightgrey"]],
#                                     visible=True, name="No Flow", 
#                                     colorbar=dict(
#                                         tickvals=[],  # Empty list to disable tick values
#                                         ticks="",     # Empty string to disable tick labels
#                                         ticktext=[],   # Empty list to disable tick text
#                                         x=0.85,  
#                                         y=0.5
#                                     )))

# fig.add_trace(go.Choroplethmapbox(geojson=arcs_json, locations= flow_arcs['index'], z=flow_arcs["value"],
#                                     colorscale=pl_deep, zmin=0, zmax=MaxFlow,
#                                     marker_opacity=1, marker_line_width=0,
#                                     visible=True, name="Flow",
#                                     colorbar=dict(
#                                         x=0.85,       # Adjust x position of the colorbar
#                                         y=0.5         # Adjust y position of the colorbar
#                                     )))

# fig.add_trace(go.Choroplethmapbox(geojson=intersections_json, locations= intersections.index, z=intersections["value"],
#                                     colorscale=pl_deep, zmin=0, zmax=MaxFlow,
#                                     marker_opacity=1, marker_line_width=0.5,
#                                     visible=True, name="Intersection",
#                                     colorbar=dict(
#                                         x=0.85,       # Adjust x position of the colorbar
#                                         y=0.5         # Adjust y position of the colorbar
#                                     )))

# fig.add_trace(go.Choroplethmapbox(geojson=sinkNodes_json, locations= sinkNodes.index, z=sinkNodes["value"],
#                                     colorscale=pl_deep, zmin=0, zmax=MaxFlow,
#                                     marker_opacity=1, marker_line_width=2,
#                                     visible=True, name="Sink Nodes",
#                                     colorbar=dict(
#                                         x=0.85,       # Adjust x position of the colorbar
#                                         y=0.5         # Adjust y position of the colorbar
#                                     )))


# #     fig.add_trace(go.Scattermapbox(
# #             lat=departed_houses.geometry.y.values,  # Latitude data
# #             lon=departed_houses.geometry.x.values,  # Longitude data
# #             marker=dict(color="slategrey"), #fillcolor="slategrey",
# #             hoverinfo="none",
# #             visible=False, name="Departed house"
# #         ))

# fig.add_trace(go.Scattermapbox(
#         lat=departing_houses.lat,  # Latitude data
#         lon=departing_houses.lon,  # Longitude data
#         marker=dict(color="cyan"),#fillcolor="cyan",
#         hoverinfo="none",
#         visible=True, name="Departing house"
#     ))
# fig.add_trace(go.Scattermapbox(
#         lat=to_depart_houses.lat,  # Latitude data
#         lon=to_depart_houses.lon,  # Longitude data
#         marker=dict(color="cadetblue"),#fillcolor="cadetblue",
#         hoverinfo="none",
#         visible=True, name="To depart house"
#     ))



# # # Make 10th trace visible
# # for i in range(step_l):
# #     fig.data[i].visible = True



# # Create and add slider
# # steps = []
# # for i in range(len(fig.data)//step_l):
# #     step = dict(
# #         method="update",
# #         args=[{"visible": [True if (_ // step_l) == i else False for _ in range(len(fig.data))]},
# #                 {"title": "Time slider at time: " + str(i)}],  # layout attribute
# #         label="step" + str(i)
# #     )
# #     steps.append(step)


# # sliders = [dict(
# #     active=0,
# #     currentvalue={"prefix": "Time: "},
# #     pad={"t": 50},
# #     steps=steps
# # )]

# # fig.update_layout(
# #     sliders=sliders
# # )
# fig.update_layout(mapbox_style="carto-positron", #"open-street-map", # carto-positron
#                     mapbox_zoom=14, mapbox_center = {'lat':34.45498105, 'lon':-119.71694685}, width=1300,  height=1000)

# st.plotly_chart(fig)



