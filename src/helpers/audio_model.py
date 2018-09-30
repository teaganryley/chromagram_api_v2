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
        if self.is_valid():
            self.upload_module.save()
            return True
        else:
            return False

    def get_path(self):
        self.upload_module.get_upload_path()

    def get_file_size(self):
        return len(self.file.read())

    def get_secure_file_name(self):
        return self.upload_module.filename

    def is_valid(self):
        ext_allowed = self.file.filename.lower().endswith(self.allowed_extensions)
        size_allowed = (self.get_file_size() <= self.max_upload_size)
        return ext_allowed and size_allowed


#get vendor

#delete file

#get file name method?