from supriya.ugens.BufCombN import BufCombN


class BufCombL(BufCombN):
    """
    A buffer-based linear-interpolating comb delay line unit generator.

    ::

        >>> buffer_id = 0
        >>> source = supriya.ugens.In.ar(bus=0)
        >>> supriya.ugens.BufCombL.ar(
        ...     buffer_id=buffer_id,
        ...     source=source,
        ...     )
        BufCombL.ar()

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
        Constructs an audio-rate buffer-based linear-interpolating comb delay
        line.

        ::

            >>> buffer_id = 0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> supriya.ugens.BufCombL.ar(
            ...     buffer_id=buffer_id,
            ...     decay_time=1.0,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     )
            BufCombL.ar()

        Returns unit generator graph.
        """
        return super(BufCombL, cls).ar(
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
        Constructs a control-rate buffer-based linear-interpolating comb delay
        line.

        ::

            >>> buffer_id = 0
            >>> source = supriya.ugens.In.kr(bus=0)
            >>> supriya.ugens.BufCombL.kr(
            ...     buffer_id=buffer_id,
            ...     decay_time=1.0,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     )
            BufCombL.ar()

        Returns unit generator graph.
        """
        return super(BufCombL, cls).kr(
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
        Gets `buffer_id` input of BufCombL.

        ::

            >>> buffer_id = 23
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_comb_l = supriya.ugens.BufCombL.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> buf_comb_l.buffer_id
            23.0

        Returns input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def decay_time(self):
        """
        Gets `decay_time` input of BufCombL.

        ::

            >>> buffer_id = 23
            >>> decay_time = 1.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_comb_l = supriya.ugens.BufCombL.ar(
            ...     buffer_id=buffer_id,
            ...     decay_time=decay_time,
            ...     source=source,
            ...     )
            >>> buf_comb_l.decay_time
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('decay_time')
        return self._inputs[index]

    @property
    def delay_time(self):
        """
        Gets `delay_time` input of BufCombL.

        ::

            >>> buffer_id = 23
            >>> delay_time = 1.5
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_comb_l = supriya.ugens.BufCombL.ar(
            ...     buffer_id=buffer_id,
            ...     delay_time=delay_time,
            ...     source=source,
            ...     )
            >>> buf_comb_l.delay_time
            1.5

        Returns input.
        """
        index = self._ordered_input_names.index('delay_time')
        return self._inputs[index]

    @property
    def maximum_delay_time(self):
        """
        Gets `maximum_delay_time` input of BufCombL.

        ::

            >>> buffer_id = 23
            >>> maximum_delay_time = 2.0
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_comb_l = supriya.ugens.BufCombL.ar(
            ...     buffer_id=buffer_id,
            ...     maximum_delay_time=maximum_delay_time,
            ...     source=source,
            ...     )
            >>> buf_comb_l.maximum_delay_time
            2.0

        Returns input.
        """
        index = self._ordered_input_names.index('maximum_delay_time')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of BufCombL.

        ::

            >>> buffer_id = 23
            >>> source = supriya.ugens.In.ar(bus=0)
            >>> buf_comb_l = supriya.ugens.BufCombL.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> buf_comb_l.source
            In.ar()[0]

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
