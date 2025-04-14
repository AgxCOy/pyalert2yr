# -*- encoding: utf-8 -*-
# @File   : test_csf.py
# @Time   : 2025/02/22 01:36:25
# @Author : NyaCl

# TODO: using pytest temp fixtures instead of std
from tempfile import NamedTemporaryFile as NamedTempFile

from pytest import fixture, FixtureRequest

from pyalert2yr.csf.model import *
from pyalert2yr.csf.parser import *


@fixture
def sample_csf() -> CsfDocument:
    csf = CsfDocument()
    csf['msg:NyaCl'] = 'NyaCl@ChlorideLab'
    csf['msg:nyacl'] = 'ChlorideP'  # expect a warning
    csf['msg:AiCoreIn'] = CsfVal(
        value='AiCoreIn@Meloland',
        extra='melorenae'
    )
    csf['msg:Shimakaze'] = [  # expect an incomatible warning
        CsfVal(value='frg2089@ShimakazeProject', extra='frg2089'),
        CsfVal(value='daofeng@StarryOrbitStudio')
    ]
    return csf


def test_csf_model(sample_csf: CsfDocument) -> None:
    assert isinstance(sample_csf['msg:NyaCl'],
                      CsfVal) and sample_csf['msg:NyaCl'].extra is None
    assert sample_csf['msg:AiCoreIn'].extra is not None
    assert sample_csf['msg:Shimakaze'].value == 'frg2089@ShimakazeProject'
    assert len(sample_csf.get_all_vals('msg:Shimakaze')) == 2
    assert sample_csf.header.numlabels == 3
    assert sample_csf.header.numvalues == 4


def test_csf_llf_parser(request: FixtureRequest) -> None:
    llf = CsfLLangParser(f"{request.path.parent}/ra2md.llf").read()
    RAW_CNT = 5211
    ERR_CNT = 3
    assert len(llf) == RAW_CNT - ERR_CNT
    assert 'NAME: Cntrpunch' not in llf

    llf['NAME: Cntrpunch'] = 'Cntrpunch'
    with NamedTempFile('r+', encoding='utf-8', suffix='.llf') as f:
        CsfLLangParser(f.name).write(llf)
        f.seek(0)
        _, len_ = f.readline(), f.readline()
    cnt = int(len_.split(': ')[-1])
    assert cnt == RAW_CNT - ERR_CNT + 1


def test_csf_parser(sample_csf: CsfDocument) -> None:
    with NamedTempFile('r+', encoding='utf-8', suffix='.csf') as f:
        CsfFileParser(f.name).write(sample_csf)
        f.seek(0)
        csf = CsfFileParser(f.name).read()
    assert csf.header.numvalues == 4
    assert len(csf) == 3 and 'msg:NyaCl' in csf


def test_csf_json_parser(
    request: FixtureRequest,
    sample_csf: CsfDocument
) -> None:
    ra2md = CsfJsonV2Parser(f"{request.path.parent}/ra2md.v2.json").read()
    ra2md.update(sample_csf)
    # MutableMapping may __getitem__ first and __setitem__.
    # expect only one value for 'msg:Shimakaze'
    assert len(ra2md.get_all_vals('msg:Shimakaze')) == 1
    with NamedTempFile('w', encoding='utf-8', suffix='.json') as f:
        CsfJsonV2Parser(f.name).write(ra2md)


def test_csf_xml_parser(request: FixtureRequest) -> None:
    ra2md = CsfXmlParser(f"{request.path.parent}/ra2md.xml").read()
    themes = [i for i in ra2md.keys() if i.startswith('THEME:')]
    assert len(themes) == 36
    with NamedTempFile('w', encoding='utf-8', suffix='.xml') as f:
        CsfXmlParser(f.name).write(ra2md)
