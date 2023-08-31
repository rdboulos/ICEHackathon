import streamlit as st
#import dotenv
#from dotenv import load_dotenv


##import environ
##env = environ.Env()
##environ.Env.read_env()

#load_dotenv()

import pandas as pd
from pandasai import PandasAI

import os
#from pandasai import SmartDataframe

# Define the path to the folder containing the files
#folder_path = "C:/Users/Rebecca/Documents/LLMs/PandasOpenAIV2/Data"
#folder_path = "https://raw.githubusercontent.com/rdboulos/repository/main/icehackathon"

# Get a list of all files in the folder
#file_list = os.listdir(folder_path)

# Initialize an empty list to hold data frames
#data_frames = []

# Loop through the files and read them into Pandas data frames
#for file_name in file_list:
file_path = "https://github.com/rdboulos/ICEHackathon/blob/main/GOTOES_FIT-CSV_Github.csv"
#if os.path.isfile(file_path):

        #df = pd.read_csv(file_path)  # You can adjust this based on the file format
        #df = pd.read_csv(file_path)

#df = pd.read_csv(https://raw.githubusercontent.com/rdboulos/repository/main/icehackathon/GOTOES_FIT-CSV_Github.csv)
        github_csv_url ="https://github.com/rdboulos/ICEHackathon/blob/main/GOTOES_FIT-CSV_Github.csv"
        df = pd.read_csv(github_csv_url)
        data_frames.append(df)

# Concatenate all data frames into a single data frame
combined_df = pd.concat(data_frames, ignore_index=True)

# Convert the combined data frame to a SmartDataFrame
#smart_df = SmartDataFrame.from_pandas(combined_df)

# Alternatively, you can also convert it to a SmartDataLake
#smart_lake = SmartDataLake.from_dataframe(smart_df)

# Show a summary of the SmartDataFrame or SmartDataLake
# print(smart_df.summary())
#_________________________________________________________

# Instantiate a LLM
from pandasai.llm.openai import OpenAI
llm = OpenAI(api_token="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")

pandas_ai = PandasAI(llm, conversational=True, enable_cache=True)

def main():
    st.title("Matthew Dinham Databot")
    st.write("Welcome to the Matthew Dinham Databot! Ask questions to his data for 90th World Championships Mens Road Race.")

    # Add a text input for user input
    user_input = st.text_input("Ask a question:")

    if st.button("Get Answer"):
        if user_input:
            response = pandas_ai.run(combined_df, prompt=user_input)
            st.write("Chatbot's Response:")
            st.write(response)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()



