from supriya.ugens.Filter import Filter


class Ringz(Filter):
    """
    A ringing filter.

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> ringz = supriya.ugens.Ringz.ar(
        ...     decay_time=1,
        ...     frequency=440,
        ...     source=source,
        ...     )
        >>> ringz
        Ringz.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Filter UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'frequency',
        'decay_time',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        decay_time=1,
        frequency=440,
        source=None,
        ):
        Filter.__init__(
            self,
            calculation_rate=calculation_rate,
            decay_time=decay_time,
            frequency=frequency,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        decay_time=1,
        frequency=440,
        source=None,
        ):
        """
        Constructs an audio-rate Ringz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> ringz = supriya.ugens.Ringz.ar(
            ...     decay_time=1,
            ...     frequency=440,
            ...     source=source,
            ...     )
            >>> ringz
            Ringz.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            decay_time=decay_time,
            frequency=frequency,
            source=source,
            )
        return ugen

    # def coeffs(): ...

    @classmethod
    def kr(
        cls,
        decay_time=1,
        frequency=440,
        source=None,
        ):
        """
        Constructs a control-rate Ringz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> ringz = supriya.ugens.Ringz.kr(
            ...     decay_time=1,
            ...     frequency=440,
            ...     source=source,
            ...     )
            >>> ringz
            Ringz.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            decay_time=decay_time,
            frequency=frequency,
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
    def decay_time(self):
        """
        Gets `decay_time` input of Ringz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> ringz = supriya.ugens.Ringz.ar(
            ...     decay_time=1,
            ...     frequency=440,
            ...     source=source,
            ...     )
            >>> ringz.decay_time
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('decay_time')
        return self._inputs[index]

    @property
    def frequency(self):
        """
        Gets `frequency` input of Ringz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> ringz = supriya.ugens.Ringz.ar(
            ...     decay_time=1,
            ...     frequency=440,
            ...     source=source,
            ...     )
            >>> ringz.frequency
            440.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('frequency')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of Ringz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> ringz = supriya.ugens.Ringz.ar(
            ...     decay_time=1,
            ...     frequency=440,
            ...     source=source,
            ...     )
            >>> ringz.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
