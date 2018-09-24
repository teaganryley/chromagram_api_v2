from src.helpers import build_chroma


def test_build_chroma_return_type(app):
    path_to_file = app.config['TEST_WAV']
    assert isinstance(build_chroma.analyze(path_to_file), list)

