from flask import Flask, render_template, request, jsonify, redirect
import requests
import json

app = Flask(__name__)

#Home Page
@app.route('/')
def home():
    return render_template('index.html')

#About Page
@app.route('/about')
def about():
    return render_template('about.html')

#Github
@app.route('/github', methods=['GET'])
def github():
    return redirect("https://github.com/its-me-abhishek/LetMeCook")

#Search Output
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    ingredient = data['ingredient']
    
    #API info
    app_id = 'b4cc4ff4'
    app_key = '208a15bc89f8e6cdd13872f6dbbc4c44'
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'
    
    #Response
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        recipes = data.get('hits', [])[:10]
        return jsonify({"recipes": recipes})
    else:
        return jsonify({"recipes": []})


if __name__ == '__main__':
    app.run()
