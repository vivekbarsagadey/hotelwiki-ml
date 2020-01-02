from werkzeug.utils import secure_filename
from application import app
import os


ALLOWED_EXTENSIONS = set(['xlsx','csv'])
BASE_FOLDER = os.path.abspath(os.path.dirname(__name__))
UPLOAD_PATH = "/application/resources/recommender/files/upload/"

app.config['UPLOAD_FOLDER'] = BASE_FOLDER + UPLOAD_PATH


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


class FileHandler:
    def __init__(self):
        print("File handler init")

    def saveFile(self, request):
        if 'file' not in request.files:
            print("No file found")
            return "No file found"

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            completeFileName = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(completeFileName)

        return completeFileName
