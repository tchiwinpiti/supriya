from supriya.ugens.PureUGen import PureUGen


class DegreeToKey(PureUGen):
    """
    A signal-to-modal-pitch converter.`

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> degree_to_key = supriya.ugens.DegreeToKey.ar(
        ...     buffer_id=23,
        ...     octave=12,
        ...     source=source,
        ...     )
        >>> degree_to_key
        DegreeToKey.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'buffer_id',
        'source',
        'octave',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        buffer_id=None,
        octave=12,
        source=None,
        ):
        PureUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            octave=octave,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        buffer_id=None,
        octave=12,
        source=None,
        ):
        """
        Constructs an audio-rate DegreeToKey.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> degree_to_key = supriya.ugens.DegreeToKey.ar(
            ...     buffer_id=23,
            ...     octave=12,
            ...     source=source,
            ...     )
            >>> degree_to_key
            DegreeToKey.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            octave=octave,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        buffer_id=None,
        octave=12,
        source=None,
        ):
        """
        Constructs a control-rate DegreeToKey.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> degree_to_key = supriya.ugens.DegreeToKey.kr(
            ...     buffer_id=23,
            ...     octave=12,
            ...     source=source,
            ...     )
            >>> degree_to_key
            DegreeToKey.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            octave=octave,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        """
        Gets `buffer_id` input of DegreeToKey.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> degree_to_key = supriya.ugens.DegreeToKey.ar(
            ...     buffer_id=23,
            ...     octave=12,
            ...     source=source,
            ...     )
            >>> degree_to_key.buffer_id
            23

        Returns ugen input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return int(self._inputs[index])

    @property
    def octave(self):
        """
        Gets `octave` input of DegreeToKey.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> degree_to_key = supriya.ugens.DegreeToKey.ar(
            ...     buffer_id=23,
            ...     octave=12,
            ...     source=source,
            ...     )
            >>> degree_to_key.octave
            12.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('octave')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of DegreeToKey.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> degree_to_key = supriya.ugens.DegreeToKey.ar(
            ...     buffer_id=23,
            ...     octave=12,
            ...     source=source,
            ...     )
            >>> degree_to_key.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
