from supriya.ugens.UGen import UGen


class LFDClipNoise(UGen):
    """
    A clipped noise generator.

    ::

        >>> supriya.ugens.LFDClipNoise.ar()
        LFDClipNoise.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Noise UGens'

    __slots__ = ()

    _ordered_input_names = (
        'frequency',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        frequency=500,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            frequency=frequency,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        frequency=500,
        ):
        """
        Constructs an audio-rate dynamic clipped noise generator.

        ::

            >>> supriya.ugens.LFDClipNoise.ar(
            ...     frequency=10,
            ...     )
            LFDClipNoise.ar()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            frequency=frequency,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        frequency=500,
        ):
        """
        Constructs a control-rate dynamic clipped noise generator.

        ::

            >>> supriya.ugens.LFDClipNoise.kr(
            ...     frequency=10,
            ...     )
            LFDClipNoise.kr()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            frequency=frequency,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def frequency(self):
        """
        Gets `frequency` input of LFDClipNoise.

        ::

            >>> frequency = 0.5
            >>> lf_noise_0 = supriya.ugens.LFDClipNoise.ar(
            ...     frequency=frequency,
            ...     )
            >>> lf_noise_0.frequency
            0.5

        Returns input.
        """
        index = self._ordered_input_names.index('frequency')
        return self._inputs[index]
