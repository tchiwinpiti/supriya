from supriya.ugens.UGen import UGen


class Amplitude(UGen):
    """
    An amplitude follower.

    ::

        >>> source = supriya.ugens.In.ar(0)
        >>> amplitude = supriya.ugens.Amplitude.kr(
        ...     attack_time=0.01,
        ...     release_time=0.01,
        ...     source=source,
        ...     )
        >>> amplitude
        Amplitude.kr()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Dynamics UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'attack_time',
        'release_time',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        attack_time=0.01,
        release_time=0.01,
        source=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            attack_time=attack_time,
            release_time=release_time,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        attack_time=0.01,
        release_time=0.01,
        source=None,
        ):
        """
        Constructs an audio-rate Amplitude.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> amplitude = supriya.ugens.Amplitude.ar(
            ...     attack_time=0.01,
            ...     release_time=0.01,
            ...     source=source,
            ...     )
            >>> amplitude
            Amplitude.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            attack_time=attack_time,
            release_time=release_time,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        attack_time=0.01,
        release_time=0.01,
        source=None,
        ):
        """
        Constructs a control-rate Amplitude.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> amplitude = supriya.ugens.Amplitude.kr(
            ...     attack_time=0.01,
            ...     release_time=0.01,
            ...     source=source,
            ...     )
            >>> amplitude
            Amplitude.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            attack_time=attack_time,
            release_time=release_time,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def attack_time(self):
        """
        Gets `attack_time` input of Amplitude.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> amplitude = supriya.ugens.Amplitude.kr(
            ...     attack_time=0.01,
            ...     release_time=0.01,
            ...     source=source,
            ...     )
            >>> amplitude.attack_time
            0.01

        Returns ugen input.
        """
        index = self._ordered_input_names.index('attack_time')
        return self._inputs[index]

    @property
    def release_time(self):
        """
        Gets `release_time` input of Amplitude.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> amplitude = supriya.ugens.Amplitude.ar(
            ...     attack_time=0.01,
            ...     release_time=0.01,
            ...     source=source,
            ...     )
            >>> amplitude.release_time
            0.01

        Returns ugen input.
        """
        index = self._ordered_input_names.index('release_time')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of Amplitude.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> amplitude = supriya.ugens.Amplitude.ar(
            ...     attack_time=0.01,
            ...     release_time=0.01,
            ...     source=source,
            ...     )
            >>> amplitude.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
