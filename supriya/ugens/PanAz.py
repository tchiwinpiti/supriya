from supriya.ugens.MultiOutUGen import MultiOutUGen


class PanAz(MultiOutUGen):
    """
    A multi-channel equal-power panner.

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> pan_az = supriya.ugens.PanAz.ar(
        ...     channel_count=8,
        ...     amplitude=1,
        ...     orientation=0.5,
        ...     position=0,
        ...     source=source,
        ...     width=2,
        ...     )
        >>> pan_az
        UGenArray({8})

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Spatialization UGens'

    __slots__ = ()

    _ordered_input_names = (
        'channel_count',
        'source',
        'position',
        'amplitude',
        'width',
        'orientation',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        channel_count=8,
        amplitude=1,
        orientation=0.5,
        position=0,
        source=None,
        width=2,
        ):
        MultiOutUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            channel_count=channel_count,
            amplitude=amplitude,
            orientation=orientation,
            position=position,
            source=source,
            width=width,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        channel_count=None,
        amplitude=1,
        orientation=0.5,
        position=0,
        source=None,
        width=2,
        ):
        """
        Constructs an audio-rate PanAz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_az = supriya.ugens.PanAz.ar(
            ...     channel_count=8,
            ...     amplitude=1,
            ...     orientation=0.5,
            ...     position=0,
            ...     source=source,
            ...     width=2,
            ...     )
            >>> pan_az
            UGenArray({8})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            channel_count=channel_count,
            amplitude=amplitude,
            orientation=orientation,
            position=position,
            source=source,
            width=width,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        channel_count=None,
        amplitude=1,
        orientation=0.5,
        position=0,
        source=None,
        width=2,
        ):
        """
        Constructs a control-rate PanAz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_az = supriya.ugens.PanAz.kr(
            ...     channel_count=8,
            ...     amplitude=1,
            ...     orientation=0.5,
            ...     position=0,
            ...     source=source,
            ...     width=2,
            ...     )
            >>> pan_az
            UGenArray({8})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            channel_count=channel_count,
            amplitude=amplitude,
            orientation=orientation,
            position=position,
            source=source,
            width=width,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def channel_count(self):
        """
        Gets `channel_count` input of PanAz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_az = supriya.ugens.PanAz.ar(
            ...     channel_count=8,
            ...     amplitude=1,
            ...     orientation=0.5,
            ...     position=0,
            ...     source=source,
            ...     width=2,
            ...     )
            >>> pan_az[0].source.channel_count
            8

        Returns ugen input.
        """
        index = self._ordered_input_names.index('channel_count')
        return int(self._inputs[index])

    @property
    def amplitude(self):
        """
        Gets `amplitude` input of PanAz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_az = supriya.ugens.PanAz.ar(
            ...     channel_count=8,
            ...     amplitude=1,
            ...     orientation=0.5,
            ...     position=0,
            ...     source=source,
            ...     width=2,
            ...     )
            >>> pan_az[0].source.amplitude
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('amplitude')
        return self._inputs[index]

    @property
    def orientation(self):
        """
        Gets `orientation` input of PanAz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_az = supriya.ugens.PanAz.ar(
            ...     channel_count=8,
            ...     amplitude=1,
            ...     orientation=0.5,
            ...     position=0,
            ...     source=source,
            ...     width=2,
            ...     )
            >>> pan_az[0].source.orientation
            0.5

        Returns ugen input.
        """
        index = self._ordered_input_names.index('orientation')
        return self._inputs[index]

    @property
    def position(self):
        """
        Gets `position` input of PanAz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_az = supriya.ugens.PanAz.ar(
            ...     channel_count=8,
            ...     amplitude=1,
            ...     orientation=0.5,
            ...     position=0,
            ...     source=source,
            ...     width=2,
            ...     )
            >>> pan_az[0].source.position
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('position')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of PanAz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_az = supriya.ugens.PanAz.ar(
            ...     channel_count=8,
            ...     amplitude=1,
            ...     orientation=0.5,
            ...     position=0,
            ...     source=source,
            ...     width=2,
            ...     )
            >>> pan_az[0].source.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]

    @property
    def width(self):
        """
        Gets `width` input of PanAz.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_az = supriya.ugens.PanAz.ar(
            ...     channel_count=8,
            ...     amplitude=1,
            ...     orientation=0.5,
            ...     position=0,
            ...     source=source,
            ...     width=2,
            ...     )
            >>> pan_az[0].source.width
            2.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('width')
        return self._inputs[index]
