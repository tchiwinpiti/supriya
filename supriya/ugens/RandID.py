from supriya.ugens.WidthFirstUGen import WidthFirstUGen


class RandID(WidthFirstUGen):
    """
    Sets the synth's random generator ID.

    ::

        >>> rand_id = supriya.ugens.RandID.ir(
        ...     rand_id=1,
        ...     )
        >>> rand_id
        RandID.ir()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Noise UGens'

    __slots__ = ()

    _ordered_input_names = (
        'rand_id',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        rand_id=1,
        ):
        WidthFirstUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            rand_id=rand_id,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ir(
        cls,
        rand_id=0,
        ):
        """
        Constructs a scalar-rate RandID.

        ::

            >>> rand_id = supriya.ugens.RandID.ir(
            ...     rand_id=1,
            ...     )
            >>> rand_id
            RandID.ir()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.SCALAR
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            rand_id=rand_id,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        rand_id=0,
        ):
        """
        Constructs a control-rate RandID.

        ::

            >>> rand_id = supriya.ugens.RandID.kr(
            ...     rand_id=1,
            ...     )
            >>> rand_id
            RandID.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            rand_id=rand_id,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def rand_id(self):
        """
        Gets `rand_id` input of RandID.

        ::

            >>> rand_id = supriya.ugens.RandID.kr(
            ...     rand_id=1,
            ...     )
            >>> rand_id.rand_id
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('rand_id')
        return self._inputs[index]
