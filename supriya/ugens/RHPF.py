from supriya.ugens.Filter import Filter


class RHPF(Filter):
    """
    A resonant highpass filter unit generator.

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> supriya.ugens.RLPF.ar(source=source)
        RLPF.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Filter UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'frequency',
        'reciprocal_of_q',
        )

    ### PUBLIC METHODS ###

    def __init__(
        self,
        frequency=440,
        calculation_rate=None,
        reciprocal_of_q=1.0,
        source=None,
        ):
        Filter.__init__(
            self,
            frequency=frequency,
            calculation_rate=calculation_rate,
            reciprocal_of_q=reciprocal_of_q,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        frequency=440,
        reciprocal_of_q=1.0,
        source=None,
        ):
        """
        Constructs an audio-rate resonant highpass filter.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> supriya.ugens.RLPF.ar(
            ...     frequency=440,
            ...     reciprocal_of_q=1.0,
            ...     source=source,
            ...     )
            RLPF.ar()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            frequency=frequency,
            calculation_rate=calculation_rate,
            reciprocal_of_q=reciprocal_of_q,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        frequency=440,
        reciprocal_of_q=1.0,
        source=None,
        ):
        """
        Constructs a control-rate resonant highpass filter.

        ::

            >>> source = supriya.ugens.In.kr(bus=0)
            >>> supriya.ugens.RLPF.kr(
            ...     frequency=440,
            ...     reciprocal_of_q=1.0,
            ...     source=source,
            ...     )
            RLPF.kr()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            frequency=frequency,
            calculation_rate=calculation_rate,
            reciprocal_of_q=reciprocal_of_q,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def frequency(self):
        """
        Gets `frequency` input of RHPF.

        ::

            >>> frequency = 442
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> rhpf = supriya.ugens.RHPF.ar(
            ...     frequency=frequency,
            ...     source=source,
            ...     )
            >>> rhpf.frequency
            442.0

        Returns input.
        """
        index = self._ordered_input_names.index('frequency')
        return self._inputs[index]

    @property
    def reciprocal_of_q(self):
        """
        Gets `reciprocal_of_q` input of RHPF.

        ::

            >>> reciprocal_of_q = 2.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> rhpf = supriya.ugens.RHPF.ar(
            ...     reciprocal_of_q=reciprocal_of_q,
            ...     source=source,
            ...     )
            >>> rhpf.reciprocal_of_q
            2.0

        Returns input.
        """
        index = self._ordered_input_names.index('reciprocal_of_q')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of RHPF.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> rhpf = supriya.ugens.RHPF.ar(
            ...     source=source,
            ...     )
            >>> rhpf.source
            In.ar()[0]

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
