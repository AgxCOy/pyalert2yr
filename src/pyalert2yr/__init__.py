# -*- encoding: utf-8 -*-
# @File   : __init__.py
# @Time   : 2023/11/14 20:01:52
# @Author : Chloride

from . import maps
from .csf import (CsfDocument, CsfFileParser, CsfJsonV2Parser, CsfLLangParser,
                  CsfVal, CsfXmlParser)
from .ini import IniClass, IniParser, IniSectionProxy, IniTreeParser

__version__ = '3.0.0-dev241018'

PKG_NAME = f'pyalert2yr v{__version__}'
PKG_DESC = 'RA2 Map dev toolkits for Python 3.'
PKG_URL = 'https://github.com/ChlorideP/pyalert2yr'
