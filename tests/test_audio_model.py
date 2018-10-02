from werkzeug.utils import secure_filename


def test_get_path(test_model, app):
    with app.app_context():
        assert test_model.get_path()


def test_get_file_size(test_model):
    assert test_model.get_file_size()


def test_get_secure_file_name(test_model):
    a = secure_filename(test_model.file.filename)
    b = test_model.get_secure_file_name()
    assert a == b

"""
What do we need for our fixture?
    -audio model object, with all parameters included
    -
"""


def test_is_valid_reject_file_size(test_model):
    pass


def test_is_valid_no_file(test_model):
    pass


def test_is_valid_illegal_extension(test_model):
    pass


def test_is_valid_legal_file_and_extension(test_model):
    pass


# TODO: Cases: PARAMETERIZE
#   -no file
#   -no module
#   -file over max size
#   -no filename
#   -valid file, type, and size
#   -incorrect file type
#
#   -get_path fails if you don't save first-- NOPE
#   -get_file_size fails if file size is zero