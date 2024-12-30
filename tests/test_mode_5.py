import pytest

from genstr import Genstr
from genstr import Mode


class TestMode5:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mode = Mode.MIXED_EXCLUDE_PURE

    def test_00_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode
        ).combine().list()
        assert list[0] == '0a'
        length = len(list)
        assert length == 520
        assert list[length - 1] == 'z9'

    def test_0_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True
        ).combine().list()
        assert list[0] == '0a'
        length = len(list)
        assert length == 520
        assert list[length - 1] == 'z9'

    def test_between_one_p(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'a0'
        length = len(list)
        assert length == 10
        assert list[length - 1] == 'a9'


    def test_between_two_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            prefix='a'
        ).combine().list()
        assert list[0] == 'a00'
        length = len(list)
        assert length == 620
        assert list[length - 1] == 'az9'

    def test_between_three_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'a0'
        length = len(list)
        assert length == 630
        assert list[length - 1] == 'az9'


    def test_between_one_s(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True,
            suffix='o'
        ).combine().list()
        assert list[0] == '0o'
        length = len(list)
        assert length == 10
        assert list[length - 1] == '9o'


    def test_between_two_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            suffix='o'
        ).combine().list()
        assert list[0] == '00o'
        length = len(list)
        assert length == 620
        assert list[length - 1] == 'z9o'

    def test_between_three_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            is_range=True,
            suffix='o'
        ).combine().list()
        assert list[0] == '0o'
        length = len(list)
        assert length == 630
        assert list[length - 1] == 'z9o'


    def test_between_any_1(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            is_range=True,
            prefix='0',
            suffix='o'
        ).combine().list()
        assert list[0] == '00o'
        length = len(list)
        assert length == 36
        assert list[length - 1] == '0zo'

    def test_between_any_2(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            is_range=True,
            prefix='k',
            suffix='8'
        ).combine().list()
        assert list[0] == 'k08'
        length = len(list)
        assert length == 36
        assert list[length - 1] == 'kz8'

