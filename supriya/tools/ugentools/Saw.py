# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.PureUGen import PureUGen


class Saw(PureUGen):
    r'''A band-limited sawtooth oscillator unit generator.

    ::

        >>> ugentools.Saw.ar()
        Saw.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Oscillator UGens'

    __slots__ = ()

    _ordered_input_names = (
        'frequency',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        frequency=440.,
        ):
        PureUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            frequency=frequency,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        frequency=440,
        ):
        r'''Constructs an audio-rate band-limited sawtooth oscillator.

        ::

            >>> ugentools.Saw.ar(
            ...     frequency=443,
            ...     )
            Saw.ar()

        Returns unit generator graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            frequency=frequency,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        frequency=440,
        ):
        r'''Constructs a control-rate band-limited sawtooth oscillator.

        ::

            >>> ugentools.Saw.kr(
            ...     frequency=443,
            ...     )
            Saw.kr()

        Returns unit generator graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            frequency=frequency,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def frequency(self):
        r'''Gets `frequency` input of Saw.

        ::

            >>> frequency = 443
            >>> saw = ugentools.Saw.ar(
            ...     frequency=frequency,
            ...     )
            >>> saw.frequency
            443.0

        Returns input.
        '''
        index = self._ordered_input_names.index('frequency')
        return self._inputs[index]