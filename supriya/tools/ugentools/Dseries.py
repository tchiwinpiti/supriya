# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.CalculationRate import CalculationRate
from supriya.tools.ugentools.DUGen import DUGen


class Dseries(DUGen):
    r'''A demand-rate arithmetic series.

    ::

        >>> dseries = ugentools.Dseries.new(
        ...     length=float('inf'),
        ...     start=1,
        ...     step=1,
        ...     )
        >>> dseries
        Dseries()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Demand UGens'

    __slots__ = ()

    _ordered_input_names = (
        'start',
        'step',
        'length',
        )

    _valid_calculation_rates = (
        CalculationRate.DEMAND,
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        length=float('inf'),
        start=1,
        step=1,
        ):
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.DEMAND
        if length is None:
            length = float('inf')
        DUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            length=length,
            start=start,
            step=step,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        length=float('inf'),
        start=1,
        step=1,
        ):
        r'''Constructs a Dseries.

        ::

            >>> dseries = ugentools.Dseries.new(
            ...     length=float('inf'),
            ...     start=1,
            ...     step=1,
            ...     )
            >>> dseries
            Dseries()

        Returns ugen graph.
        '''
        ugen = cls._new_expanded(
            length=length,
            start=start,
            step=step,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def length(self):
        r'''Gets `length` input of Dseries.

        ::

            >>> dseries = ugentools.Dseries.new(
            ...     length=float('inf'),
            ...     start=1,
            ...     step=1,
            ...     )
            >>> dseries.length
            inf

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('length')
        return self._inputs[index]

    @property
    def start(self):
        r'''Gets `start` input of Dseries.

        ::

            >>> dseries = ugentools.Dseries.new(
            ...     length=float('inf'),
            ...     start=1,
            ...     step=1,
            ...     )
            >>> dseries.start
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('start')
        return self._inputs[index]

    @property
    def step(self):
        r'''Gets `step` input of Dseries.

        ::

            >>> dseries = ugentools.Dseries.new(
            ...     length=float('inf'),
            ...     start=1,
            ...     step=1,
            ...     )
            >>> dseries.step
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('step')
        return self._inputs[index]