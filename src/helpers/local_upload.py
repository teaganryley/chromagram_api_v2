import os
from werkzeug.utils import secure_filename
from flask import current_app as app


class LocalUpload:
    def __init__(self, file):
        self.file = file

    def save(self):
        filename = secure_filename(self.file.filename)
        self.file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File saved via local upload.'


