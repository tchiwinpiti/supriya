from supriya.ugens.Filter import Filter


class Decay(Filter):
    """
    A leaky signal integrator.

    ::

        >>> source = supriya.ugens.Impulse.ar()
        >>> decay = supriya.ugens.Decay.ar(
        ...     source=source,
        ...     )
        >>> decay
        Decay.ar()

    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'decay_time',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        decay_time=1.0,
        calculation_rate=None,
        source=None,
        ):
        Filter.__init__(
            self,
            decay_time=decay_time,
            calculation_rate=calculation_rate,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        decay_time=1.0,
        source=None,
        ):
        """
        Constructs an audio-rate leaky signal integrator.

        ::

            >>> source = supriya.ugens.Impulse.ar(frequency=[100, 101])
            >>> decay = supriya.ugens.Decay.ar(
            ...     source=source,
            ...     )
            >>> decay
            UGenArray({2})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            decay_time=decay_time,
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        decay_time=1.0,
        source=None,
        ):
        """
        Constructs a control-rate leaky signal integrator.

        ::

            >>> source = supriya.ugens.Impulse.kr(frequency=[100, 101])
            >>> decay = supriya.ugens.Decay.kr(
            ...     source=source,
            ...     )
            >>> decay
            UGenArray({2})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            decay_time=decay_time,
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def decay_time(self):
        """
        Gets `decay_time` input of Decay.

        ::

            >>> decay_time = 1.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> decay = supriya.ugens.Decay.ar(
            ...     decay_time=decay_time,
            ...     source=source,
            ...     )
            >>> decay.decay_time
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('decay_time')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of Decay.

        ::

            >>> decay_time = 1.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> decay = supriya.ugens.Decay.ar(
            ...     decay_time=decay_time,
            ...     source=source,
            ...     )
            >>> decay.source
            In.ar()[0]

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
