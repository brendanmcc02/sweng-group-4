from flask import Flask, request, render_template, jsonify
from search import search_db
from search import create_uploaded_embeddings
from PIL import Image
from flask_cors import CORS
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import glob
from tqdm import tqdm
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        # Get the search term from the form
        search_term = request.form['search_term']
        
        # Search the database
        results = search_db(search_term)
        new_results = []
        
        for result in results:
            print(result)
            result = result.replace('public/', '/static/public/')
            new_results.append(result)

        return render_template('search.html', image_filenames=new_results)
    
#temp for frontend testing
@app.route('/search_frontend', methods=['GET'])
def search_frontend():
    search_term = request.args.get('parameter')
     #= 'puppy'
    results = search_db(search_term)
    return results

@app.route('/getCaption', methods=['GET'])
def get_image_caption():
    if request.method == 'GET':
        image_path = request.args.get('imagePath')
        caption = None
        if image_path:
            # Call search_db function to retrieve matches
            matches = search_db(image_path)
            if matches:
                # Extract the caption from the payload of the first match
                caption = matches[0]["caption"]
        return jsonify({'caption': caption})
    
@app.route('/uploadImg', methods=['POST'])
def uploadImg():
    try:
        if 'myFile' in request.files:
            uploaded_image = request.files['myFile']
            # adding caption from form data
            caption = request.form.get('caption')
            print ("got a caption")

            create_uploaded_embeddings(uploaded_image, caption)

            return 'Success', 200
    except Exception as e:
        print(e)
        return 'Error', 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

