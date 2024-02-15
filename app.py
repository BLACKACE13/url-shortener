from flask import Flask, render_template, request, redirect
from main import URL_shortener

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['original_url']
    s = URL_shortener(original_url)
    short_url = s.shorten_url(s.url)
    return render_template('index.html', original_url=original_url, short_url=short_url)

@app.route('/<shortened_id>')
def redirect_to_original(shortened_id):
    original_url = URL_shortener.get_original_url(shortened_id)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
