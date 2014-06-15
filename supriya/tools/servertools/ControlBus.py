# -*- encoding: utf-8 -*-
from supriya.tools.servertools.Bus import Bus


class ControlBus(Bus):
    r'''A control bus.

    ::

        >>> from supriya.tools import servertools
        >>> server = servertools.Server().boot()

    ::

        >>> control_bus = servertools.ControlBus(channel_count=4)
        >>> control_bus.allocate()
        >>> control_bus.bus_id
        0

    ::

        >>> control_bus.map_symbol
        'c0'

    ::

        >>> control_bus.free()
        >>> server.quit()
        RECV: OscMessage('/done', '/quit')
        <Server: offline>

    '''

    ### INITIALIZER ###

    def __init__(
        self,
        channel_count=1,
        ):
        Bus.__init__(
            self,
            channel_count=channel_count,
            )

    ### PUBLIC METHODS ###

    def allocate(self, server=None):
        Bus.allocate(self, server=server)
        bus_id = self.server.control_bus_allocator.allocate()
        if bus_id is None:
            raise Exception
        assert bus_id not in self.server._control_busses
        self.server._control_busses[bus_id] = self
        self._bus_id = bus_id

    def free(self):
        if self.server is not None:
            self.server.control_bus_allocator.free(self.bus_id)
            del(self.server._control_busses[self._bus_id])
        self._bus_id = None
        Bus.free(self)

    ### PUBLIC PROPERTIES ###

    @property
    def calculation_rate(self):
        r'''Gets this bus' calculation rate.
        
        ::

            >>> control_bus = servertools.ControlBus()
            >>> control_bus.calculation_rate
            <CalculationRate.CONTROL: 1>

        Returns calculation rate.
        '''
        from supriya.tools import synthdeftools
        return synthdeftools.CalculationRate.CONTROL
