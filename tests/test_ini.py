# -*- encoding: utf-8 -*-
# @File   : test_ini.py
# @Time   : 2025/02/22 01:36:38
# @Author : NyaCl

from pytest import fixture, FixtureRequest

# TODO: complete ini testing
# - read/write without error or misunderstanding
# - model handling INI grammar expansion without misunderstanding
# - operation assertion (like INI section inheritance MRO).


@fixture
def ares_ini(request: FixtureRequest) -> str:
    """at least `+=` and `[sub]:[super]` validation."""
    with open(f'{request.path.parent}/sample_ares.ini', 'r',
              encoding='utf-8') as f:
        return f.read()


@fixture
def phobos_ini(request: FixtureRequest) -> str:
    """at least `$Inherits` validation."""
    with open(f'{request.path.parent}/sample_phobos.ini', 'r',
              encoding='utf-8') as f:
        return f.read()


def test_ini_model() -> None:
    ...


class IniParserTest:
    def test_readstream(self) -> None:
        ...

    def test_decode_file(self) -> None:
        ...

    def test_read(self) -> None:
        ...

    def test_write(self) -> None:
        ...


@fixture
def prepare_ini_tree():  # type: ignore
    ...  # setup
    yield


def test_ini_tree_parser(prepare_ini_tree) -> None:  # type: ignore
    ...
