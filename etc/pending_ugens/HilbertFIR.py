from supriya.ugens.UGen import UGen


class HilbertFIR(UGen):
    """

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> hilbert_fir = supriya.ugens.HilbertFIR.ar(
        ...     buffer_id=buffer_id,
        ...     source=source,
        ...     )
        >>> hilbert_fir
        HilbertFIR.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'buffer_id',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        buffer_id=None,
        source=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        buffer_id=None,
        source=None,
        ):
        """
        Constructs an audio-rate HilbertFIR.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> hilbert_fir = supriya.ugens.HilbertFIR.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> hilbert_fir
            HilbertFIR.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        """
        Gets `buffer_id` input of HilbertFIR.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> hilbert_fir = supriya.ugens.HilbertFIR.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> hilbert_fir.buffer_id

        Returns ugen input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of HilbertFIR.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> hilbert_fir = supriya.ugens.HilbertFIR.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> hilbert_fir.source
            OutputProxy(
                source=In(
                    bus=0.0,
                    calculation_rate=CalculationRate.AUDIO,
                    channel_count=1
                    ),
                output_index=0
                )

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
