from supriya.ugens.UGen import UGen


class PeakFollower(UGen):
    """
    Tracks peak signal amplitude.

    ::

        >>> source = supriya.ugens.In.ar(0)
        >>> peak_follower = supriya.ugens.PeakFollower.ar(
        ...     decay=0.999,
        ...     source=source,
        ...     )
        >>> peak_follower
        PeakFollower.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Trigger Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'decay',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        decay=0.999,
        source=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            decay=decay,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        decay=0.999,
        source=None,
        ):
        """
        Constructs an audio-rate PeakFollower.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> peak_follower = supriya.ugens.PeakFollower.ar(
            ...     decay=0.999,
            ...     source=source,
            ...     )
            >>> peak_follower
            PeakFollower.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            decay=decay,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        decay=0.999,
        source=None,
        ):
        """
        Constructs a control-rate PeakFollower.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> peak_follower = supriya.ugens.PeakFollower.kr(
            ...     decay=0.999,
            ...     source=source,
            ...     )
            >>> peak_follower
            PeakFollower.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            decay=decay,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def decay(self):
        """
        Gets `decay` input of PeakFollower.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> peak_follower = supriya.ugens.PeakFollower.ar(
            ...     decay=0.999,
            ...     source=source,
            ...     )
            >>> peak_follower.decay
            0.999

        Returns ugen input.
        """
        index = self._ordered_input_names.index('decay')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of PeakFollower.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> peak_follower = supriya.ugens.PeakFollower.ar(
            ...     decay=0.999,
            ...     source=source,
            ...     )
            >>> peak_follower.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
