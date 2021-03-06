from supriya.ugens.InfoUGenBase import InfoUGenBase


class NumControlBuses(InfoUGenBase):
    """
    A number of control buses info unit generator.

    ::

        >>> supriya.ugens.NumControlBuses.ir()
        NumControlBuses.ir()

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
