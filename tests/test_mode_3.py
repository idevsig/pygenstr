import pytest

from genstr import Genstr
from genstr import Mode


class TestMode3:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mode = Mode.PURE_NUMBERS_LETTERS

    def test_0_to_z(self):
        list = Genstr(
            length=1,
            mode=self.mode
        ).combine().list()
        assert list[0] == '0'
        length = len(list)
        assert length == 36
        assert list[length - 1] == 'z'

    def test_00_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode
        ).combine().list()
        assert list[0] == '00'
        length = len(list)
        assert length == 776
        assert list[length - 1] == 'zz'

    def test_0_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True
        ).combine().list()
        assert list[0] == '0'
        length = len(list)
        assert length == 812
        assert list[length - 1] == 'zz'

    def test_between_one_p(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aa'
        length = len(list)
        assert length == 26
        assert list[length - 1] == 'az'


    def test_between_two_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aaa'
        length = len(list)
        assert length == 676
        assert list[length - 1] == 'azz'

    def test_between_three_p(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aa'
        length = len(list)
        assert length == 702
        assert list[length - 1] == 'azz'


    def test_between_one_s(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True,
            suffix='o'
        ).combine().list()
        assert list[0] == 'ao'
        length = len(list)
        assert length == 26
        assert list[length - 1] == 'zo'


    def test_between_two_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            suffix='o'
        ).combine().list()
        assert list[0] == 'aao'
        length = len(list)
        assert length == 676
        assert list[length - 1] == 'zzo'

    def test_between_three_s(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            is_range=True,
            suffix='o'
        ).combine().list()
        assert list[0] == 'ao'
        length = len(list)
        assert length == 702
        assert list[length - 1] == 'zzo'

    def test_between_one_num(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            is_range=True,
            suffix='5'
        ).combine().list()
        assert list[0] == '05'
        length = len(list)
        assert length == 110
        assert list[length - 1] == '995'
