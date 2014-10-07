#!/usr/local/bin/python

from flask import Flask, render_template, request
import hashlib
app = Flask(__name__)

# URL to usage count
url_counts = {}

# hashed to URL
url_originals = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shortened', methods=['POST'])
def shortener():
    short_url = shorten_url(request.form['url'])
    return render_template('shortened.html', url=short_url)

@app.route('/<hashed>')
def original(hashed=None):
    # Do a reverse lookup of original url using hash
    original_url = None
    url_count = 0
    if hashed in url_originals:
        original_url = url_originals[hashed]
        url_count = url_counts[original_url]
    return render_template('link.html', url=original_url, count=url_count)

def shorten_url(string):
    # Increment string count
    new_string = string
    if string in url_counts:
        url_counts[string] += 1
    else:
        url_counts[string] = 1

    # Get hash of url
    short_url = hashlib.md5(string).hexdigest()[:7]
    if short_url not in url_originals:
        url_originals[short_url] = string
    return short_url

if __name__ == '__main__':
    app.run(debug=True)

# End of file
