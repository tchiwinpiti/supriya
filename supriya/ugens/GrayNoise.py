from supriya.ugens.UGen import UGen


class GrayNoise(UGen):
    """
    A gray noise unit generator.

    ::

        >>> supriya.ugens.GrayNoise.ar()
        GrayNoise.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Noise UGens'

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        ):
        """
        Constructs an audio-rate gray noise unit generator.

        ::

            >>> supriya.ugens.GrayNoise.ar()
            GrayNoise.ar()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        ):
        """
        Constructs a control-rate gray noise unit generator.

        ::

            >>> supriya.ugens.GrayNoise.kr()
            GrayNoise.kr()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            )
        return ugen
