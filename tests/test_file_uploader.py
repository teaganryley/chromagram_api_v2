import pytest
from src.helpers.file_uploader import FileUploader


def test_init_no_module_name():
    with pytest.raises(ValueError):
        FileUploader('pathname', None)


