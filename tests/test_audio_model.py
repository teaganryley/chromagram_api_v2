from werkzeug.utils import secure_filename
# from flask import current_app as app


def test_audio_model_save(test_model):
    audio_model, app = test_model
    with app.app_context():
        assert audio_model.save_file()


def test_get_path_before_save(test_model):
    audio_model, app = test_model
    with app.app_context():
        assert not audio_model.get_path()



def test_get_file_size(test_model):
    #assert test_model.get_file_size()
    pass


def test_get_secure_file_name(test_model):
    #assert test_model.get_secure_file_name()
    pass
