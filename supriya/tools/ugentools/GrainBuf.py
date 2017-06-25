from supriya.tools.ugentools.MultiOutUGen import MultiOutUGen


class GrainBuf(MultiOutUGen):
    """

    ::

        >>> grain_buf = ugentools.GrainBuf.ar(
        ...     channel_count=1,
        ...     duration=1,
        ...     envelope_buffer_id=-1,
        ...     interpolate=2,
        ...     maximum_overlap=512,
        ...     pan=0,
        ...     position=0,
        ...     rate=1,
        ...     buffer_id=buffer_id,
        ...     trigger=0,
        ...     )
        >>> grain_buf
        GrainBuf.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'trigger',
        'duration',
        'buffer_id',
        'rate',
        'position',
        'interpolate',
        'pan',
        'envelope_buffer_id',
        'maximum_overlap',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        channel_count=1,
        duration=1,
        envelope_buffer_id=-1,
        interpolate=2,
        maximum_overlap=512,
        pan=0,
        position=0,
        rate=1,
        buffer_id=None,
        trigger=0,
        ):
        MultiOutUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            channel_count=channel_count,
            duration=duration,
            envelope_buffer_id=envelope_buffer_id,
            interpolate=interpolate,
            maximum_overlap=maximum_overlap,
            pan=pan,
            position=position,
            rate=rate,
            buffer_id=buffer_id,
            trigger=trigger,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        channel_count=1,
        duration=1,
        envelope_buffer_id=-1,
        interpolate=2,
        maximum_overlap=512,
        pan=0,
        position=0,
        rate=1,
        buffer_id=None,
        trigger=0,
        ):
        """
        Constructs an audio-rate GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf
            GrainBuf.ar()

        Returns ugen graph.
        """
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            channel_count=channel_count,
            duration=duration,
            envelope_buffer_id=envelope_buffer_id,
            interpolate=interpolate,
            maximum_overlap=maximum_overlap,
            pan=pan,
            position=position,
            rate=rate,
            buffer_id=buffer_id,
            trigger=trigger,
            )
        return ugen

    # def newFromDesc(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def duration(self):
        """
        Gets `duration` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.duration
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('duration')
        return self._inputs[index]

    @property
    def envelope_buffer_id(self):
        """
        Gets `envelope_buffer_id` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.envelope_buffer_id
            -1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('envelope_buffer_id')
        return self._inputs[index]

    @property
    def interpolate(self):
        """
        Gets `interpolate` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.interpolate
            2.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('interpolate')
        return self._inputs[index]

    @property
    def maximum_overlap(self):
        """
        Gets `maximum_overlap` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.maximum_overlap
            512.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('maximum_overlap')
        return self._inputs[index]

    @property
    def pan(self):
        """
        Gets `pan` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.pan
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('pan')
        return self._inputs[index]

    @property
    def position(self):
        """
        Gets `position` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.position
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('position')
        return self._inputs[index]

    @property
    def rate(self):
        """
        Gets `rate` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.rate
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('rate')
        return self._inputs[index]

    @property
    def buffer_id(self):
        """
        Gets `buffer_id` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.buffer_id

        Returns ugen input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def trigger(self):
        """
        Gets `trigger` input of GrainBuf.

        ::

            >>> grain_buf = ugentools.GrainBuf.ar(
            ...     channel_count=1,
            ...     duration=1,
            ...     envelope_buffer_id=-1,
            ...     interpolate=2,
            ...     maximum_overlap=512,
            ...     pan=0,
            ...     position=0,
            ...     rate=1,
            ...     buffer_id=buffer_id,
            ...     trigger=0,
            ...     )
            >>> grain_buf.trigger
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('trigger')
        return self._inputs[index]
