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
    git_ak = 'https://github.com/its-me-abhishek'
    git_as = 'https://github.com/abhijitshukla'
    li_ak = 'https://www.linkedin.com/in/abhishek-%E2%80%8E-6009a224b/'
    li_as = 'https://www.linkedin.com/in/abhijit-kumar-shukla-b41739272/'
    li_ar = 'https://www.linkedin.com/in/aditya-raina-65aa66257'
    li_at = 'https://www.linkedin.com/in/jerryyyy'
    em_ak = 'abhishek31304@gmail.com'
    em_as = 'abhijitshukla888@gmail.com'
    em_ar = 'adityaraina204@gmail.com'
    em_at = 'akshrivastav8864@gmail.com'
    return render_template('about.html', git_ak=git_ak, git_as=git_as, li_ak=li_ak, li_as=li_as, li_ar=li_ar, li_at=li_at, em_ak=em_ak, em_as=em_as, em_ar=em_ar, em_at=em_at)

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
    app_id = 'APP_ID'
    app_key = 'APP_KEY'
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
