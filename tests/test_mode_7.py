import pytest

from genstr import Genstr
from genstr import Mode


class TestMode7:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mode = Mode.CUSTOM_EXCLUDE_PURE
        self.alphabets = '3456789qwertyupasdfghjkxcvbnm'

    def test_00_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets
        ).combine().list()
        assert list[0] == '3q'
        length = len(list)
        assert length == 308
        assert list[length - 1] == 'm9'

    def test_0_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True
        ).combine().list()
        assert list[0] == '3q'
        length = len(list)
        assert length == 308
        assert list[length - 1] == 'm9'

    def test_between_one_p(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'a3'
        length = len(list)
        assert length == 7
        assert list[length - 1] == 'a9'


    def test_between_two_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            prefix='a'
        ).combine().list()
        assert list[0] == 'a33'
        length = len(list)
        assert length == 357
        assert list[length - 1] == 'am9'

    def test_between_three_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'a3'
        length = len(list)
        assert length == 364
        assert list[length - 1] == 'am9'


    def test_between_one_s(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            suffix='o'
        ).combine().list()
        assert list[0] == '3o'
        length = len(list)
        assert length == 7
        assert list[length - 1] == '9o'


    def test_between_two_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            suffix='o'
        ).combine().list()
        assert list[0] == '33o'
        length = len(list)
        assert length == 357
        assert list[length - 1] == 'm9o'

    def test_between_three_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            suffix='o'
        ).combine().list()
        assert list[0] == '3o'
        length = len(list)
        assert length == 364
        assert list[length - 1] == 'm9o'


    def test_between_any_1(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            prefix='0',
            suffix='o'
        ).combine().list()
        assert list[0] == '03o'
        length = len(list)
        assert length == 29
        assert list[length - 1] == '0mo'

    def test_between_any_2(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            alphabets=self.alphabets,
            is_range=True,
            prefix='k',
            suffix='8'
        ).combine().list()
        assert list[0] == 'k38'
        length = len(list)
        assert length == 29
        assert list[length - 1] == 'km8'

