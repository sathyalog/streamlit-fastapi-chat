import streamlit as st
import pandas as pd

# large-heading
st.markdown("# My Streamlit App")
# small-heading
st.markdown("## streamlit library is used to create web apps in python")
st.write("Hello, welcome to my Streamlit app!")

number = st.slider("Select a number", 0, 100, 50)
st.write("You selected:", number)

checkbox = st.checkbox("Check me!")
if checkbox:
    st.write("Checkbox is checked!")

st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo")

st.video("https://www.youtube.com/watch?v=jEqmcR2z5L4&pp=ygUYd2hhdCBpcyBzdHJlYW1saXQgNjBzZWNz", format="video/mp4", start_time=0)


# file uploader for CSV and Excel files
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx"])

# check if a file is uploaded and read it into a pandas DataFrame
if uploaded_file is not None:
    # 1. Read the data based on file type
    if uploaded_file.name.endswith('.csv') or uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # 2. Display metadata
    st.write("### Data Overview")
    st.write("Dataframe shape: ", df.shape) # print the shape of the dataframe
    st.write("Column names: ", df.columns.tolist()) # print the column names of the dataframe
    
    # Optional: Display the raw data in an expander so it doesn't take up too much space
    with st.expander("View Raw Data"):
        st.dataframe(df)

    # 3. Data filtering and selection
    st.write("### Data filtering and selection")
    
    # Check if 'Country' exists in columns to prevent errors
    if 'Country' in df.columns:
        selected_value = st.selectbox("Select a country to filter by", df['Country'].unique()) # selectbox is used to select a column from the dataframe

        filtered_data = df[df['Country'] == selected_value] # filter the dataframe based on the selected value
        
        st.write(f"Showing results for: **{selected_value}**")
        st.dataframe(filtered_data) # display the filtered data
    else:
        st.error("The uploaded file does not contain a 'Country' column to filter by.")

        #Display basic statistics of the dataframe
    st.write("### Basic Statistics")
    st.write(df.describe()) # display basic statistics of the dataframe

    #Show specific metrics like total rows
    st.write("Total rows in the dataframe: ", len(df)) # display total rows in the dataframe

    #Visualization: Display a bar chart for a specific column if it exists
    import matplotlib.pyplot as plt
    if 'Country' in df.columns:
        country_counts = df['Country'].value_counts()
        st.write("### Country Distribution")
        st.bar_chart(country_counts) # display a bar chart of the country distribution

    fig,ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
    st.pyplot(fig)