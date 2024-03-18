import streamlit as st


# dataset infos:

st.title("Our Dataset")


# Define summaries
train_summary = "Train data is like practicing with examples to learn how things work."
test_summary = "Test data is like taking a quiz to see how well you remember what you've learned."
label_summary = "Label data is like having answers to the quiz, telling you what each example is."


# Display text boxes side by side
col1, col2, col3 = st.columns(3)

# Create containers for each section

with col1:
    st.info("Train Data")
    st.write(train_summary)

with col2:
    st.info("Test Data")
    st.write(test_summary)

with col3:
    st.info("Label Data")
    st.write(label_summary)


# dataset in boxes:

# def main():
#     st.header('Our Dataset in numbers')


#     # Define the content for each text box
#     train_data_content = '''train_data.shape:(160, 22036)'''

#     test_data_content = '''test_data.shape:(40, 22036)'''

#     labels_content = '''train_labels.shape:(160, 1)'''

#     # Display text boxes side by side
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.info("Train Data:")
#         st.text(train_data_content)

#     with col2:
#         st.info("Test Data")
#         st.text(test_data_content)

#     with col3:
#         st.info("Labels")
#         st.text(labels_content)

# if __name__ == "__main__":
#     main()

import pandas as pd

st.subheader('Images into numbers')
st.write('In simple words, our dataset are the **images** already translated to **numbers**, the language that the computers understand.')





# Load data into a list of lists

import streamlit as st

# Define the DOT language string for the flowchart
dot_code = """
digraph G {
    rankdir=LR;  // Set direction to left-to-right

    node [shape=rectangle, style=filled, fillcolor=lightblue];  // Define node properties

    // Define nodes
    brain_images [label="Brain Images"];
    preprocessing [label="Numbers"];
    numbers [label="Inputs to teach our model"];

    // Define connections
    brain_images -> preprocessing [label="Preprocessing"];  // Connection from brain images to preprocessing
    preprocessing -> numbers [label="Feature Extraction"];  // Connection from preprocessing to numbers
}
"""

# Display the flowchart using Graphviz DOT language
st.graphviz_chart(dot_code)




data = [
[-0.742153,	-0.776961,	-1.482406,	-2.372191,	-1.397303,	"...", 1.700659,	0.193262,	-0.903444],
[0.706499,	-3.121015,	1.604055,	-2.142794,	-4.990133,	"...", -0.589694, 0.620819, -0.236290],
[1.340712,	-1.551577,	-1.736186,	-1.961429,	-0.458469,	"...", -0.974377, -3.684177,	-3.495424],
[2.076994,	-0.372954,	-3.075090,	-1.484835,	2.603373,	"...", 1.733859, 0.144309,   -1.581721],
[0.234867,	1.090594,	2.437128,	1.936450,	-1.576794,	"...", 2.313220,	-2.347912,	-2.586554],
[2.692319,	-2.779358,	-1.946595,	-2.480742,	-2.229945,	"...", 0.747942,	0.484352,	-1.336589],
[0.541417,	-0.658512,	2.620512,	0.368862,	0.181794, "...",	1.257818,	-0.040875,	-0.545998],
[0.726454,	1.638362,	0.757149,	1.590652,	0.745251, "...", -6.832868,	-5.093495,	-1.690081],
[0.170095,	1.062273,	0.859110,	0.581071,	2.520496, "...",	-3.590637,	-3.480587,	-1.849468],
['...','...','...','...','...','...','...','...','...'],
]

# Define column names
#columns = [str(i) for i in range(len(data[0]))]

# Manually specify column names
column_names = ['1', '2', '3', '4,', '5','...','22034','22035', '22036']

# Create a DataFrame with column names
df = pd.DataFrame(data, columns=column_names)

# Display the DataFrame
st.write(df)

st.write('160 rows × 22036 columns')
