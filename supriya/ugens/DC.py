from supriya.ugens.PureUGen import PureUGen


class DC(PureUGen):
    """
    A DC unit generator.

    ::

        >>> supriya.ugens.DC.ar(
        ...     source=0,
        ...     )
        DC.ar()

    ::

        >>> supriya.ugens.DC.ar(
        ...     source=(1, 2, 3),
        ...     )
        UGenArray({3})

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        source=None,
        ):
        PureUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        source=None,
        ):
        """
        Constructs an audio-rate DC generator.

        ::

            >>> supriya.ugens.DC.ar(
            ...     source=0,
            ...     )
            DC.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        source=None,
        ):
        """
        Constructs a control-rate DC generator.

        ::

            >>> supriya.ugens.DC.kr(
            ...     source=0,
            ...     )
            DC.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def source(self):
        """
        Gets `source` input of DC.

        ::

            >>> source = 0.5
            >>> dc = supriya.ugens.DC.ar(
            ...     source=source,
            ...     )
            >>> dc.source
            0.5

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
