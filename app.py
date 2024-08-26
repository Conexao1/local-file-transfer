import os
from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename

#uploadPath = str(input("Where do you want you upload files? ")).replace("\\", "/") # where your upload files are going to
# i've to work on it

app = Flask(__name__)

uploadPath = ""
if not uploadPath:
    uploadPath = "./static/uploads"
    if uploadPath[-1] != "/":
        uploadPath = uploadPath + "/"
        print(uploadPath)

@app.route('/', methods=['GET', 'POST'])
def upload():
    os.makedirs(uploadPath, exist_ok=True) # create an upload dir if it not exist
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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
