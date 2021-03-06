from supriya.realtime.ServerObjectProxy import ServerObjectProxy


class BusGroup(ServerObjectProxy):
    """
    A bus group.
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Main Classes'

    __slots__ = (
        '_bus_id',
        '_buses',
        '_calculation_rate',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        bus_count=1,
        calculation_rate=None,
        bus_id=None,
        ):
        import supriya.realtime
        import supriya.synthdefs
        ServerObjectProxy.__init__(self)
        calculation_rate = supriya.synthdefs.CalculationRate.from_expr(
            calculation_rate)
        assert calculation_rate in (
            supriya.synthdefs.CalculationRate.AUDIO,
            supriya.synthdefs.CalculationRate.CONTROL,
            )
        self._calculation_rate = calculation_rate
        bus_count = int(bus_count)
        assert 0 < bus_count
        self._buses = tuple(
            supriya.realtime.Bus(
                bus_group_or_index=self,
                calculation_rate=self.calculation_rate,
                )
            for _ in range(bus_count)
            )
        assert isinstance(bus_id, (type(None), int))
        self._bus_id = bus_id

    ### SPECIAL METHODS ###

    def __contains__(self, item):
        return self.buses.__contains__(item)

    def __float__(self):
        return float(self.bus_id)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._buses[item]
        elif isinstance(item, slice):
            indices = item.indices(len(self))
            bus_count = indices[1] - indices[0]
            bus_group = type(self)(
                bus_count=bus_count,
                bus_id=self.bus_id,
                calculation_rate=self.calculation_rate,
                )
            return bus_group

    def __int__(self):
        return int(self.bus_id)

    def __iter__(self):
        return iter(self.buses)

    def __len__(self):
        return len(self._buses)

    def __repr__(self):
        string = '<{}: {{{}}} @ {}>'.format(
            type(self).__name__,
            len(self),
            self.bus_id
            )
        return string

    def __str__(self):
        return self.map_symbol

    ### PRIVATE METHODS ###

    def _receive_bound_event(self, event=None):
        if event is None:
            return
        event = float(event)
        self.fill(event)

    ### PUBLIC METHODS ###

    def allocate(
        self,
        server=None,
        sync=False,
        ):
        import supriya.realtime
        if self.is_allocated:
            return
        ServerObjectProxy.allocate(self, server=server)
        allocator = supriya.realtime.Bus._get_allocator(
            calculation_rate=self.calculation_rate,
            server=self.server,
            )
        bus_id = allocator.allocate(len(self))
        if bus_id is None:
            ServerObjectProxy.free(self)
            raise ValueError
        self._bus_id = bus_id
        if sync:
            self.server.sync()
        return self

    def ar(self):
        """
        Creates an audio-rate input ugen subgraph.

        ..  container:: example

            ::

                >>> import supriya.realtime
                >>> audio_bus_group = supriya.realtime.BusGroup(
                ...     bus_id=8,
                ...     bus_count=4,
                ...     calculation_rate='audio',
                ...     )
                >>> ugen = audio_bus_group.ar()
                >>> graph(ugen)  # doctest: +SKIP

            ::

                >>> print(ugen)
                synthdef:
                    name: 0af6b551a643cad01e9994845ff4ae40
                    ugens:
                    -   In.ar:
                            bus: 8.0

        ..  container:: example

            ::

                >>> control_bus_group = supriya.realtime.BusGroup(
                ...     bus_id=8,
                ...     bus_count=4,
                ...     calculation_rate='control',
                ...     )
                >>> ugen = control_bus_group.ar()
                >>> graph(ugen)  # doctest: +SKIP

            ::

                >>> print(ugen)
                synthdef:
                    name: ecaa7fe9417cb0742cdcda87657fe9de
                    ugens:
                    -   In.kr:
                            bus: 8.0
                    -   K2A.ar/0:
                            source: In.kr[0]
                    -   K2A.ar/1:
                            source: In.kr[1]
                    -   K2A.ar/2:
                            source: In.kr[2]
                    -   K2A.ar/3:
                            source: In.kr[3]

        Returns ugen.
        """
        import supriya.synthdefs
        import supriya.ugens
        channel_count = len(self)
        if self.calculation_rate == supriya.synthdefs.CalculationRate.AUDIO:
            ugen = supriya.ugens.In.ar(
                bus=self.bus_id,
                channel_count=channel_count,
                )
        else:
            ugen = supriya.ugens.In.kr(
                bus=self.bus_id,
                channel_count=channel_count,
                )
            ugen = supriya.ugens.K2A.ar(
                source=ugen,
                )
        return ugen

    def fill(self, value):
        import supriya.commands
        import supriya.synthdefs
        if self.calculation_rate != supriya.synthdefs.CalculationRate.CONTROL:
            return
        if not self.is_allocated:
            return
        index_count_value_triples = [(self.bus_id, len(self), value)]
        request = supriya.commands.ControlBusFillRequest(
            index_count_value_triples=index_count_value_triples,
            )
        request.communicate(
            server=self.server,
            sync=False,
            )

    def free(self):
        import supriya.realtime
        if not self.is_allocated:
            return
        allocator = supriya.realtime.Bus._get_allocator(
            calculation_rate=self.calculation_rate,
            server=self.server,
            )
        allocator.free(self.bus_id)
        self._bus_id = None
        ServerObjectProxy.free(self)

    def get(self):
        import supriya.commands
        import supriya.synthdefs
        if self.calculation_rate != supriya.synthdefs.CalculationRate.CONTROL:
            return
        if not self.is_allocated:
            return
        index_count_pairs = [(self.bus_id, len(self))]
        request = supriya.commands.ControlBusGetContiguousRequest(
            index_count_pairs=index_count_pairs,
            )
        response = request.communicate(server=self.server)
        assert len(response) == 1
        value = response[0].bus_values
        return value

    def index(self, item):
        return self.buses.index(item)

    def kr(self):
        """
        Creates a control-rate input ugen subgraph.

        ..  container:: example

            ::

                >>> import supriya.realtime
                >>> audio_bus_group = supriya.realtime.BusGroup(
                ...     bus_id=8,
                ...     bus_count=4,
                ...     calculation_rate='audio',
                ...     )
                >>> ugen = audio_bus_group.kr()
                >>> graph(ugen)  # doctest: +SKIP

            ::

                >>> print(ugen)
                synthdef:
                    name: ffeda833c370bc644251437469e243ef
                    ugens:
                    -   In.ar:
                            bus: 8.0
                    -   A2K.kr/0:
                            source: In.ar[0]
                    -   A2K.kr/1:
                            source: In.ar[1]
                    -   A2K.kr/2:
                            source: In.ar[2]
                    -   A2K.kr/3:
                            source: In.ar[3]

        ..  container:: example

            ::

                >>> control_bus_group = supriya.realtime.BusGroup(
                ...     bus_id=8,
                ...     bus_count=4,
                ...     calculation_rate='control',
                ...     )
                >>> ugen = control_bus_group.kr()
                >>> graph(ugen)  # doctest: +SKIP

            ::

                >>> print(ugen)
                synthdef:
                    name: b64857a04b384841694ba85f74f0fd0b
                    ugens:
                    -   In.kr:
                            bus: 8.0

        Returns ugen.
        """
        import supriya.synthdefs
        import supriya.ugens
        channel_count = len(self)
        if self.calculation_rate == supriya.synthdefs.CalculationRate.AUDIO:
            ugen = supriya.ugens.In.ar(
                bus=self.bus_id,
                channel_count=channel_count,
                )
            ugen = supriya.ugens.A2K.kr(
                source=ugen,
                )
        else:
            ugen = supriya.ugens.In.kr(
                bus=self.bus_id,
                channel_count=channel_count,
                )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def bus_id(self):
        return self._bus_id

    @property
    def buses(self):
        return self._buses

    @property
    def calculation_rate(self):
        return self._calculation_rate

    @property
    def is_allocated(self):
        return self.server is not None

    @property
    def map_symbol(self):
        import supriya.synthdefs
        if self.calculation_rate == supriya.synthdefs.CalculationRate.AUDIO:
            map_symbol = 'a'
        else:
            map_symbol = 'c'
        map_symbol += str(self.bus_id)
        return map_symbol
