import pytest
from src.helpers.file_uploader import FileUploader
from src.helpers.local_upload import LocalUpload


def test_init_no_module_name():
    with pytest.raises(ValueError):
        FileUploader('pathname', None)


