from supriya.ugens.UGen import UGen


class Trig(UGen):
    """
    A timed trigger.

    ::

        >>> source = supriya.ugens.Dust.kr(1)
        >>> trig = supriya.ugens.Trig.ar(
        ...     duration=0.1,
        ...     source=source,
        ...     )
        >>> trig
        Trig.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Trigger Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'duration',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        duration=0.1,
        source=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            duration=duration,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        duration=0.1,
        source=None,
        ):
        """
        Constructs an audio-rate Trig.

        ::

            >>> source = supriya.ugens.Dust.kr(1)
            >>> trig = supriya.ugens.Trig.ar(
            ...     duration=0.1,
            ...     source=source,
            ...     )
            >>> trig
            Trig.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            duration=duration,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        duration=0.1,
        source=None,
        ):
        """
        Constructs a control-rate Trig.

        ::

            >>> source = supriya.ugens.Dust.kr(1)
            >>> trig = supriya.ugens.Trig.kr(
            ...     duration=0.1,
            ...     source=source,
            ...     )
            >>> trig
            Trig.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            duration=duration,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def duration(self):
        """
        Gets `duration` input of Trig.

        ::

            >>> source = supriya.ugens.Dust.kr(1)
            >>> trig = supriya.ugens.Trig.ar(
            ...     duration=0.1,
            ...     source=source,
            ...     )
            >>> trig.duration
            0.1

        Returns ugen input.
        """
        index = self._ordered_input_names.index('duration')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of Trig.

        ::

            >>> source = supriya.ugens.Dust.kr(1)
            >>> trig = supriya.ugens.Trig.ar(
            ...     duration=0.1,
            ...     source=source,
            ...     )
            >>> trig.source
            Dust.kr()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
