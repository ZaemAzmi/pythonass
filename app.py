from flask import Flask, render_template, send_from_directory
import os
from eda import run_eda, output_dir

app = Flask(__name__, static_url_path='/static')

# Run EDA only once
if not os.path.exists(output_dir) or not os.listdir(output_dir):
    print("Running EDA...")
    run_eda()
else:
    print("EDA results already exist. Skipping EDA execution.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/amazon')
def amazon():
    return render_template('amazon.html')

@app.route('/apple')
def apple():
    return render_template('apple.html')

@app.route('/microsoft')
def microsoft():
    return render_template('microsoft.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/netflix')
def netflix():
    return render_template('netflix.html')

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('templates/images', filename)

if __name__ == "__main__":
    app.run(debug=True)
