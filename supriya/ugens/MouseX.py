from supriya.synthdefs.CalculationRate import CalculationRate
from supriya.synthdefs.SignalRange import SignalRange
from supriya.ugens.UGen import UGen


class MouseX(UGen):
    """
    A mouse cursor tracker.

    MouseX tracks the y-axis of the mouse cursor position.

    ::

        >>> supriya.ugens.MouseX.kr()
        MouseX.kr()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'User Interaction UGens'

    __slots__ = ()

    _ordered_input_names = (
        'minimum',
        'maximum',
        'warp',
        'lag',
        )

    _signal_range = SignalRange.UNIPOLAR

    _valid_calculation_rates = (
        CalculationRate.CONTROL,
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        lag=0.2,
        maximum=1,
        minimum=0,
        warp=0,
        ):
        warp = int(bool(warp))
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            lag=lag,
            maximum=maximum,
            minimum=minimum,
            warp=warp,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def kr(
        cls,
        lag=0.2,
        maximum=1,
        minimum=0,
        warp=0,
        ):
        """
        Constructs a control-rate mouse cursor tracking unit generator.

        ::

            >>> supriya.ugens.MouseX.kr(
            ...     lag=0.2,
            ...     maximum=1,
            ...     minimum=0,
            ...     warp=1,
            ...     )
            MouseX.kr()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            lag=lag,
            maximum=maximum,
            minimum=minimum,
            warp=warp,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def lag(self):
        """
        Gets `lag` input of MouseX.

        ::

            >>> mouse_x = supriya.ugens.MouseX.kr(
            ...     lag=0.2,
            ...     maximum=1,
            ...     minimum=0,
            ...     warp=1,
            ...     )
            >>> mouse_x.lag
            0.2

        Returns ugen input.
        """
        index = self._ordered_input_names.index('lag')
        return self._inputs[index]

    @property
    def maximum(self):
        """
        Gets `maximum` input of MouseX.

        ::

            >>> mouse_x = supriya.ugens.MouseX.kr(
            ...     lag=0.2,
            ...     maximum=1,
            ...     minimum=0,
            ...     warp=1,
            ...     )
            >>> mouse_x.maximum
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('maximum')
        return self._inputs[index]

    @property
    def minimum(self):
        """
        Gets `minimum` input of MouseX.

        ::

            >>> mouse_x = supriya.ugens.MouseX.kr(
            ...     lag=0.2,
            ...     maximum=1,
            ...     minimum=0,
            ...     warp=1,
            ...     )
            >>> mouse_x.minimum
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('minimum')
        return self._inputs[index]

    @property
    def warp(self):
        """
        Gets `warp` input of MouseX.

        ::

            >>> mouse_x = supriya.ugens.MouseX.kr(
            ...     lag=0.2,
            ...     maximum=1,
            ...     minimum=0,
            ...     warp=1,
            ...     )
            >>> mouse_x.warp
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('warp')
        return self._inputs[index]
