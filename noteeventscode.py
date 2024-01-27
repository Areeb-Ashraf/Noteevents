from dotenv import load_dotenv
from openai import OpenAI
import os
import pandas
import functions

# Get API KEY
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("API_KEY"),
)

# Read and Process NOTEVENTS.csv
df = pandas.read_csv("small_NOTEEVENTS.csv")
df = df.drop(columns=['SUBJECT_ID','CHARTDATE','CHARTTIME','STORETIME','CATEGORY','DESCRIPTION','CGID','ISERROR'])

# Iterating dataframe
for index in range(len(df)):

    # Get Prompt
    text = df.at[index, 'TEXT']
    user_prompt = functions.prompt(text)

    # Call API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Store Response
    response = chat_completion.choices[0].message.content  
    df.at[index, 'is_stroke_pt'] = response

# Downloading new dataframe 
df = df.drop(columns=["TEXT"])       
df.to_csv('file1.csv')


# 4k Token Limit Hit, On average one API call is 8K tokens.