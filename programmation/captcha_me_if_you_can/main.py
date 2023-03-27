import requests as r
import base64
import os

url = "http://challenge01.root-me.org/programmation/ch8/"
response = r.get(url)
response_html = response.text
response_html = response_html.replace("<html><head></head><body><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' /><iframe id='iframe' src='https://www.root-me.org/?page=externe_header'></iframe><p></p><br/><img src=", "")
response_html = response_html.replace('"data:image/png;base64,', '')
response_html = response_html.replace('" /><br><br><form action="" method="POST"><input type="text" name="cametu" /><input type="submit" value="Try" /></form></body></html>', '')
print(response_html)
img_data = base64.b64decode(response_html)
file = 'image.png'
with open(file, 'wb') as f:
    f.write(img_data)
    f.close()

os.system('tesseract image.png flag')

