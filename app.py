from flask import Flask, render_template, request, redirect
import random
import string

# this is a comment
app = Flask(__name__)

url_map = {}

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

@app.route('/', methods=['GET', 'POST'])
def home():

    short_url = None

    if request.method == 'POST':

        long_url = request.form['url']

        code = generate_code()

        url_map[code] = long_url

        short_url = request.host_url + code

    return render_template('index.html', short_url=short_url)

@app.route('/<code>')
def redirect_url(code):

    if code in url_map:
        return redirect(url_map[code])

    return "URL not found"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
