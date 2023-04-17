from flask import Flask, request, jsonify
import pickle
from helpers import read_item_names
import pandas as pd
from flask_cors import CORS

with open('model/kNN_model.pkl', 'rb') as f:
    model = pickle.load(f)

print(model['algo'])
# Load the DataFrame from a CSV file

df = pd.read_csv('data/books.csv')

# Read the mappings raw id <-> movie name
rid_to_name, name_to_rid = read_item_names(df)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Welcome to my Flask app!'
# Define a route for book recommendations
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Retrieve inner id of the book
    book_title = request.args.get("book_title")
    print("Is the book here?", book_title, type(book_title))
    raw_id = name_to_rid[book_title]
    raw_id = int(raw_id)
    inner_id = model['algo'].trainset.to_inner_iid(raw_id)
    
    neighbors_inner = model['algo'].get_neighbors(inner_id, k=10) 

    # Get book information
    book_data = df.loc[df['book_id'] == raw_id].iloc[0]


    # Create response object
    response = {
        'book_title': book_data['title'],
        'image_url': book_data['image_url'],
        'authors': book_data['authors'],
        'publication_year': book_data['original_publication_year'],
        'nearest_neighbors': []
    }


    # Add nearest neighbors to response object
    for neighbor_inner in neighbors_inner:
        neighbor_raw = model['algo'].trainset.to_raw_iid(neighbor_inner)
        neighbor_name = rid_to_name[str(neighbor_raw)]
        neighbor_data = df.loc[df['book_id'] == neighbor_raw].iloc[0]
        response['nearest_neighbors'].append({
            'book_title': neighbor_data['title'],
            'image_url': neighbor_data['image_url'],
            'authors': neighbor_data['authors'],
            'publication_year': neighbor_data['original_publication_year']
        })

    return jsonify(response)