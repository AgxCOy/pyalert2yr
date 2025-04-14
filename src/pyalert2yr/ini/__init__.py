# -*- encoding: utf-8 -*-
# @File   : __init__.py
# @Time   : 2024/10/10 01:16:53
# @Author : Kariko Lin

from .model import IniSectionProxy, IniClass
from .parser import IniParser, IniTreeParser


# 讲道理在不保证 INI 树完整的情况下，我也不好说什么实现更合理一些。
# 弄继承还要考虑 INI 默认值问题。只是`<undefined>`可能并不合理。
# 但我也没什么更好的办法。

# TODO: redesign ini model and proxy
# for parser, needs rearranging the io process.
# like, iniparser, initreeparser, aresiniparser, phobosiniparser.

# basically ini model may focus on concept abstraction, like inheritance
# and +=.

# for including, it's too difficult to manage ini document instances tree,
# even key-val traversal between nodes.
# so just merge them into one (in whatever parser).

# so the main problem is to design an easier interface to let user know
# how to manage inheritances (add, remove, find, change),
# instead of considering which extension they use, whether "$Inherits"
# appears in section or not.

# formerly i used tree maintaining which makes child points to parent,
# but it couldn't handle phobos-multiple-inheritance like Python does.

# A newer design currently used is to make a proxy like stdlib "configparser",
# but still got issues:
# 1. proxy may lost track and all changes in proxy couldn't commit to raw dict
#    handled by IniClass.
# 2. some API in MutableMapping may got infinite cycling, as pairs from parents
#    is READ-ONLY, and never able to be deleted.
