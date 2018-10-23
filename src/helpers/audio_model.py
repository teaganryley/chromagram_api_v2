import os


class AudioModel:
    def __init__(self,
                 file,
                 module,
                 allowed_extensions=('wav', 'mp3'),
                 max_upload_size=(8 * 1024 * 1024)):
        self.file = file    # In Flask, this is a werkzeug FileStorage object
        self.upload_module = module(file)
        self.allowed_extensions = allowed_extensions
        self.max_upload_size = max_upload_size

    def get_path(self):
        return self.upload_module.get_upload_path()

    def get_file_size(self):
        return os.path.getsize(self.file.filename)

    def get_secure_file_name(self):
        return self.upload_module.filename

    def is_valid(self, filename=None, file_size=None):
        # sets object fields as default values
        filename = self.file.filename if filename is None else filename
        file_size = self.get_file_size() if file_size is None else file_size

        return filename.lower().endswith(self.allowed_extensions) and \
            (0 < file_size <= self.max_upload_size)

    def save_file(self):
        self.upload_module.save()
        return self.get_path()



# TODO: get_vendor, get_file_name
