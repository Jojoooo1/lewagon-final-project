import streamlit as st


# dataset infos:

st.title("Our Dataset")


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

# dataset in boxes:

def main():
    st.header('The Dataset in numbers')

    # Define the content for each text box
    train_data_content = '''train_data.shape:(160, 22036)'''

    test_data_content = '''test_data.shape:(40, 22036)'''

    labels_content = '''train_labels.shape:(160, 1)'''

    # Display text boxes side by side
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("Train Data")
        st.text(train_data_content)

    with col2:
        st.info("Test Data")
        st.text(test_data_content)

    with col3:
        st.info("Labels")
        st.text(labels_content)

if __name__ == "__main__":
    main()
