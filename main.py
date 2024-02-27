import streamlit as st
import requests


#prepare API URL and API key
api_key="ko3O0izFoyeFbTqzUZLyqwiBxUyqpAliRiod5Bj7"
url="https://api.nasa.gov/planetary/apod?" \
f"api_key={api_key}"

#get request data as dictionary
response1=requests.get(url)
data=response1.json()

#extract image title, url and explanation
title=data["title"]
image_url=data["url"]
explanation=data["explanation"]

#download image from url
image_filepath="img.jpg"
response2=requests.get(image_url)
with open(image_filepath, "wb")as file:
    file.write(response2.content)

#create front end of website

st.title(title)
st.image(image_filepath)
st.write(explanation)







