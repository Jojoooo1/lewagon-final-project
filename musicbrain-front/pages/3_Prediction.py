
# Import necessary libraries
import os
import sys
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

# Define the URL of your Fast API
BASE_URL = os.environ.get("BASE_URL")
API_URL = f"{BASE_URL}/predict/csv"

music_files = {
    0: "ambient.jpg",
    1: "country.jpg",
    2: "heavy.png",
    3: "rock.jpeg",
    4: "classical.jpg"
}

music_labels_list = [
    "Ambient Music",
    "Country Music",
    "Heavy Metal",
    "Rock 'n Roll",
    "Classical Symphonic"
]

# Create the Streamlit app
def main():

    st.title('Music Genre Classification')
    st.write('Upload a CSV file containing vectorized data to classify its music genre:')

    uploaded_file = st.file_uploader("csv", type=["csv"], label_visibility="hidden")

    if uploaded_file is not None:

        st.text("Uploading data...")
        df = pd.read_csv(uploaded_file, header=None)
        
        st.write('Data:')
        st.write(df.head())

        st.markdown("Successfully uploaded!:white_check_mark:")

        if st.button('Predict'):
            progress_bar = st.progress(0)
            
            response, time_taken = make_prediction(uploaded_file)
            st.write(f"Time taken for prediction: {time_taken:.2f} seconds")
            progress_bar.progress(100)

            if response:
                music_labels = response['music_labels'][0]
                music_labels_index = music_labels.index(max(music_labels))
                st.title('Results:')
                
                root_path = os.path.dirname(sys.argv[0])
                image_path = os.path.join(root_path, "images", music_files.get(music_labels_index))
                
                image = open(image_path, 'rb').read()
                st.image(image, width=500, use_column_width=False)

                pie_chart = px.pie(values=response['music_labels'][0], names=music_labels_list)
                st.plotly_chart(pie_chart)


def make_prediction(uploaded_file):
    start_time = time.time()
    response = requests.request("POST", API_URL, files={"file" : uploaded_file.getvalue()})

    end_time = time.time()
    prediction_time = end_time - start_time

    if response.status_code == 200:
        return response.json(), prediction_time
    else:
        return None, prediction_time

if __name__ == '__main__':
    main()