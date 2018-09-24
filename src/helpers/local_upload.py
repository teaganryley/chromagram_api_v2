import os
from werkzeug.utils import secure_filename
from flask import current_app as app


class LocalUpload:
    def __init__(self, file):
        self.file = file

    def save(self):
        filename = secure_filename(self.file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        self.file.save(upload_path)
        return upload_path


