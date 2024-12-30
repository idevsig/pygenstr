import argparse
import itertools
import sys
import textwrap

from genstr.utils import is_characters
from genstr.utils import is_pure_character
from genstr.utils import Mode

version = '0.1.1'

class Genstr:
    """
    字符串生成器
    """

    def __init__(self,
        length: int,
        mode: Mode = Mode.PURE_NUMBERS,
        alphabets: str = '',
        prefix: str = '',
        suffix: str = '',
        is_range: bool = False
    ):

        self._length = length
        self._mode = mode
        self._alphabets = alphabets
        self._prefix = prefix
        self._suffix = suffix
        self._range = is_range

        self.str_list= [] # 无后缀的字符串列表

        self.characters = '' # 字符串组合字符

    def filter_string(self, filter):
        """
        过滤字符串数组
        """
        if not filter:
            return self

        try:
            index = self.str_list.index(str(filter))
            self.str_list = self.str_list[index:]
        except Exception as e:
            print(f'Error: {e}')
        return self

    def combine(self):
        """
        生成组合数据
        """
        # 若前缀后缀相加，等于长度，直接返回
        fill_characters = f"{self._prefix}{self._suffix}"
        if not is_characters(fill_characters):
            raise ValueError('前缀后缀必须是数字或字母组合')

        if len(fill_characters) == self._length:
            self.str_list = [fill_characters]
            return self

        match self._mode:
            case Mode.PURE_NUMBERS: # 1. 纯数字
                if fill_characters and not fill_characters.isdigit():
                    raise ValueError('前缀后缀必须是纯数字')
                self.add_pure_numbers(True)

            case Mode.PURE_LETTERS: # 2. 纯字母
                if fill_characters and not fill_characters.isalpha():
                    raise ValueError('前缀后缀必须是纯字母')
                self.add_pure_letters(True)

            case Mode.PURE_NUMBERS_LETTERS: # 3.纯数字+纯字母
                self.add_pure_numbers(True) \
                    .padding_prefix_suffix()\
                    .add_pure_letters(True)

            case Mode.MIXED_CHARACTERS: # 4. 数字与字母混合（杂米+纯字母+纯数字）
                self.add_pure_numbers().add_pure_letters(False)

            case Mode.MIXED_EXCLUDE_PURE: # 5.杂米（排除纯数字和纯字母）
                self.add_pure_numbers().add_pure_letters(False)

            case Mode.CUSTOM_CHARACTERS: # 6. 自定义字符
                self.set_custom_characters(self._alphabets)

            case Mode.CUSTOM_EXCLUDE_PURE: # 7. 自定义字符（杂米，排除纯数字和纯字母）
                self.set_custom_characters(self._alphabets)

            case Mode.CUSTOM_PURE_NUMBERS_LETTERS: # 8. 自定义字符（纯数字和纯字母）
                self.set_custom_characters(self._alphabets)

            case _:
                raise ValueError(f'组合模式必须在 1~8 之间,当前为 {self._mode}')

        # 过滤
        #self.filter_string(strs, self.starting_character)
        # 添加字符串后缀
        self.padding_prefix_suffix()
        return self

    def gen_only_number(self, min=0, max=9):
        """
        生成 0-9 的数字
        """
        return ''.join(str(i) for i in range(min, max + 1))

    def gen_only_letters(self):
        """
        生成 a-z 的字符串
        """
        return ''.join(chr(i) for i in range(97, 123))

    def add_pure_numbers(self, only = True):
        """
        添加纯数字
        """
        # self.characters += '0123456789'
        characters = self.gen_only_number()
        self.characters = characters if only else self.characters + characters
        return self

    def add_pure_letters(self, only = True):
        """
        添加纯字母
        """
        characters = self.gen_only_letters()
        self.characters = characters if only else self.characters + characters
        return self

    def set_custom_characters(self, characters):
        """
        设置为自定义字符
        """
        self.characters = characters
        return self

    def generate_list(self, length: int):
        """
        组合字符串数据列表
        """
        repeat = length - len(self._prefix + self._suffix)
        # print(self.characters, length, repeat)
        if repeat <= 0:
            return list()
        return list(itertools.product(self.characters, repeat=repeat))

    def generate_numbers_letters(self, iter_list: tuple, pure = False):
        """
        生成同时包含字母和数字的组合
        only: 纯数字或纯字母
        """
        str_list = []

        for chars in iter_list:
            str = ''.join(chars)

            if (is_pure_character(str, pure)):
                str_list.append(str)

        return str_list

    def generate_iter_combinations(self, length: int):
        """
        生成数据池
        """
        iter_combinations = self.generate_list(length)
        if self._mode == Mode.MIXED_EXCLUDE_PURE or \
            self._mode == Mode.CUSTOM_EXCLUDE_PURE: # 排除模式：杂米
            iter_combinations = self.generate_numbers_letters(iter_combinations)
        elif self._mode == Mode.CUSTOM_PURE_NUMBERS_LETTERS: # 排除模式：纯数字或纯字母
            iter_combinations = self.generate_numbers_letters(iter_combinations, True)
        return iter_combinations

    def padding_prefix_suffix(self, append = False):
        """
        字符串添加前缀和后缀
        """
        iter_combinations = []
        if not self._range:
            iter_combinations.extend(self.generate_list(self._length))
        else:
            for i in range(1, self._length + 1):
                iter_combinations.extend(self.generate_list(i))

        # 添加前后缀
        str_list = [
            f"{self._prefix}{''.join(combination)}{self._suffix}"
            for combination in iter_combinations
        ]

        new_str_list = []
        # 再次检测纯字符的匹配
        match self._mode:
            # 只纯字母或纯数字
            case Mode.PURE_NUMBERS | Mode.PURE_LETTERS | Mode.PURE_NUMBERS_LETTERS | Mode.CUSTOM_PURE_NUMBERS_LETTERS:
                new_str_list = [ str for str in str_list if is_pure_character(str, True)]
            # 排除纯字母和纯数字
            case Mode.MIXED_EXCLUDE_PURE | Mode.CUSTOM_EXCLUDE_PURE:
                new_str_list = [str for str in str_list if is_pure_character(str, False)]
            # 所有字䇴
            case _:
                new_str_list = str_list

        self.str_list = new_str_list if append else self.str_list + new_str_list
        return self

    def list(self):
        return self.str_list

    def clear_characters(self):
        """
        清空字符
        """
        self.characters = ''
        return self

