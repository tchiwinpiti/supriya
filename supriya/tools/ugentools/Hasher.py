# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.UGen import UGen


class Hasher(UGen):
    r'''A signal hasher.

    ::

        >>> source = ugentools.SinOsc.ar()
        >>> hasher = ugentools.Hasher.ar(
        ...     source=source,
        ...     )
        >>> hasher
        Hasher.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Noise UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        source=0,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        source=0,
        ):
        r'''Constructs an audio-rate signal hasher.

        ::

            >>> source = ugentools.SinOsc.ar(frequency=[440, 442])
            >>> hasher = ugentools.Hasher.ar(
            ...     source=source,
            ...     )
            >>> hasher
            UGenArray({2})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        source=0,
        ):
        r'''Constructs a control-rate signal hasher.

        ::

            >>> source = ugentools.SinOsc.kr(frequency=[4, 2])
            >>> hasher = ugentools.Hasher.kr(
            ...     source=source,
            ...     )
            >>> hasher
            UGenArray({2})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen