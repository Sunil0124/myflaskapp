from flask import Flask, render_template, jsonify, request
from forms import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        return jsonify({"message": f"Thank you {form.name.data}, your feedback has been submitted!"})
    return render_template('feedback.html', form=form)

# Internal API: Returns dummy project data
@app.route('/api/internal', methods=['GET'])
def internal_api():
    data = {"message": "This is data from an internal Flask API!"}
    return jsonify(data)

# External API: Fetch data from GitHub
import requests
@app.route('/api/github', methods=['GET'])
def github_api():
    response = requests.get('https://api.github.com/users/github/repos')
    if response.status_code == 200:
        repos = response.json()[:3]  # Limit to 3 repos
        return jsonify(repos)
    return jsonify({"error": "Unable to fetch data"}), 500

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)
