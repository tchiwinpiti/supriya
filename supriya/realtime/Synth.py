from supriya.realtime.Node import Node


class Synth(Node):
    """
    A synth.

    ::

        >>> import supriya.realtime
        >>> server = supriya.realtime.Server()
        >>> server.boot()
        <Server: udp://127.0.0.1:57751, 8i8o>

    ::

        >>> import supriya.synthdefs
        >>> import supriya.ugens
        >>> with supriya.synthdefs.SynthDefBuilder(
        ...     amplitude=0.0,
        ...     frequency=440.0,
        ...     ) as builder:
        ...     sin_osc = supriya.ugens.SinOsc.ar(
        ...         frequency=builder['frequency'],
        ...         )
        ...     sin_osc *= builder['amplitude']
        ...     out = supriya.ugens.Out.ar(
        ...         bus=0,
        ...         source=[sin_osc, sin_osc],
        ...         )
        ...
        >>> synthdef = builder.build()
        >>> synthdef.allocate()
        <SynthDef: e41193ac8b7216f49ff0d477876a3bf3>

    ::

        >>> synth = supriya.realtime.Synth(synthdef=synthdef).allocate()

    ::

        >>> server.quit()
        <Server: offline>

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Main Classes'

    __slots__ = (
        '_control_interface',
        '_register_controls',
        '_synthdef',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        synthdef=None,
        name=None,
        register_controls=None,
        **kwargs
        ):
        import supriya.assets.synthdefs
        import supriya.realtime
        import supriya.synthdefs
        Node.__init__(self, name=name)
        synthdef = synthdef or supriya.assets.synthdefs.default
        assert isinstance(synthdef, supriya.synthdefs.SynthDef)
        self._synthdef = synthdef
        self._control_interface = supriya.realtime.SynthInterface(
            client=self,
            synthdef=self._synthdef,
            )
        if register_controls is not None:
            register_controls = bool(register_controls)
        self._register_controls = register_controls
        self._control_interface._set(**kwargs)

    ### SPECIAL METHODS ###

    def __getitem__(self, item):
        return self._control_interface[item]

    def __setitem__(self, items, values):
        self.controls.__setitem__(items, values)

    def __str__(self):
        result = []
        node_id = self.node_id
        if node_id is None:
            node_id = '???'
        if self.name:
            string = '{node_id} {synthdef} ({name})'
        else:
            string = '{node_id} {synthdef}'
        string = string.format(
            name=self.name,
            node_id=node_id,
            synthdef=self.synthdef.actual_name,
            )
        result.append(string)
        control_pieces = []
        controls = sorted(self.controls, key=lambda x: x.name)
        for control in controls:
            control_piece = '{}: {!s}'.format(
                control.name,
                control.value,
                )
            control_pieces.append(control_piece)
        control_pieces = '    ' + ', '.join(control_pieces)
        result.append(control_pieces)
        result = '\n'.join(result)
        return result

    ### PRIVATE METHODS ###

    def _unregister_with_local_server(self):
        node_id = Node._unregister_with_local_server(self)
        if 'gate' in self.controls:
            self['gate'].reset()
        return node_id

    ### PUBLIC METHODS ###

    def allocate(
        self,
        add_action=None,
        node_id_is_permanent=False,
        sync=True,
        target_node=None,
        **kwargs
        ):
        import supriya.commands
        import supriya.realtime
        if self.is_allocated:
            return
        add_action, node_id, target_node_id = Node.allocate(
            self,
            add_action=add_action,
            node_id_is_permanent=node_id_is_permanent,
            target_node=target_node,
            )
        if not self.synthdef.is_allocated:
            self.synthdef.allocate()
        self.controls._set(**kwargs)
        requests = []
        settings, map_requests = self.controls._make_synth_new_settings()
        synth_request = supriya.commands.SynthNewRequest(
            add_action=add_action,
            node_id=node_id,
            synthdef=self.synthdef,
            target_node_id=target_node_id,
            **settings
            )
        requests.append(synth_request)
        requests.extend(map_requests)
        if self.is_paused:
            pause_request = supriya.commands.NodeRunRequest(
                [(self.node_id, False)])
            requests.append(pause_request)
        if 1 < len(requests):
            message_bundler = supriya.realtime.MessageBundler(
                server=self.server,
                sync=True,
                )
            message_bundler.add_messages(requests)
            message_bundler.add_synchronizing_request(synth_request)
            message_bundler.send_messages()
        else:
            synth_request.communicate(
                server=self.server,
                sync=True,
                )
        return self

    def free(self):
        Node.free(self)

    def release(self):
        if 'gate' in self.controls:
            self['gate'] = 0
        else:
            self.free()

    def unrelease(self):
        if 'gate' in self.controls:
            self['gate'] = 1
        self.unpause()

    ### PUBLIC PROPERTIES ###

    @property
    def controls(self):
        return self._control_interface

    @property
    def synthdef(self):
        return self._synthdef

    @property
    def register_controls(self):
        return self._register_controls
