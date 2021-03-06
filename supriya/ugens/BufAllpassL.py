from supriya.ugens.BufAllpassN import BufAllpassN


class BufAllpassL(BufAllpassN):
    """
    A buffer-based linear-interpolating allpass delay line unit generator.

    ::

        >>> buffer_id = 0
        >>> source = supriya.ugens.In.ar(bus=0)
        >>> supriya.ugens.BufAllpassL.ar(
        ...     buffer_id=buffer_id,
        ...     source=source,
        ...     )
        BufAllpassL.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Delay UGens'

    __slots__ = ()

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
        Constructs an audio-rate buffer-based linear-interpolating allpass
        delay line.

        ::

            >>> buffer_id = 0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> supriya.ugens.BufAllpassL.ar(
            ...     buffer_id=buffer_id,
            ...     decay_time=1.0,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     )
            BufAllpassL.ar()

        Returns unit generator graph.
        """
        return super(BufAllpassL, cls).ar(
            buffer_id=buffer_id,
            decay_time=decay_time,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )

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
        Constructs a control-rate buffer-based linear-interpolating allpass
        delay line.

        ::

            >>> buffer_id = 0
            >>> source = supriya.ugens.In.kr(bus=0)
            >>> supriya.ugens.BufAllpassL.kr(
            ...     buffer_id=buffer_id,
            ...     decay_time=1.0,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     )
            BufAllpassL.ar()

        Returns unit generator graph.
        """
        return super(BufAllpassL, cls).kr(
            buffer_id=buffer_id,
            decay_time=decay_time,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        """
        Gets `buffer_id` input of BufAllpassL.

        ::

            >>> buffer_id = 23
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_l = supriya.ugens.BufAllpassL.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> buf_allpass_l.buffer_id
            23.0

        Returns input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def decay_time(self):
        """
        Gets `decay_time` input of BufAllpassL.

        ::

            >>> buffer_id = 23
            >>> decay_time = 1.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_l = supriya.ugens.BufAllpassL.ar(
            ...     buffer_id=buffer_id,
            ...     decay_time=decay_time,
            ...     source=source,
            ...     )
            >>> buf_allpass_l.decay_time
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('decay_time')
        return self._inputs[index]

    @property
    def delay_time(self):
        """
        Gets `delay_time` input of BufAllpassL.

        ::

            >>> buffer_id = 23
            >>> delay_time = 1.5
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_l = supriya.ugens.BufAllpassL.ar(
            ...     buffer_id=buffer_id,
            ...     delay_time=delay_time,
            ...     source=source,
            ...     )
            >>> buf_allpass_l.delay_time
            1.5

        Returns input.
        """
        index = self._ordered_input_names.index('delay_time')
        return self._inputs[index]

    @property
    def maximum_delay_time(self):
        """
        Gets `maximum_delay_time` input of BufAllpassL.

        ::

            >>> buffer_id = 23
            >>> maximum_delay_time = 2.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_l = supriya.ugens.BufAllpassL.ar(
            ...     buffer_id=buffer_id,
            ...     maximum_delay_time=maximum_delay_time,
            ...     source=source,
            ...     )
            >>> buf_allpass_l.maximum_delay_time
            2.0

        Returns input.
        """
        index = self._ordered_input_names.index('maximum_delay_time')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of BufAllpassL.

        ::

            >>> buffer_id = 23
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_allpass_l = supriya.ugens.BufAllpassL.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> buf_allpass_l.source
            In.ar()[0]

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
