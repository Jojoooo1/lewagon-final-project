import streamlit as st


st.header("Additional Informations")

# about the datasets

st.subheader("1. About the dataset")

st.markdown('''The data consists of **train.csv, labels.csv, and test.csv**, for a one-person subset of a larger 20-subject study.''')

st.markdown('''The **training data** (train.csv) consist of 160 event-related brain images (trials),
            corresponding to twenty 6-second music clips, four clips in each of the five genres,
            repeated in-order eight times (runs).
            ''')

st.markdown('''The **labels** (labels.csv) correspond to the correct musical genres,
            listed above, for each of the 160 trials.There are 22036 features in each brain image, corresponding to blood-oxygenation levels at each 2mm-cubed 3D location
            within a section of the auditory cortex.''')

st.markdown('''The **testing data** (test.csv) consists of 40 event-related brain images corresponding to novel 6-second music clips in the five genres.
            The test data is in randomized order with no labels. You must predict,
            using only the given brain images, the correct genre labels (0-4) for the 40 test trials.''')

# contextualization


st.subheader("2. Contextualization")

st.markdown('''
            ***Neural decoding models*** aim to interpret mental states from neural activity recordings, utilizing various neuroimaging modalities such as fMRI, ECoG, EEG, and fNIRS.
            These models have been applied to decode diverse activities including affective states, visual imagery, and semantic information.
            ''')

st.markdown('''***Decoding models*** serve two main purposes: **reconstructing original stimuli** or mental activity and
            **identifying stimulus categories or mental imagery**.
            They find applications in **neuroscience, psychology, and diagnostic medicine**.
            Particularly,decoding acoustic information holds promise for brain-computer interfacing (BCI) systems, potentially enhancing their performance.''')


# links to papers

st.subheader("3. Papers Cited")

st.link_button("Enhancing Music Genre Classification with Neural Networks by using Extracted Musical Features", "https://essay.utwente.nl/80549/1/Flederus_BA_EEMCS.pdf")

st.link_button("Ghaemmaghami, Pouya & Sebe, Nicu. (2016). Brain and music: Music genre classification using brain signals. 708-712. 10.1109/EUSIPCO.2016.7760340.", "https://www.researchgate.net/publication/311757569_Brain_and_music_Music_genre_classification_using_brain_signals")

st.link_button("Daly, I. Neural decoding of music from the EEG. Sci Rep 13, 624 (2023). Neural decoding of music from the EEG", "https://rdcu.be/dBE3s")

st.link_button("Youtube video: 'Music in the Brain', MIT Scientists","https://www.youtube.com/watch?v=HhTCOlJ-nh4")



# links to the team members:

st.subheader("4. Teammates")

# Define the URLs for your team members' social media profiles
lorena_linkedin_url = "www.linkedin.com/in/lorenamelodev"
lorena_github_url = "https://github.com/lorenamelos"

jonathan_linkedin_url = "https://www.linkedin.com/in/jonathan-chevalier-fr/"
jonathan_github_url = "https://github.com/Jojoooo1"

# Define the HTML code for the icons
linkedin_icon = '<img src="https://img.icons8.com/color/48/000000/linkedin.png"/>'
github_icon = '<img src="https://img.icons8.com/color/48/000000/github--v1.png"/>'

# Define the layout for Lorena and Jonathan
col1, col2 = st.columns(2)

# Lorena's social media links
with col1:
    st.write("Lorena Melo")
    st.markdown(
        '<div style="display:flex; align-items:center;"><a href="{}" target="_blank">{}</a> <a href="{}" target="_blank">{}</a></div>'.format(
            lorena_linkedin_url, linkedin_icon, lorena_github_url, github_icon
        ),
        unsafe_allow_html=True,
    )

# Jonathan's social media links
with col2:
    st.write("Jonathan Chevalier")
    st.markdown(
        '<div style="display:flex; align-items:center;"><a href="{}" target="_blank">{}</a> <a href="{}" target="_blank">{}</a></div>'.format(
            jonathan_linkedin_url, linkedin_icon, jonathan_github_url, github_icon
        ),
        unsafe_allow_html=True,
    )
