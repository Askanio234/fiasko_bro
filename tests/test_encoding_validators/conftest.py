import os.path
import pytest
import git
from fiasko_bro import LocalRepositoryInfo


@pytest.fixture(scope="module")
def encoding_repo_path():
    encoding_repo_dir = 'test_fixtures{}encoding_repo'.format(os.path.sep)
    return encoding_repo_dir


@pytest.fixture(scope="module")
def general_repo_path():
    general_repo_dir = 'test_fixtures{}general_repo'.format(os.path.sep)
    return general_repo_dir


@pytest.fixture(scope="module")
def test_repo_with_bom():
    test_repo_dir = 'test_fixtures{0}encoding_repo{0}utf8_with_bom'.format(os.path.sep)
    git.Repo.init(test_repo_dir)
    return LocalRepositoryInfo(test_repo_dir)


@pytest.fixture(scope="module")
def test_repo_without_bom():
    test_repo_dir = 'test_fixtures{}general_repo'.format(os.path.sep)
    git.Repo.init(test_repo_dir)
    return LocalRepositoryInfo(test_repo_dir)
