import pytest

from genstr import Genstr
from genstr import Mode


class TestMode1:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mode = Mode.PURE_NUMBERS

    def test_less_than_10(self):
        list = Genstr(
            length=1,
            mode=self.mode
        ).combine().list()
        assert list[0] == '0'
        length = len(list)
        assert length == 10
        assert list[length - 1] == '9'

    def test_between_10_and_100(self):
        list = Genstr(
            length=2,
            mode=self.mode
        ).combine().list()
        assert list[0] == '00'
        length = len(list)
        assert length == 100
        assert list[length - 1] == '99'

    def test_less_than_100(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True
        ).combine().list()
        assert list[0] == '0'
        length = len(list)
        assert length == 110
        assert list[length - 1] == '99'

    def test_between_one(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            is_range=True,
            prefix='9'
        ).combine().list()
        assert list[0] == '90'
        length = len(list)
        assert length == 110
        assert list[length - 1] == '999'

    def test_between_two(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            prefix='9'
        ).combine().list()
        assert list[0] == '900'
        length = len(list)
        assert length == 100
        assert list[length - 1] == '999'
