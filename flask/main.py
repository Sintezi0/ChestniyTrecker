import os

from flask import Flask, request, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'C:/Users/1/PycharmProjects/pythonLesson/flask/static/content'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'rar'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    files = [f"<a href='http://127.0.0.1:5000/download/{file}'><li>{file}</li></a>" for file in
             os.listdir(app.config['UPLOAD_FOLDER'])]
    return (f'''
<!DOCTYPE html>
<html lang="ru">
<link rel="icon" href="/static/img/заголовок.ico)" type="image/x-icon">
<link rel="shortcut icon" href="/static/img/заголовок.ico)" type="image/x-icon">
  <head>
    <meta charset="utf-8">
    <title>Магазин онлайн-распродаж</title>
    <link href="/static/css/style.css" rel="stylesheet" type="text/css">
    <script src="/static/js/upload.js" defer></script>
  </head>
  <body>
    <header class="site-header">
      <div class="container">
        <h1>ChestniyTrecker</h1>
        <p>У нас праздничная распродажа! Качай приложения со скидкой 100% (акция продлится до 9 мая)!</p>
        <img src="static/img/gloevk-examples.png" width="800" height="510" alt="открытка">
      </div>
    </header>
    <section class="features">
      <ul>{''.join(files)}</ul>
    </section>
    <section class="advantages">
    <form id="upload-form" action="" method="post" enctype="multipart/form-data">
      <label for="file-input" class="plus-button">
        <span>+</span>
      </label>
      <input type="file" id="file-input" name="file" style="display: none;">
    </form>
    </section>
  </body>
</html>
''')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/download/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    return send_file(f'{app.config["UPLOAD_FOLDER"]}/{filename}', as_attachment=True)


@app.route('/download/', methods=['GET', 'POST'])
def download():
    files = [f"<a href='http://127.0.0.1:5000/download/{file}'><li>{file}</li></a>" for file in os.listdir(app.config['UPLOAD_FOLDER'])]
    return f"<ul>{''.join(files)}</ul>"


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
