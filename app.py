import os
from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from markupsafe import escape

a

app = Flask(__name__)
uploadPath = "".join(("./static/", input(str("Where do you want you upload files? ")).replace("\\", "/"))) # where your upload files are going to
#uploadPath = input(str("Where do you want you upload files? ")).replace("\\", "/") # where your upload files are going to

if not uploadPath:
    uploadPath = "./static/uploads"
    if uploadPath[-1] != "/":
        uploadPath = uploadPath + "/"
        print(uploadPath)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    os.makedirs(uploadPath, exist_ok=True) # create a upload dir if it not exist
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        files = request.files.getlist("file") 
        for file in files:
            print(file.filename)
            fileName = secure_filename(file.filename)
            file.save(os.path.join(uploadPath, fileName))
            print(os.path.join(uploadPath, fileName))
    uploadedFiles = os.listdir(uploadPath) # list of all files that already are in uploaded at current path
    
    for file in uploadedFiles: # filtering what is not a file 
        if "." not in file:
            uploadedFiles.remove(file)
    print(uploadedFiles)
    return render_template("index.html", uploadPath=uploadPath, uploadedFiles=uploadedFiles)
'''
@app.route('/download/<fileName>', methods=['GET'])
def download(fileName):
    return send_from_directory(uploadPath, fileName)
'''
'''
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(downloadPath, name)
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
