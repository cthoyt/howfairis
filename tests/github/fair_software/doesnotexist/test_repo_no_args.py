import pytest
from requests_mock import Mocker
from howfairis import Repo
from howfairis.exceptions import GetDefaultBranchException
from tests.contracts.repo import Contract


def get_mocked_repo():
    return Repo("https://github.com/fair-software/doesnotexist")


skip_unreachable = pytest.mark.skip("Code for test is unreachable")


class TestRepoNoArgs(Contract):
    @skip_unreachable
    def test_api(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_branch(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_default_branch(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_owner(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_path(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_platform(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_raw_url_format_string(self, mocker: Mocker):
        pass

    def test_repo(self, mocker: Mocker):
        with mocker, pytest.raises(GetDefaultBranchException) as exc_info:
            get_mocked_repo()
        assert str(exc_info.value) == "Something went wrong asking the repo for its default branch."

    @skip_unreachable
    def test_url(self, mocker: Mocker):
        pass
