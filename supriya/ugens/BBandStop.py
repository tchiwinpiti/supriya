from supriya.ugens.BEQSuite import BEQSuite


class BBandStop(BEQSuite):
    """
    A band-stop filter.

    ::

        >>> source = supriya.ugens.In.ar(0)
        >>> bband_stop = supriya.ugens.BBandStop.ar(
        ...     bandwidth=1,
        ...     frequency=1200,
        ...     source=source,
        ...     )
        >>> bband_stop
        BBandStop.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Filter UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'frequency',
        'bandwidth',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        bandwidth=1,
        frequency=1200,
        source=None,
        ):
        BEQSuite.__init__(
            self,
            calculation_rate=calculation_rate,
            bandwidth=bandwidth,
            frequency=frequency,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        bandwidth=1,
        frequency=1200,
        source=None,
        ):
        """
        Constructs an audio-rate BBandStop.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> bband_stop = supriya.ugens.BBandStop.ar(
            ...     bandwidth=1,
            ...     frequency=1200,
            ...     source=source,
            ...     )
            >>> bband_stop
            BBandStop.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            bandwidth=bandwidth,
            frequency=frequency,
            source=source,
            )
        return ugen

    # def coeffs(): ...

    # def magResponse(): ...

    # def magResponse2(): ...

    # def magResponse5(): ...

    # def magResponseN(): ...

    # def sc(): ...

    # def scopeResponse(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def bandwidth(self):
        """
        Gets `bandwidth` input of BBandStop.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> bband_stop = supriya.ugens.BBandStop.ar(
            ...     bandwidth=1,
            ...     frequency=1200,
            ...     source=source,
            ...     )
            >>> bband_stop.bandwidth
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('bandwidth')
        return self._inputs[index]

    @property
    def frequency(self):
        """
        Gets `frequency` input of BBandStop.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> bband_stop = supriya.ugens.BBandStop.ar(
            ...     bandwidth=1,
            ...     frequency=1200,
            ...     source=source,
            ...     )
            >>> bband_stop.frequency
            1200.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('frequency')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of BBandStop.

        ::

            >>> source = supriya.ugens.In.ar(0)
            >>> bband_stop = supriya.ugens.BBandStop.ar(
            ...     bandwidth=1,
            ...     frequency=1200,
            ...     source=source,
            ...     )
            >>> bband_stop.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
