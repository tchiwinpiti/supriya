from supriya.ugens.PureUGen import PureUGen


class BufAllpassN(PureUGen):
    """
    A buffer-based non-interpolating allpass delay line unit generator.

    ::

        >>> buffer_id = 0
        >>> source = supriya.ugens.In.ar(bus=0)
        >>> supriya.ugens.BufAllpassN.ar(
        ...     buffer_id=buffer_id,
        ...     source=source,
        ...     )
        BufAllpassN.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Delay UGens'

    __slots__ = ()

    _ordered_input_names = (
        'buffer_id',
        'source',
        'maximum_delay_time',
        'delay_time',
        'decay_time',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        buffer_id=None,
        calculation_rate=None,
        decay_time=1.0,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        ):
        PureUGen.__init__(
            self,
            buffer_id=int(buffer_id),
            calculation_rate=calculation_rate,
            decay_time=decay_time,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        buffer_id=None,
        decay_time=1.0,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        ):
        """
        Constructs an audio-rate buffer-based non-interpolating allpass delay
        line.

        ::

            >>> buffer_id = 0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> supriya.ugens.BufAllpassN.ar(
            ...     buffer_id=buffer_id,
            ...     decay_time=1.0,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     )
            BufAllpassN.ar()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        source = cls._as_audio_rate_input(source)
        ugen = cls._new_expanded(
            buffer_id=buffer_id,
            calculation_rate=calculation_rate,
            decay_time=decay_time,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        buffer_id=None,
        decay_time=1.0,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        ):
        """
        Constructs a control-rate buffer-based non-interpolating allpass delay
        line.

        ::

            >>> buffer_id = 0
            >>> source = supriya.ugens.In.kr(bus=0)
            >>> supriya.ugens.BufAllpassN.kr(
            ...     buffer_id=buffer_id,
            ...     decay_time=1.0,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     )
            BufAllpassN.ar()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            buffer_id=buffer_id,
            calculation_rate=calculation_rate,
            decay_time=decay_time,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        """
        Gets `buffer_id` input of BufAllpassN.

        ::

            >>> buffer_id = 23
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_n = supriya.ugens.BufAllpassN.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> buf_allpass_n.buffer_id
            23.0

        Returns input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def decay_time(self):
        """
        Gets `decay_time` input of BufAllpassN.

        ::

            >>> buffer_id = 23
            >>> decay_time = 1.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_n = supriya.ugens.BufAllpassN.ar(
            ...     buffer_id=buffer_id,
            ...     decay_time=decay_time,
            ...     source=source,
            ...     )
            >>> buf_allpass_n.decay_time
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('decay_time')
        return self._inputs[index]

    @property
    def delay_time(self):
        """
        Gets `delay_time` input of BufAllpassN.

        ::

            >>> buffer_id = 23
            >>> delay_time = 1.5
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_n = supriya.ugens.BufAllpassN.ar(
            ...     buffer_id=buffer_id,
            ...     delay_time=delay_time,
            ...     source=source,
            ...     )
            >>> buf_allpass_n.delay_time
            1.5

        Returns input.
        """
        index = self._ordered_input_names.index('delay_time')
        return self._inputs[index]

    @property
    def maximum_delay_time(self):
        """
        Gets `maximum_delay_time` input of BufAllpassN.

        ::

            >>> buffer_id = 23
            >>> maximum_delay_time = 2.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_n = supriya.ugens.BufAllpassN.ar(
            ...     buffer_id=buffer_id,
            ...     maximum_delay_time=maximum_delay_time,
            ...     source=source,
            ...     )
            >>> buf_allpass_n.maximum_delay_time
            2.0

        Returns input.
        """
        index = self._ordered_input_names.index('maximum_delay_time')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of BufAllpassN.

        ::

            >>> buffer_id = 23
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_n = supriya.ugens.BufAllpassN.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> buf_allpass_n.source
            In.ar()[0]

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
