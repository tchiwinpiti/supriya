from supriya.ugens.MultiOutUGen import MultiOutUGen


class PanB(MultiOutUGen):
    """
    A 3D ambisonic b-format panner.

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> pan_b = supriya.ugens.PanB.ar(
        ...     azimuth=0,
        ...     elevation=0,
        ...     gain=1,
        ...     source=source,
        ...     )
        >>> pan_b
        UGenArray({3})

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Spatialization UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'azimuth',
        'elevation',
        'gain',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        azimuth=0,
        elevation=0,
        gain=1,
        source=None,
        ):
        MultiOutUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            channel_count=3,
            azimuth=azimuth,
            elevation=elevation,
            gain=gain,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        azimuth=0,
        elevation=0,
        gain=1,
        source=None,
        ):
        """
        Constructs an audio-rate PanB.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_b = supriya.ugens.PanB.ar(
            ...     azimuth=0,
            ...     elevation=0,
            ...     gain=1,
            ...     source=source,
            ...     )
            >>> pan_b
            UGenArray({3})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            azimuth=azimuth,
            elevation=elevation,
            gain=gain,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        azimuth=0,
        elevation=0,
        gain=1,
        source=None,
        ):
        """
        Constructs a control-rate PanB.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_b = supriya.ugens.PanB.kr(
            ...     azimuth=0,
            ...     elevation=0,
            ...     gain=1,
            ...     source=source,
            ...     )
            >>> pan_b
            UGenArray({3})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            azimuth=azimuth,
            elevation=elevation,
            gain=gain,
            source=source,
            )
        return ugen

    # def newFromDesc(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def azimuth(self):
        """
        Gets `azimuth` input of PanB.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_b = supriya.ugens.PanB.ar(
            ...     azimuth=0,
            ...     elevation=0,
            ...     gain=1,
            ...     source=source,
            ...     )
            >>> pan_b[0].source.azimuth
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('azimuth')
        return self._inputs[index]

    @property
    def elevation(self):
        """
        Gets `elevation` input of PanB.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_b = supriya.ugens.PanB.ar(
            ...     azimuth=0,
            ...     elevation=0,
            ...     gain=1,
            ...     source=source,
            ...     )
            >>> pan_b[0].source.elevation
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('elevation')
        return self._inputs[index]

    @property
    def gain(self):
        """
        Gets `gain` input of PanB.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_b = supriya.ugens.PanB.ar(
            ...     azimuth=0,
            ...     elevation=0,
            ...     gain=1,
            ...     source=source,
            ...     )
            >>> pan_b[0].source.gain
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('gain')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of PanB.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> pan_b = supriya.ugens.PanB.ar(
            ...     azimuth=0,
            ...     elevation=0,
            ...     gain=1,
            ...     source=source,
            ...     )
            >>> pan_b[0].source.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
