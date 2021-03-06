from supriya.ugens.UGen import UGen


class Convolution2L(UGen):
    """
    Strict convolution with fixed kernel which can be updated using a trigger signal.

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> kernel = supriya.ugens.Mix.new(
        ...     supriya.ugens.LFSaw.ar(frequency=[300, 500, 800, 1000]) *
        ...     supriya.ugens.MouseX.kr(minimum=1, maximum=2),
        ...     )
        >>> convolution_2_l = supriya.ugens.Convolution2L.ar(
        ...     crossfade=1,
        ...     framesize=2048,
        ...     kernel=kernel,
        ...     source=source,
        ...     trigger=0,
        ...     )
        >>> convolution_2_l
        Convolution2L.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'kernel',
        'trigger',
        'framesize',
        'crossfade',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        crossfade=1,
        framesize=2048,
        kernel=None,
        source=None,
        trigger=0,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            crossfade=crossfade,
            framesize=framesize,
            kernel=kernel,
            source=source,
            trigger=trigger,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        crossfade=1,
        framesize=2048,
        kernel=None,
        source=None,
        trigger=0,
        ):
        """
        Constructs an audio-rate Convolution2L.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> kernel = supriya.ugens.Mix.new(
            ...     supriya.ugens.LFSaw.ar(frequency=[300, 500, 800, 1000]) *
            ...     supriya.ugens.MouseX.kr(minimum=1, maximum=2),
            ...     )
            >>> convolution_2_l = supriya.ugens.Convolution2L.ar(
            ...     crossfade=1,
            ...     framesize=2048,
            ...     kernel=kernel,
            ...     source=source,
            ...     trigger=0,
            ...     )
            >>> convolution_2_l
            Convolution2L.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            crossfade=crossfade,
            framesize=framesize,
            kernel=kernel,
            source=source,
            trigger=trigger,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def crossfade(self):
        """
        Gets `crossfade` input of Convolution2L.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> kernel = supriya.ugens.Mix.new(
            ...     supriya.ugens.LFSaw.ar(frequency=[300, 500, 800, 1000]) *
            ...     supriya.ugens.MouseX.kr(minimum=1, maximum=2),
            ...     )
            >>> convolution_2_l = supriya.ugens.Convolution2L.ar(
            ...     crossfade=1,
            ...     framesize=2048,
            ...     kernel=kernel,
            ...     source=source,
            ...     trigger=0,
            ...     )
            >>> convolution_2_l.crossfade
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('crossfade')
        return self._inputs[index]

    @property
    def framesize(self):
        """
        Gets `framesize` input of Convolution2L.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> kernel = supriya.ugens.Mix.new(
            ...     supriya.ugens.LFSaw.ar(frequency=[300, 500, 800, 1000]) *
            ...     supriya.ugens.MouseX.kr(minimum=1, maximum=2),
            ...     )
            >>> convolution_2_l = supriya.ugens.Convolution2L.ar(
            ...     crossfade=1,
            ...     framesize=2048,
            ...     kernel=kernel,
            ...     source=source,
            ...     trigger=0,
            ...     )
            >>> convolution_2_l.framesize
            2048.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('framesize')
        return self._inputs[index]

    @property
    def kernel(self):
        """
        Gets `kernel` input of Convolution2L.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> kernel = supriya.ugens.Mix.new(
            ...     supriya.ugens.LFSaw.ar(frequency=[300, 500, 800, 1000]) *
            ...     supriya.ugens.MouseX.kr(minimum=1, maximum=2),
            ...     )
            >>> convolution_2_l = supriya.ugens.Convolution2L.ar(
            ...     crossfade=1,
            ...     framesize=2048,
            ...     kernel=kernel,
            ...     source=source,
            ...     trigger=0,
            ...     )
            >>> convolution_2_l.kernel
            Sum4.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('kernel')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of Convolution2L.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> kernel = supriya.ugens.Mix.new(
            ...     supriya.ugens.LFSaw.ar(frequency=[300, 500, 800, 1000]) *
            ...     supriya.ugens.MouseX.kr(minimum=1, maximum=2),
            ...     )
            >>> convolution_2_l = supriya.ugens.Convolution2L.ar(
            ...     crossfade=1,
            ...     framesize=2048,
            ...     kernel=kernel,
            ...     source=source,
            ...     trigger=0,
            ...     )
            >>> convolution_2_l.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]

    @property
    def trigger(self):
        """
        Gets `trigger` input of Convolution2L.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> kernel = supriya.ugens.Mix.new(
            ...     supriya.ugens.LFSaw.ar(frequency=[300, 500, 800, 1000]) *
            ...     supriya.ugens.MouseX.kr(minimum=1, maximum=2),
            ...     )
            >>> convolution_2_l = supriya.ugens.Convolution2L.ar(
            ...     crossfade=1,
            ...     framesize=2048,
            ...     kernel=kernel,
            ...     source=source,
            ...     trigger=0,
            ...     )
            >>> convolution_2_l.trigger
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('trigger')
        return self._inputs[index]
