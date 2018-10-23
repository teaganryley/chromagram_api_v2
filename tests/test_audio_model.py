import pytest
from werkzeug.utils import secure_filename

"""
We organize is_valid() scenarios according to a truth table members:

(valid extension) ^ (valid size) 

    F ^ F | F
    F ^ T | F
    T ^ F | F
    T ^ T | T       this only needs one scenario

Although these scenarios could be merged into a single test case, I will separate them for the readability.
"""

f_f_files = ['testname', 'not_audio.bin']
f_f_sizes = [0, 10 * 1024 * 1024]

f_t_files = ['testname', 'not_audio.bin']
f_t_sizes = [500]

t_f_files = ['audio.wav', 'audio.mp3']
t_f_sizes = [0, 10 * 1024 * 1024]


def test_get_path(test_model, app):
    with app.app_context():
        assert test_model.get_path()


def test_get_file_size(test_model):
    assert test_model.get_file_size()


def test_get_secure_file_name(test_model):
    a = secure_filename(test_model.file.filename)
    b = test_model.get_secure_file_name()
    assert a == b


@pytest.mark.parametrize('file', f_f_files)
@pytest.mark.parametrize('size', f_f_sizes)
def test_is_valid_f_f(test_model, file, size):
    assert not test_model.is_valid(file, size)


@pytest.mark.parametrize('file', f_t_files)
@pytest.mark.parametrize('size', f_t_sizes)
def test_is_valid_f_t(test_model, file, size):
    assert not test_model.is_valid(file, size)


@pytest.mark.parametrize('file', t_f_files)
@pytest.mark.parametrize('size', t_f_sizes)
def test_is_valid_t_f(test_model, file, size):
    assert not test_model.is_valid(file, size)


def test_is_valid_t_t(test_model):
    assert test_model.is_valid('audio.wav', 500)


def test_is_valid_with_default_values(test_model):
    assert test_model.is_valid()

