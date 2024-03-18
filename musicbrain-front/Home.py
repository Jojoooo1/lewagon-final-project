import streamlit as st
from graphviz import Digraph


st.set_page_config(page_title = "MusicBrain app")

st.header("Classifying The Brain on Music")
st.subheader("Machine Learning for Brain Music Classification")

# st.header("Contextualizing our project")
# st.subheader("Why create a model to classify music genres from brain images?")

# Define text for each box or step
text_box1 = "Decoding models"
text_box2 = '''**Applications:**
            neuroscience, psychology, and diagnostic medicine'''
text_box3 = "**Understanding the brain**: advancements in technology and its application in medicine, psychology, bioengineering and so on"

# Define the layout for the flow chart using columns
col1, col2, col3 = st.columns(3)

# Place text in each box
with col1:
    st.info(text_box1)

with col2:
    st.info(text_box2)

with col3:
    st.info(text_box3)


st.image("https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41598-022-27361-x/MediaObjects/41598_2022_27361_Fig6_HTML.png?as=webp", caption="Analysis pipeline illustration from the original study. / Daly, I. Neural decoding of music from the EEG. Sci Rep 13, 624 (2023). https://doi.org/10.1038/s41598-022-27361-x")

st.subheader("Objective")

st.markdown('''For our project the data was already ready to be used in our model.The contextualization above was to clarify from **where** the information that we
            used came from and also for **better understanding** of why our project is ***impactful***.
            ''')

st.markdown('''The objective of our project is to classify fMRI brain images
            taken while listening to music in five different genres:
            **label 0=Ambient Music, 1=Country Music, 2=Heavy Metal, 3=Rock 'n Roll, 4=Classical Symphonic**.''')


st.markdown('''Our model will **predict**, using only the given brain images -  already preprocessed and vectorized -  the correct genre labels (0-4) for the 40 test trials.''')


# flowchart
def main():
    st.title('Basic Project Flowchart')
    st.write('Find below a simple flowchart of our project.')

    # Create a new Digraph
    dot = Digraph()

    # Define nodes
    dot.node('A', 'Input data')
    dot.node('B', 'Preprocessing')
    dot.node('C', 'Model Training: logistic regression')
    dot.node('D', 'Output: predicted labels')

    # Define edges
    dot.edges(['AB', 'BC', 'CD'])

    # Render the flowchart
    st.graphviz_chart(dot)

if __name__ == '__main__':
    main()
