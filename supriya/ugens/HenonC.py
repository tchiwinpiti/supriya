from supriya.ugens.UGen import UGen


class HenonC(UGen):
    """
    A cubic-interpolating henon map chaotic generator.

    ::

        >>> henon_c = supriya.ugens.HenonC.ar(
        ...     a=1.4,
        ...     b=0.3,
        ...     frequency=22050,
        ...     x_0=0,
        ...     x_1=0,
        ...     )
        >>> henon_c
        HenonC.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Chaos UGens'

    __slots__ = ()

    _ordered_input_names = (
        'frequency',
        'a',
        'b',
        'x_0',
        'x_1',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        a=1.4,
        b=0.3,
        frequency=22050,
        x_0=0,
        x_1=0,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            a=a,
            b=b,
            frequency=frequency,
            x_0=x_0,
            x_1=x_1,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        a=1.4,
        b=0.3,
        frequency=22050,
        x_0=0,
        x_1=0,
        ):
        """
        Constructs an audio-rate HenonC.

        ::

            >>> henon_c = supriya.ugens.HenonC.ar(
            ...     a=1.4,
            ...     b=0.3,
            ...     frequency=22050,
            ...     x_0=0,
            ...     x_1=0,
            ...     )
            >>> henon_c
            HenonC.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            a=a,
            b=b,
            frequency=frequency,
            x_0=x_0,
            x_1=x_1,
            )
        return ugen

    # def equation(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def a(self):
        """
        Gets `a` input of HenonC.

        ::

            >>> henon_c = supriya.ugens.HenonC.ar(
            ...     a=1.4,
            ...     b=0.3,
            ...     frequency=22050,
            ...     x_0=0,
            ...     x_1=0,
            ...     )
            >>> henon_c.a
            1.4

        Returns ugen input.
        """
        index = self._ordered_input_names.index('a')
        return self._inputs[index]

    @property
    def b(self):
        """
        Gets `b` input of HenonC.

        ::

            >>> henon_c = supriya.ugens.HenonC.ar(
            ...     a=1.4,
            ...     b=0.3,
            ...     frequency=22050,
            ...     x_0=0,
            ...     x_1=0,
            ...     )
            >>> henon_c.b
            0.3

        Returns ugen input.
        """
        index = self._ordered_input_names.index('b')
        return self._inputs[index]

    @property
    def frequency(self):
        """
        Gets `frequency` input of HenonC.

        ::

            >>> henon_c = supriya.ugens.HenonC.ar(
            ...     a=1.4,
            ...     b=0.3,
            ...     frequency=22050,
            ...     x_0=0,
            ...     x_1=0,
            ...     )
            >>> henon_c.frequency
            22050.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('frequency')
        return self._inputs[index]

    @property
    def x_0(self):
        """
        Gets `x_0` input of HenonC.

        ::

            >>> henon_c = supriya.ugens.HenonC.ar(
            ...     a=1.4,
            ...     b=0.3,
            ...     frequency=22050,
            ...     x_0=0,
            ...     x_1=0,
            ...     )
            >>> henon_c.x_0
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('x_0')
        return self._inputs[index]

    @property
    def x_1(self):
        """
        Gets `x_1` input of HenonC.

        ::

            >>> henon_c = supriya.ugens.HenonC.ar(
            ...     a=1.4,
            ...     b=0.3,
            ...     frequency=22050,
            ...     x_0=0,
            ...     x_1=0,
            ...     )
            >>> henon_c.x_1
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('x_1')
        return self._inputs[index]
