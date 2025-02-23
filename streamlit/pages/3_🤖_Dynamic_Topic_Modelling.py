import streamlit as st
from streamlit import components


#topic_results = topic_model.get_topic_info()
#st.write(topic_results)

#topic_dist_map = topic_model.visualize_topics()
#st.write(topic_dist_map)
with open('./models/document_clusters.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=1300, height=800, scrolling=False)

with open('./models/topic_barchart.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=1300, height=800, scrolling=False)

with open('./models/topics_over_time.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=1300, height=800, scrolling=False)