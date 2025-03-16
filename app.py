from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated file storage
files = []

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.form.get('filename')
    if filename:
        files.append(filename)
    return redirect(url_for('index'))

@app.route('/update/<int:file_id>', methods=['POST'])
def update(file_id):
    new_filename = request.form.get('new_filename')
    if 0 <= file_id < len(files) and new_filename:
        files[file_id] = new_filename
    return redirect(url_for('index'))

@app.route('/delete/<int:file_id>', methods=['POST'])  # Changed to POST to fix 405 error
def delete(file_id):
    if 0 <= file_id < len(files):
        files.pop(file_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

