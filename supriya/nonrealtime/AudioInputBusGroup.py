import supriya.synthdefs
from supriya.nonrealtime.BusGroup import BusGroup


class AudioInputBusGroup(BusGroup):
    """
    A non-realtime audio input bus group.
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Session Objects'

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        session,
        ):
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        bus_count = session.options.input_bus_channel_count
        BusGroup.__init__(
            self,
            session,
            bus_count=bus_count,
            calculation_rate=calculation_rate,
            )
