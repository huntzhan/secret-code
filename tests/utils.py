from secret_code.utils import *  # noqa
import pytest


def test_case1():
    PATH = '/path/to/dir/filename.ext'

    assert '/path/to/dir' == extract_dir_path(PATH)
    assert 'filename' == extract_filename(PATH)
    assert 'ext' == extract_ext(PATH)


def test_case2():
    PATH = 'filename.ext'

    assert '' == extract_dir_path(PATH)
    assert 'filename' == extract_filename(PATH)
    assert 'ext' == extract_ext(PATH)


def test_case3():
    PATH = '/path/to/dir/filename'

    assert '/path/to/dir' == extract_dir_path(PATH)
    assert 'filename' == extract_filename(PATH)
    with pytest.raises(RuntimeError):
        extract_ext(PATH)


def test_case4():
    PATH = 'filename'

    assert '/path/to/dir' == extract_dir_path(PATH)
    assert 'filename' == extract_filename(PATH)
    with pytest.raises(RuntimeError):
        extract_ext(PATH)


def test_case5():
    PATH = '/path/to/dir/.ext'

    assert '/path/to/dir' == extract_dir_path(PATH)
    with pytest.raises(RuntimeError):
        extract_filename(PATH)
    assert 'ext' == extract_ext(PATH)


def test_case6():
    PATH = '/path/to/dir/filename.abc.ext'

    assert '/path/to/dir' == extract_dir_path(PATH)
    assert 'filename.abc' == extract_filename(PATH)
    assert 'ext' == extract_ext(PATH)
