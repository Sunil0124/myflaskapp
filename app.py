from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for feedback
data_store = []

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        username = request.form.get("username")
        comments = request.form.get("comments")
        
        feedback_entry = {"username": username, "comments": comments}
        data_store.append(feedback_entry)  # Store feedback
        
        return render_template("form_result.html", username=username, comments=comments)
    return render_template("feedback.html")

@app.route("/all_feedback")
def all_feedback():
    return render_template("all_feedback.html", feedback_list=data_store)

@app.route("/api/feedback")
def api_feedback():
    return jsonify(data_store)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
