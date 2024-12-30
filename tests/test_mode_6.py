import pytest

from genstr import Genstr
from genstr import Mode


class TestMode6:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mode = Mode.CUSTOM_CHARACTERS
        self.alphabets = 'qwertyupasdfghjkxcvbnm3456789'

    def test_00_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets
        ).combine().list()
        assert list[0] == 'qq'
        length = len(list)
        assert length == 841
        assert list[length - 1] == '99'

    def test_0_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True
        ).combine().list()
        assert list[0] == 'q'
        length = len(list)
        assert length == 870
        assert list[length - 1] == '99'

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
        assert length == 29
        assert list[length - 1] == 'a9'


    def test_between_two_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aqq'
        length = len(list)
        assert length == 841
        assert list[length - 1] == 'a99'

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
        assert length == 870
        assert list[length - 1] == 'a99'


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
        assert length == 29
        assert list[length - 1] == '9o'


    def test_between_two_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            suffix='o'
        ).combine().list()
        assert list[0] == 'qqo'
        length = len(list)
        assert length == 841
        assert list[length - 1] == '99o'

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
        assert length == 870
        assert list[length - 1] == '99o'


    def test_between_any_1(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            prefix='0',
            suffix='o'
        ).combine().list()
        assert list[0] == '0qo'
        length = len(list)
        assert length == 29
        assert list[length - 1] == '09o'

    def test_between_any_2(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            prefix='k',
            suffix='8'
        ).combine().list()
        assert list[0] == 'kq8'
        length = len(list)
        assert length == 29
        assert list[length - 1] == 'k98'

