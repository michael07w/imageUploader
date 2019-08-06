from flask import Flask, request, render_template
from PIL import Image
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/upload', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':

        target = os.path.join(APP_ROOT, 'static/')    # file path to uploaded file

        img = request.files['pic']    # uploaded FileStorage object
        filename = img.filename    # file name of said object^^

        destination = '/'.join([target, filename])
        img.save(destination)    # saves uploaded file to specified destination

        return render_template("displayUpload.html", image_name=filename)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
