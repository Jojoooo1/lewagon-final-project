import streamlit as st


# dataset infos:

st.title("Our Dataset")


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
