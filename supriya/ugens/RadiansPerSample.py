from supriya.ugens.InfoUGenBase import InfoUGenBase


class RadiansPerSample(InfoUGenBase):
    """
    A radians-per-sample info unit generator.

    ::

        >>> supriya.ugens.RadiansPerSample.ir()
        RadiansPerSample.ir()

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
