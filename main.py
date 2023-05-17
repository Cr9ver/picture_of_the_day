import streamlit as st
import requests
import backend

api_key = "CscYDTjoeXbrLitfbbk9joUTw1hLmLmnLHlKacFy"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request as a dictionary
request = requests.get(url)
response1 = request.json()


#Extract the image, url, title and explanation
title = response1["title"]
explanation = response1["explanation"]
image_url = response1["url"]

response2 = requests.get(image_url)



#Download image
with open("image.jpg", "wb") as file:
    file.write(response2.content)

st.title(title)
st.image("image.jpg")

st.write(explanation)