def parse_arguments():
    '''
    解析命令行参数
    '''
    parser = argparse.ArgumentParser(description='按指定规则生成字符串', add_help=False)

    help_mode_text = textwrap.dedent("""\
    组合模式:
    1. 纯数字
    2. 纯字母
    3. 纯数字+纯字母
    4. 字符混合
    5. 字符混合：所有-纯字母-纯数字
    6. 自定义字符
    7. 自定义字符：所有-纯字母-纯数字
    8. 自定义字符：纯字母+纯数字
    """)

    parser.add_argument(
        '-l',
        '--length',
        type=int,
        help='长度，含组合前缀和后缀',
    )

    parser.add_argument(
        '-m',
        '--mode',
        type=int,
        help=help_mode_text
    )

    parser.add_argument(
        '-r',
        '--range',
        action='store_true',
        help='范围，如长度为 3 时，则范围为 1-3 内的数据',
    )

    parser.add_argument(
        '-A',
        '--alphabets',
        type=str,
        help='自定义组合字母表，-m 6/7/8 必填',
    )

    parser.add_argument(
        '-P',
        '--prefix',
        type=str,
        help='组合前缀，如 -P a，则生成 a*',
    )

    parser.add_argument(
        '-S',
        '--suffix',
        type=str,
        help='组合后缀，如 -S z，则生成 *z',
    )

    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help='打印帮助信息'
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s ' + version,
        help='打印版本信息',
    )

    args = parser.parse_args()
    return args

def update_args(args):
    '''
    更新配置参数
    '''
    args.mode = args.mode if args.mode else 1
    args.length = args.length if args.length else 1
    args.prefix = args.prefix if args.prefix else ''
    args.suffix = args.suffix if args.suffix else ''
    args.alphabets = args.alphabets if args.alphabets else ''
    args.range = args.range if args.range else False

    args.mode = Mode(args.mode)

    # 组合模式 必须在 1~8 之间
    if isinstance(args.mode, Mode) is False:
        raise ValueError('组合模式必须在 1~8 之间')

    # 组合模式 6 或 7，字母表不能为空
    if args.mode == Mode.CUSTOM_CHARACTERS or \
        args.mode == Mode.CUSTOM_EXCLUDE_PURE or \
            args.mode == Mode.CUSTOM_PURE_NUMBERS_LETTERS:
        if not args.alphabets or args.alphabets == '':
            raise ValueError('组合模式 6~8，字母表不能为空')
    else: # 其它模式，字母表为空
        args.alphabets = ''

    # 字符串长度 必须在 1~10 之间
    if args.length < 1 or args.length > 10:
        raise ValueError('字符串长度必须在 1~10 之间')

    # 字符串前缀和后缀相加不得大于字符串长度
    if len(str(args.prefix) + str(args.suffix)) > args.length:
        raise ValueError('字符串前缀和后缀相加不得大于字符串长度')

    return args

def main():
    try:
        args = parse_arguments()
        # print(args)
        new_args = update_args(args)
        # print(new_args)

        list = Genstr(
            length=new_args.length,
            mode=new_args.mode,
            alphabets=new_args.alphabets,
            prefix=new_args.prefix,
            suffix=new_args.suffix,
            is_range=new_args.range
        ).combine().list()

        print(','.join(list)) if len(list) > 0 else print(list)

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)
