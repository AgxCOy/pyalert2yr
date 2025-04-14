# -*- encoding: utf-8 -*-
# @File   : utils.py
# @Time   : 2025/03/10 10:54:13
# @Author : NyaCl

from typing import Callable

from .model import IniSectionProxy, IniClass


def foreach_pairs(
    ini: IniClass, section_name: str, /,
    pair_func: Callable[[str, str], None],
    override_parent: bool = False
) -> None:
    """
    批处理指定小节的所有键值对。

    :param ini: INI 文件对象。
    :param section_name: 小节名。
    :param pair_func: 处理函数。
    :param override_parent: 是否覆盖父小节。
    """
    section = ini[section_name]
    for k, v in section.items():
        pair_func(k, v)
