from supriya.ugens.UGen import UGen


class Wrap(UGen):
    """
    Wraps a signal outside given thresholds.

    ::

        >>> source = supriya.ugens.SinOsc.ar()
        >>> wrap = supriya.ugens.Wrap.ar(
        ...     maximum=0.9,
        ...     minimum=0.1,
        ...     source=source,
        ...     )
        >>> wrap
        Wrap.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Trigger Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'minimum',
        'maximum',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        maximum=1,
        minimum=0,
        source=0,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        maximum=1,
        minimum=0,
        source=None,
        ):
        """
        Constucts an audio-rate Wrap ugen.

        ::

            >>> source = supriya.ugens.SinOsc.ar(frequency=[440, 442])
            >>> wrap = supriya.ugens.Wrap.ar(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> wrap
            UGenArray({2})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            source=source,
            )
        return ugen

    @classmethod
    def ir(
        cls,
        maximum=1,
        minimum=0,
        source=None,
        ):
        """
        Constucts a scalar-rate Wrap ugen.

        ::

            >>> source = [supriya.ugens.Rand.ir(), supriya.ugens.Rand.ir()]
            >>> wrap = supriya.ugens.Wrap.ir(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> wrap
            UGenArray({2})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.SCALAR
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        maximum=1,
        minimum=0,
        source=None,
        ):
        """
        Constucts a control-rate Wrap ugen.

        ::

            >>> source = supriya.ugens.SinOsc.kr(frequency=[4, 2])
            >>> wrap = supriya.ugens.Wrap.kr(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> wrap
            UGenArray({2})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def maximum(self):
        """
        Gets `maximum` input of Wrap.

        ::

            >>> source = supriya.ugens.SinOsc.ar()
            >>> wrap = supriya.ugens.Wrap.ar(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> wrap.maximum
            0.9

        Returns input.
        """
        index = self._ordered_input_names.index('maximum')
        return self._inputs[index]

    @property
    def minimum(self):
        """
        Gets `minimum` input of Wrap.

        ::

            >>> source = supriya.ugens.SinOsc.ar()
            >>> wrap = supriya.ugens.Wrap.ar(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> wrap.minimum
            0.1

        Returns input.
        """
        index = self._ordered_input_names.index('minimum')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `minimum` input of Wrap.

        ::

            >>> source = supriya.ugens.SinOsc.ar()
            >>> wrap = supriya.ugens.Wrap.ar(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> wrap.source
            SinOsc.ar()[0]

        Returns input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
