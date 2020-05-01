import requests, time

img_urls = [
'https://images.unsplash.com/photo-1587969572126-a9e459d35cfc?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80',
    
]

t1 = time.perf_counter()

for img_url in img_urls:
    img_bytes = requests.get(img_url).content
    img_name = img_url.spilt('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

t2 = time.perf_counter()
print(f'Finished in {t2-t1} second(s)...')