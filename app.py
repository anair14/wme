"""
Author: Ashwin Nair
Date: 2025-01-27
Project name: app.py
Summary: Python portion for the Web Markdown Editor
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
