from supriya.ugens.BufDelayN import BufDelayN


class BufDelayC(BufDelayN):
    """
    A buffer-based cubic-interpolating delay line unit generator.

    ::

        >>> buffer_id = 0
        >>> source = supriya.ugens.In.ar(bus=0)
        >>> supriya.ugens.BufDelayC.ar(
        ...     buffer_id=buffer_id,
        ...     source=source,
        ...     )
        BufDelayC.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Delay UGens'

    __slots__ = ()

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        buffer_id=None,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        ):
        """
        Constructs an audio-rate buffer-based cubic-interpolating delay line.

        ::

            >>> buffer_id = 0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> supriya.ugens.BufDelayC.ar(
            ...     buffer_id=buffer_id,
            ...     delay_time=0.5,
            ...     maximum_delay_time=1.0,
            ...     source=source,
            ...     )
            BufDelayC.ar()

        Returns unit generator graph.
        """
        return super(BufDelayC, cls).ar(
            buffer_id=buffer_id,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )

    @classmethod
    def kr(
        cls,
        buffer_id=None,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        ):
        """
        Constructs a control-rate buffer-based cubic-interpolating delay line.

        ::

            >>> buffer_id = 0
            >>> source = supriya.ugens.In.kr(bus=0)
            >>> supriya.ugens.BufDelayC.kr(
            ...     buffer_id=buffer_id,
            ...     delay_time=0.5,
            ...     maximum_delay_time=1.0,
            ...     source=source,
            ...     )
            BufDelayC.ar()

        Returns unit generator graph.
        """
        return super(BufDelayC, cls).kr(
            buffer_id=buffer_id,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        """
        Gets `buffer_id` input of BufDelayC.

        ::

            >>> buffer_id = 23
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_delay_c = supriya.ugens.BufDelayC.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> buf_delay_c.buffer_id
            23.0

        Returns input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def delay_time(self):
        """
        Gets `delay_time` input of BufDelayC.

        ::

            >>> buffer_id = 23
            >>> delay_time = 1.5
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_delay_c = supriya.ugens.BufDelayC.ar(
            ...     buffer_id=buffer_id,
            ...     delay_time=delay_time,
            ...     source=source,
            ...     )
            >>> buf_delay_c.delay_time
            1.5

        Returns input.
        """
        index = self._ordered_input_names.index('delay_time')
        return self._inputs[index]

    @property
    def maximum_delay_time(self):
        """
        Gets `maximum_delay_time` input of BufDelayC.

        ::

            >>> buffer_id = 23
            >>> maximum_delay_time = 2.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_delay_c = supriya.ugens.BufDelayC.ar(
            ...     buffer_id=buffer_id,
            ...     maximum_delay_time=maximum_delay_time,
            ...     source=source,
            ...     )
            >>> buf_delay_c.maximum_delay_time
            2.0

        Returns input.
        """
        index = self._ordered_input_names.index('maximum_delay_time')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of BufDelayC.

        ::

            >>> buffer_id = 23
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_delay_c = supriya.ugens.BufDelayC.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> buf_delay_c.source
            In.ar()[0]

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
