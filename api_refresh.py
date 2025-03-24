import os
import requests
import pprint


api_key=os.getenv('NASA_API_KEY')
# url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
url= f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=14&api_key={api_key}"

request = requests.get(url)
response = request.json()

# image_url=response['photos'][10]['img_src']
# response2 = requests.get(image_url)

camera_name=response['photos'][0]['camera']['full_name']
camera_id=response['photos'][0]['camera']['id']
device_name=f'The camera name is {camera_name}\n'
device_id=f'The camera id is {camera_id}\n'

with open('device_info.txt', 'w') as f:
    f.write(device_name)
    f.write(device_id)

print(device_name)



pprint.pprint(response)

for item in response['photos']:
    print(item['camera']['full_name'])
    print(item['camera']['id'])
    print(item['img_src'])
    print(item['earth_date'])
    print(item['rover']['name'])
    print(item['rover']['landing_date'])
    print(item['rover']['launch_date'])
    print(item['rover']['status'])
    print('-----------------')
# with open('image.jpg', 'wb') as f:
#     f.write(response2.content)

