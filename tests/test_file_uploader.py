import pytest
from src.helpers.file_uploader import FileUploader


def test_init_no_module_name():
    """Tests uploader initialized with no module name procs Value Error."""
    with pytest.raises(ValueError):
        FileUploader('pathname', None)

