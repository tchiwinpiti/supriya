import collections
from supriya.system.SupriyaValueObject import SupriyaValueObject


class QueryTreeSynth(SupriyaValueObject, collections.Sequence):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_controls',
        '_extra',
        '_node_id',
        '_synthdef_name',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        node_id=None,
        synthdef_name=None,
        controls=None,
        **extra
        ):
        self._controls = controls
        self._extra = tuple(sorted(extra.items()))
        self._node_id = node_id
        self._synthdef_name = synthdef_name

    ### SPECIAL METHODS ###

    def __getitem__(self, item):
        return self._controls[item]

    def __len__(self):
        return len(self._controls)

    def __str__(self):
        result = self._get_str_format_pieces()
        result = '\n'.join(result)
        return result

    ### PRIVATE METHODS ###

    @classmethod
    def _from_nrt_synth(
        cls,
        state,
        node,
        include_controls=False,
        include_timespans=False,
        id_mapping=None,
        ):
        import supriya.nonrealtime
        import supriya.commands
        import supriya.synthdefs
        assert isinstance(node, supriya.nonrealtime.Synth)
        node_id = node.session_id
        synthdef_name = node.synthdef
        if isinstance(synthdef_name, supriya.synthdefs.SynthDef):
            synthdef_name = synthdef_name.actual_name
        controls = []
        if include_controls:
            settings = node._collect_settings(
                state.offset,
                persistent=True,
                id_mapping=id_mapping,
                )
            synthdef, synth_kwargs = node.synthdef, node.synth_kwargs
            for name, parameter in sorted(synthdef.parameters.items()):
                value = parameter.value
                if node.start_offset == state.offset:
                    if name in synth_kwargs:
                        value = synth_kwargs[name]
                if name in settings:
                    value = settings[name]
                try:
                    value = float(value)
                except Exception:
                    pass
                control = supriya.commands.QueryTreeControl(
                    control_name_or_index=name,
                    control_value=value,
                    )
                controls.append(control)
        extra = {}
        if include_timespans:
            extra.update(timespan=[node.start_offset, node.stop_offset])
        query_tree_synth = QueryTreeSynth(
            node_id=node_id,
            synthdef_name=synthdef_name,
            controls=controls,
            **extra
            )
        return query_tree_synth

    def _get_str_format_pieces(self):
        result = []
        string = '{} {}'.format(
            self.node_id,
            self.synthdef_name,
            )
        if self.extra:
            string = '{} ({})'.format(
                string,
                ', '.join(
                    '{}: {}'.format(key, value)
                    for key, value in self.extra
                    ),
                )
        result.append(string)
        if self.controls:
            control_string = ', '.join(
                str(control) for control in self.controls
                )
            control_string = '    ' + control_string
            result.append(control_string)
        return result

    ### PUBLIC METHODS ###

    @classmethod
    def from_synth(cls, synth, include_controls=False):
        import supriya.commands
        import supriya.realtime
        import supriya.synthdefs
        assert isinstance(synth, supriya.realtime.Synth)
        node_id = synth.node_id
        synthdef_name = synth.synthdef
        if isinstance(synthdef_name, supriya.synthdefs.SynthDef):
            synthdef_name = synthdef_name.actual_name
        controls = []
        if include_controls:
            for control in synth.controls:
                control = supriya.commands.QueryTreeControl.from_control(control)
                controls.append(control)
        controls = tuple(controls)
        query_tree_synth = QueryTreeSynth(
            node_id=node_id,
            synthdef_name=synthdef_name,
            controls=controls,
            )
        return query_tree_synth

    def to_dict(self):
        """
        Convert QueryTreeSynth to JSON-serializable dictionary.

        ::

            >>> query_tree_synth = supriya.commands.QueryTreeSynth(
            ...     node_id=1001,
            ...     synthdef_name='c1aa521afab5b0c0ce3d744690951649',
            ...     controls=(
            ...         supriya.commands.QueryTreeControl(
            ...             control_name_or_index='level',
            ...             control_value=1.0,
            ...             ),
            ...         supriya.commands.QueryTreeControl(
            ...             control_name_or_index='out',
            ...             control_value=0.0,
            ...             ),
            ...         ),
            ...     )

        ::

            >>> import json
            >>> result = query_tree_synth.to_dict()
            >>> result = json.dumps(
            ...     result,
            ...     indent=4,
            ...     separators=(',', ': '),
            ...     sort_keys=True,
            ...     )
            >>> print(result)
            {
                "controls": {
                    "level": 1.0,
                    "out": 0.0
                },
                "node_id": 1001,
                "synthdef": "c1aa521afab5b0c0ce3d744690951649"
            }

        """
        result = {
            'node_id': self.node_id,
            'synthdef': self.synthdef_name,
            'controls': {}
            }
        for control in self.controls:
            name = control.control_name_or_index
            result['controls'][name] = control.control_value
        return result

    ### PUBLIC PROPERTIES ###

    @property
    def controls(self):
        return self._controls

    @property
    def extra(self):
        return self._extra

    @property
    def node_id(self):
        return self._node_id

    @property
    def synthdef_name(self):
        return self._synthdef_name
