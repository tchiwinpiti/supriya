from supriya.synthdefs.CalculationRate import CalculationRate
from supriya.ugens.Filter import Filter


class LagUD(Filter):
    """
    An up/down lag generator.

    ::

        >>> source = supriya.ugens.In.kr(bus=0)
        >>> supriya.ugens.LagUD.kr(
        ...     lag_time_down=1.25,
        ...     lag_time_up=0.5,
        ...     source=source,
        ...     )
        LagUD.kr()

    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'lag_time_up',
        'lag_time_down',
        )

    _valid_rates = (
        CalculationRate.AUDIO,
        CalculationRate.CONTROL,
        )

    ### INITIALIZER ###

    def __init__(
        self,
        lag_time_down=0.1,
        lag_time_up=0.1,
        calculation_rate=None,
        source=None,
        ):
        Filter.__init__(
            self,
            lag_time_down=lag_time_down,
            lag_time_up=lag_time_up,
            calculation_rate=calculation_rate,
            source=source,
            )

    ### PRIVATE METHODS ###

    @classmethod
    def _new_single(
        cls,
        lag_time_down=None,
        lag_time_up=None,
        calculation_rate=None,
        source=None,
        ):
        if lag_time_up == 0 and lag_time_down == 0:
            return source
        source_rate = CalculationRate.from_input(source)
        if source_rate == CalculationRate.SCALAR:
            return source
        ugen = cls(
            lag_time_down=lag_time_down,
            lag_time_up=lag_time_up,
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        lag_time_down=0.1,
        lag_time_up=0.1,
        source=None,
        ):
        """
        Constructs a control-rate lag.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> supriya.ugens.LagUD.ar(
            ...     lag_time_down=1.25,
            ...     lag_time_up=0.5,
            ...     source=source,
            ...     )
            LagUD.ar()

        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            lag_time_down=lag_time_down,
            lag_time_up=lag_time_up,
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        lag_time_down=0.1,
        lag_time_up=0.1,
        source=None,
        ):
        """
        Constructs a control-rate lag.

        ::

            >>> source = supriya.ugens.In.kr(bus=0)
            >>> supriya.ugens.LagUD.kr(
            ...     lag_time_down=1.25,
            ...     lag_time_up=0.5,
            ...     source=source,
            ...     )
            LagUD.kr()

        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            lag_time_down=lag_time_down,
            lag_time_up=lag_time_up,
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def lag_time_down(self):
        """
        Gets `lag_time_down` input of LagUD.

        ::

            >>> lag_time_down = 1.25
            >>> source = supriya.ugens.In.kr(bus=0)
            >>> lag_ud = supriya.ugens.LagUD.ar(
            ...     lag_time_down=lag_time_down,
            ...     source=source,
            ...     )
            >>> lag_ud.lag_time_down
            1.25

        Returns input.
        """
        index = self._ordered_input_names.index('lag_time_down')
        return self._inputs[index]

    @property
    def lag_time_up(self):
        """
        Gets `lag_time_up` input of LagUD.

        ::

            >>> lag_time_up = 0.5
            >>> source = supriya.ugens.In.kr(bus=0)
            >>> lag_ud = supriya.ugens.LagUD.ar(
            ...     lag_time_up=lag_time_up,
            ...     source=source,
            ...     )
            >>> lag_ud.lag_time_up
            0.5

        Returns input.
        """
        index = self._ordered_input_names.index('lag_time_up')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of LagUD.

        ::

            >>> source = supriya.ugens.In.kr(bus=0)
            >>> lag_ud = supriya.ugens.LagUD.ar(
            ...     source=source,
            ...     )
            >>> lag_ud.source
            In.kr()[0]

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
