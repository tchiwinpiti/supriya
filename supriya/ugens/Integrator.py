from supriya.ugens.Filter import Filter


class Integrator(Filter):
    """
    A leaky integrator.

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> integrator = supriya.ugens.Integrator.ar(
        ...     coefficient=1,
        ...     source=source,
        ...     )
        >>> integrator
        Integrator.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Filter UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'coefficient',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        coefficient=1,
        source=None,
        ):
        Filter.__init__(
            self,
            calculation_rate=calculation_rate,
            coefficient=coefficient,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        coefficient=1,
        source=None,
        ):
        """
        Constructs an audio-rate Integrator.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> integrator = supriya.ugens.Integrator.ar(
            ...     coefficient=1,
            ...     source=source,
            ...     )
            >>> integrator
            Integrator.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            coefficient=coefficient,
            source=source,
            )
        return ugen

    # def coeffs(): ...

    @classmethod
    def kr(
        cls,
        coefficient=1,
        source=None,
        ):
        """
        Constructs a control-rate Integrator.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> integrator = supriya.ugens.Integrator.kr(
            ...     coefficient=1,
            ...     source=source,
            ...     )
            >>> integrator
            Integrator.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            coefficient=coefficient,
            source=source,
            )
        return ugen

    # def magResponse(): ...

    # def magResponse2(): ...

    # def magResponse5(): ...

    # def magResponseN(): ...

    # def scopeResponse(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def coefficient(self):
        """
        Gets `coefficient` input of Integrator.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> integrator = supriya.ugens.Integrator.ar(
            ...     coefficient=1,
            ...     source=source,
            ...     )
            >>> integrator.coefficient
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('coefficient')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of Integrator.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> integrator = supriya.ugens.Integrator.ar(
            ...     coefficient=1,
            ...     source=source,
            ...     )
            >>> integrator.source
            In.ar()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
