import  pandas as pd
import streamlit as st
import seaborn as sns






# Title and header
st.title("Data Analysis")
st.subheader("Data Analysis using python and streamlit")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Upload dataset
upload_file = st.file_uploader("Upload Your dataset (In CSV format) : ")
if upload_file is not None:
    data = pd.read_csv(upload_file, low_memory=False)

# Show dataset
if upload_file is not None:
    upload_file.seek(0)
    data = pd.read_csv(upload_file, low_memory=False)

    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

# check datatype of each column
if upload_file is not None:
    upload_file.seek(0)
    data = pd.read_csv(upload_file, low_memory=False)
    if st.checkbox("Datatype of each column"):
        st.text("DataTypes")
        st.write(data.dtypes)

# Find the shape of the dataset
if upload_file is not None:
    upload_file.seek(0)
    data = pd.read_csv(upload_file, low_memory=False)
    data_shape = st.radio("What do you want to check",("Rows", "Columns"))
    if data_shape == "Rows":
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == "Columns":
        st.text("Number of Columns")
        st.write(data.shape[1])

# Find the null values in column
if upload_file is not None:
    upload_file.seek(0)
    data = pd.read_csv(upload_file, low_memory=False)
    if st.checkbox("Show Null Value count"):
        is_null = data.isnull().values.any()
        if is_null == True:
            st.write(data.isnull().sum())
            if st.checkbox("Show Graph"):
                sns.heatmap(data.isnull())
                st.pyplot()
        else:
            st.success("Congratulation!! No null values")

# Find duplicate values in the dataset
if upload_file is not None:
    upload_file.seek(0)
    data = pd.read_csv(upload_file, low_memory=False)

    if st.checkbox("Show Duplicate Values"):
        dup_val = data.duplicated().any()
        if dup_val == True:
            st.warning("Data contains some duplicate values")
            rmv_duplicates = st.selectbox("Do you want to remove",("Select One", "Yes", "No"))
            if rmv_duplicates == "Yes":
                data = data.drop_duplicates()
                st.text("Successful!! Duplicates removed")
            if rmv_duplicates == "No":
                st.text("Ok!! No Problem")
        else:
            st.success("Congratulation!! No duplicate values ")

# Get overall statistics of the dataset
if upload_file is not None:
    upload_file.seek(0)
    data = pd.read_csv(upload_file, low_memory=False)
    if st.checkbox("Show Statistic of Data"):
        st.write(data.describe(include='all'))


# About Section
if st.button("About App"):
    st.text("Built with streamlit")
    st.text("Thanks to Streamlit")

# By
if st.button("By"):
    st.success("Sachin Pal")
    st.text("Credit Data Thinkers")

# Insruction to use Streamlit
if st.button("Instruction to use streamlit"):
    st.text("""
    TO use streamlit
    First we need to install conda libirary
        -> pip install conda
    then we have to install streamlit
        -> pip install streamlit
    To run the streamlit server write this in terminal
    streamlit run file_name.py
    In my case it is
    streamlit run project_1_streamlit.py
    """)