from supriya.synthdefs.CalculationRate import CalculationRate
from supriya.ugens.Filter import Filter


class Lag2UD(Filter):
    """
    An up/down exponential lag generator.

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> lag_2_ud = supriya.ugens.Lag2UD.ar(
        ...     lag_time_d=0.1,
        ...     lag_time_u=0.1,
        ...     source=source,
        ...     )
        >>> lag_2_ud
        Lag2UD.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Filter UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'lag_time_u',
        'lag_time_d',
        )

    _valid_rates = (
        CalculationRate.AUDIO,
        CalculationRate.CONTROL,
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        lag_time_d=0.1,
        lag_time_u=0.1,
        source=None,
        ):
        Filter.__init__(
            self,
            calculation_rate=calculation_rate,
            lag_time_d=lag_time_d,
            lag_time_u=lag_time_u,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        lag_time_d=0.1,
        lag_time_u=0.1,
        source=None,
        ):
        """
        Constructs an audio-rate Lag2UD.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> lag_2_ud = supriya.ugens.Lag2UD.ar(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=source,
            ...     )
            >>> lag_2_ud
            Lag2UD.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            lag_time_d=lag_time_d,
            lag_time_u=lag_time_u,
            source=source,
            )
        return ugen

    # def coeffs(): ...

    @classmethod
    def kr(
        cls,
        lag_time_d=0.1,
        lag_time_u=0.1,
        source=None,
        ):
        """
        Constructs a control-rate Lag2UD.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> lag_2_ud = supriya.ugens.Lag2UD.kr(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=source,
            ...     )
            >>> lag_2_ud
            Lag2UD.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            lag_time_d=lag_time_d,
            lag_time_u=lag_time_u,
            source=source,
            )
        return ugen

    # def magResponse(): ...

    # def magResponse2(): ...

    # def magResponse5(): ...

    # def magResponseN(): ...

    # def scopeResponse(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def lag_time_d(self):
        """
        Gets `lag_time_d` input of Lag2UD.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> lag_2_ud = supriya.ugens.Lag2UD.ar(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=source,
            ...     )
            >>> lag_2_ud.lag_time_d
            0.1

        Returns ugen input.
        """
        index = self._ordered_input_names.index('lag_time_d')
        return self._inputs[index]

    @property
    def lag_time_u(self):
        """
        Gets `lag_time_u` input of Lag2UD.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> lag_2_ud = supriya.ugens.Lag2UD.ar(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=source,
            ...     )
            >>> lag_2_ud.lag_time_u
            0.1

        Returns ugen input.
        """
        index = self._ordered_input_names.index('lag_time_u')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of Lag2UD.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> lag_2_ud = supriya.ugens.Lag2UD.ar(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=source,
            ...     )
            >>> lag_2_ud.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
