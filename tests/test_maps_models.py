# -*- encoding: utf-8 -*-
# @File   : test_maps_models.py
# @Time   : 2025/02/22 01:37:03
# @Author : NyaCl

from pytest import fixture

from pyalert2yr.maps.models import *


@fixture
def trigger_actions() -> str:
    return (
        '12,'
        '11,4,mission:all03_J,0,0,0,0,A,'
        '21,6,EVA_BattlefieldControlOnline,0,0,0,0,A,'
        '47,0,0,0,0,0,0,A,'
        '53,2,01000022,0,0,0,0,A,'
        '53,2,01000018,0,0,0,0,A,'
        '112,0,0,0,0,0,0,C,'
        '19,7,CameraSwitch,0,0,0,0,A,'
        '53,2,01000174,0,0,0,0,A,'
        '53,2,01000487,0,0,0,0,A,'
        '53,2,01000578,0,0,0,0,A,'
        '53,2,01000584,0,0,0,0,A,'
        '53,2,01000020,0,0,0,0,A'
    )


def test_actions_ptr(trigger_actions: str) -> None:
    with ActionsPointer(trigger_actions) as ptr:
        assert len(ptr) == 12
        assert ptr.current.p1_type == '4'
        while ptr.seekable:
            ptr.next()
        assert ptr.current.action_id == '53'


@fixture
def trigger_events() -> str:
    return (
        "2,"
        "61,2,1,CAPowrALNW,"
        "36,0,32"
    )


def test_events_ptr(trigger_events: str) -> None:
    with EventsPointer(trigger_events) as ptr:
        assert len(ptr) == 2
        assert ptr.current['extp2_switch'] == '2' and 'p2' in ptr.current
        ptr.next()
        assert 'p2' not in ptr.current
