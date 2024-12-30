import pytest

from genstr import Genstr
from genstr import Mode


class TestMode8:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mode = Mode.CUSTOM_PURE_NUMBERS_LETTERS
        self.alphabets = '3456789qwertyupasdfghjkxcvbnm'

    def test_00_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets
        ).combine().list()
        assert list[0] == '33'
        length = len(list)
        assert length == 533
        assert list[length - 1] == 'mm'

    def test_0_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True
        ).combine().list()
        assert list[0] == '3'
        length = len(list)
        assert length == 562
        assert list[length - 1] == 'mm'

    def test_between_one_p(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aq'
        length = len(list)
        assert length == 22
        assert list[length - 1] == 'am'


    def test_between_two_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aqq'
        length = len(list)
        assert length == 484
        assert list[length - 1] == 'amm'

    def test_between_three_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aq'
        length = len(list)
        assert length == 506
        assert list[length - 1] == 'amm'


    def test_between_one_s(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            suffix='o'
        ).combine().list()
        assert list[0] == 'qo'
        length = len(list)
        assert length == 22
        assert list[length - 1] == 'mo'


    def test_between_two_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            suffix='o'
        ).combine().list()
        assert list[0] == 'qqo'
        length = len(list)
        assert length == 484
        assert list[length - 1] == 'mmo'

    def test_between_three_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            suffix='o'
        ).combine().list()
        assert list[0] == 'qo'
        length = len(list)
        assert length == 506
        assert list[length - 1] == 'mmo'
