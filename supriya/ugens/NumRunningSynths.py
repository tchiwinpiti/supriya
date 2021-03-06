from supriya.ugens.InfoUGenBase import InfoUGenBase


class NumRunningSynths(InfoUGenBase):
    """
    A number of running synths info unit generator.

    ::

        >>> supriya.ugens.NumRunningSynths.ir()
        NumRunningSynths.ir()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Info UGens'

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        ):
        InfoUGenBase.__init__(
            self,
            calculation_rate=calculation_rate,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def kr(cls, **kwargs):
        """
        Construct a control-rate ugen.

        ::

            >>> supriya.ugens.NumRunningSynths.kr()
            NumRunningSynths.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            **kwargs
            )
        return ugen
