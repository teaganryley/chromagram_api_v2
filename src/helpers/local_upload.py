import os
from werkzeug.utils import secure_filename
from flask import current_app as app


class LocalUpload:
    def __init__(self, file):
        self.file = file
        self.filename = secure_filename(file.filename)

    def get_upload_path(self):
        return os.path.join(app.config['UPLOAD_FOLDER'], self.filename)

    def save(self):
        self.file.save(self.get_upload_path())
