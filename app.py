from flask import Flask, render_template, send_from_directory
import os
from eda import run_eda, output_dir

app = Flask(__name__)

# Run EDA only once
if not os.path.exists(output_dir) or not os.listdir(output_dir):
    print("Running EDA...")
    run_eda()
else:
    print("EDA results already exist. Skipping EDA execution.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('templates/images', filename)

if __name__ == "__main__":
    app.run(debug=True)
