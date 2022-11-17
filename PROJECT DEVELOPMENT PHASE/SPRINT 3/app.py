from __future__ import division, print_function
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image 
from tensorflow.keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from twilio.rest import Client

global graph
#graph=tf.get_default_graph()
# Define a flask app
app = Flask(__name__)
model = load_model('forest1.h5')



@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('digital.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['image']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        img1 = image.load_img(file_path,target_size=(150,150))
        
        y = image.img_to_array(img1)
        x= np.expand_dims(y, axis=0)
        val = model.predict(x)
        print(val)
        if val == 1:
            send_message()
            result ="Fire"
        elif val == 0:
            result = "No Fire"
        return result

def send_message():


	<--- "Enter your Twilio address"-->
		
	
    
        

if __name__ == '__main__':
    app.run(threaded = False)

