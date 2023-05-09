from flask import Flask, request, send_file
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/image')
def get_image():
    keyword = request.args.get('keyword')
    response = requests.get(f"https://source.unsplash.com/800x600/?{keyword}")
    img = Image.open(BytesIO(response.content))
    img.save('temp.png', format='PNG')
    return send_file('temp.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)