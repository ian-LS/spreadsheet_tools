from flask import Flask, render_template, request, jsonify
from helpers import validate_format, merge_documents, remove_duplicates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    file1 = request.files['file1']
    file2 = request.files['file2']

    result = validate_format(file1, file2)

    return jsonify(result=result)

@app.route('/merge', methods=['POST'])
def merge():
    file1 = request.files['file1']
    file2 = request.files['file2']

    merged_data = merge_documents(file1, file2)

    return jsonify(result=merged_data)

@app.route('/remove_duplicates', methods=['POST'])
def remove_duplicates_route():
    file = request.files['file']

    cleaned_data = remove_duplicates(file)

    return jsonify(result=cleaned_data)

if __name__ == '__main__':
    app.run(debug=True)
