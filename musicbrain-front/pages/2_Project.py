import streamlit as st
from graphviz import Digraph

# project description

st.title("The project")

st.header("Contextualizing our project")

st.subheader("Why create a model to classify music genres from brain images?")

st.markdown('''
            ***Neural decoding models*** aim to interpret mental states from neural activity recordings, utilizing various neuroimaging modalities such as fMRI, ECoG, EEG, and fNIRS.
            These models have been applied to decode diverse activities including affective states, visual imagery, and semantic information.
            ''')

st.markdown('''***Decoding models*** serve two main purposes: **reconstructing original stimuli** or mental activity and
            **identifying stimulus categories or mental imagery**.
            They find applications in **neuroscience, psychology, and diagnostic medicine**.
            Particularly,decoding acoustic information holds promise for brain-computer interfacing (BCI) systems, potentially enhancing their performance.''')


st.image("https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41598-022-27361-x/MediaObjects/41598_2022_27361_Fig6_HTML.png?as=webp", caption="Analysis pipeline illustration from the original study." )

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

if __name__ == "__main__":
    main()
