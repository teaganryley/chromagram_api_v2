class FileUploader:
    def __init__(self, file, module):
        if not module:
            raise ValueError('Must specify upload module.')
        self.upload_module = module(file)

    def save(self):
        return self.upload_module.save()

#TODO: DELETE this once tests pass