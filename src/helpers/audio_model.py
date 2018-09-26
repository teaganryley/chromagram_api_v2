class AudioModel:
    def __init__(self,
                 file,
                 module,
                 allowed_extensions=['wav', 'mp3'],
                 max_upload_size=(8 * 1024 * 1024)):
        self.file = file
        self.upload_module = module(file)
        self.allowed_extensions = allowed_extensions
        self.max_upload_size = max_upload_size
    #TODO: validation for upload module?

    def save_file(self):
        self.upload_module.save()

    def get_path(self):
        self.upload_module.get_upload_path()

    def get_file_size(self):
        # blob = request.files['file'].read()
        # size = len(blob)

    def is_valid(self):
        ext_allowed = self.file.filename.lower().endswith(self.allowed_extensions)
        size_allowed =


#get vendor

#delete file