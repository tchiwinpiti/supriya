# -*- encoding: utf-8 -*-
from supriya import synthdefs
from supriya.tools import nonrealtimetools
from supriya.tools import patterntools
from supriya.tools import synthdeftools
from supriya.tools import ugentools
from nonrealtimetools_testbase import TestCase


class TestCase(TestCase):

    def test_manual_with_gate(self):
        session = nonrealtimetools.Session(0, 2)
        with session.at(0):
            group = session.add_group(duration=4)
        for i in range(4):
            with session.at(i):
                group.add_synth(duration=0)
        assert session.to_lists(duration=5) == [
            [0.0, [
                ['/d_recv', bytearray(synthdefs.default.compile())],
                ['/g_new', 1000, 0, 0],
                ['/s_new', 'da0982184cc8fa54cf9d288a0fe1f6ca', 1001, 0, 1000],
                ['/n_set', 1001, 'gate', 0]]],
            [1.0, [
                ['/s_new', 'da0982184cc8fa54cf9d288a0fe1f6ca', 1002, 0, 1000],
                ['/n_set', 1002, 'gate', 0]]],
            [2.0, [
                ['/s_new', 'da0982184cc8fa54cf9d288a0fe1f6ca', 1003, 0, 1000],
                ['/n_set', 1003, 'gate', 0]]],
            [3.0, [
                ['/s_new', 'da0982184cc8fa54cf9d288a0fe1f6ca', 1004, 0, 1000],
                ['/n_set', 1004, 'gate', 0]]],
            [4.0, [['/n_free', 1000]]],
            [5.0, [[0]]]]

    def test_manual_without_gate(self):
        with synthdeftools.SynthDefBuilder() as builder:
            source = ugentools.DC.ar(1)
            ugentools.Out.ar(bus=0, source=source)
        source_synthdef = builder.build()
        session = nonrealtimetools.Session(0, 1)
        with session.at(0):
            group = session.add_group(duration=4)
        for i in range(4):
            with session.at(i):
                group.add_synth(duration=0, synthdef=source_synthdef)
        assert session.to_lists(duration=10) == [
            [0.0, [
                ['/d_recv', bytearray(source_synthdef.compile())],
                ['/g_new', 1000, 0, 0],
                ['/s_new', '7839f99c38c2ac4326388a013cdd643c', 1001, 0, 1000]]],
            [1.0, [['/s_new', '7839f99c38c2ac4326388a013cdd643c', 1002, 0, 1000]]],
            [2.0, [['/s_new', '7839f99c38c2ac4326388a013cdd643c', 1003, 0, 1000]]],
            [3.0, [['/s_new', '7839f99c38c2ac4326388a013cdd643c', 1004, 0, 1000]]],
            [4.0, [['/n_free', 1000]]],
            [10.0, [[0]]]]

    def test_pattern_without_gate(self):
        with synthdeftools.SynthDefBuilder() as builder:
            source = ugentools.DC.ar(1)
            ugentools.Out.ar(bus=0, source=source)
        source_synthdef = builder.build()
        pattern = patterntools.Pbind(
            delta=1,
            duration=0,
            synthdef=source_synthdef,
            ).with_group()
        session = nonrealtimetools.Session(0, 1)
        with session.at(0):
            session.inscribe(pattern, duration=4)
        assert session.to_lists(duration=10) == [
            [0.0, [
                ['/d_recv', bytearray(source_synthdef.compile())],
                ['/g_new', 1000, 0, 0],
                ['/s_new', '7839f99c38c2ac4326388a013cdd643c', 1001, 0, 1000]]],
            [1.0, [['/s_new', '7839f99c38c2ac4326388a013cdd643c', 1002, 0, 1000]]],
            [2.0, [['/s_new', '7839f99c38c2ac4326388a013cdd643c', 1003, 0, 1000]]],
            [3.0, [['/s_new', '7839f99c38c2ac4326388a013cdd643c', 1004, 0, 1000]]],
            [4.25, [['/n_free', 1000]]],
            [10.0, [[0]]]]
