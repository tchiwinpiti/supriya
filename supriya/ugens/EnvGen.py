from supriya.ugens.UGen import UGen


class EnvGen(UGen):
    """
    An envelope generator.

    ::

        >>> envelope = supriya.synthdefs.Envelope.percussive()
        >>> supriya.ugens.EnvGen.ar(envelope=envelope)
        EnvGen.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Envelope Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'gate',
        'level_scale',
        'level_bias',
        'time_scale',
        'done_action',
        'envelope',
        )

    _unexpanded_input_names = (
        'envelope',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        done_action=0,
        envelope=None,
        gate=1.0,
        level_bias=0.0,
        level_scale=1.0,
        time_scale=1.0,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            done_action=done_action,
            envelope=envelope,
            gate=gate,
            level_bias=level_bias,
            level_scale=level_scale,
            time_scale=time_scale,
            )

    ### PRIVATE METHODS ###

    @classmethod
    def _new_expanded(
        cls,
        calculation_rate=None,
        done_action=None,
        envelope=None,
        gate=1.0,
        level_bias=0.0,
        level_scale=1.0,
        time_scale=1.0,
        ):
        import supriya.synthdefs
        if not isinstance(done_action, supriya.synthdefs.Parameter):
            done_action = supriya.synthdefs.DoneAction.from_expr(done_action)
        if envelope is None:
            envelope = supriya.synthdefs.Envelope()
        assert isinstance(envelope, supriya.synthdefs.Envelope)
        envelope = envelope.serialize()
        return super(EnvGen, cls)._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            envelope=envelope,
            gate=gate,
            level_bias=level_bias,
            level_scale=level_scale,
            time_scale=time_scale,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        done_action=0,
        envelope=None,
        gate=1.0,
        level_bias=0.0,
        level_scale=1.0,
        time_scale=1.0,
        ):
        """
        Constructs an audio-rate envelope generator.

        ::

            >>> envelope = supriya.synthdefs.Envelope.percussive()
            >>> supriya.ugens.EnvGen.ar(
            ...     envelope=envelope,
            ...     )
            EnvGen.ar()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            envelope=envelope,
            gate=gate,
            level_bias=level_bias,
            level_scale=level_scale,
            time_scale=time_scale,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        done_action=0,
        envelope=None,
        gate=1.0,
        level_bias=0.0,
        level_scale=1.0,
        time_scale=1.0,
        ):
        """
        Constructs an control-rate envelope generator.

        ::

            >>> envelope = supriya.synthdefs.Envelope.percussive()
            >>> supriya.ugens.EnvGen.kr(
            ...     envelope=envelope,
            ...     )
            EnvGen.kr()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            envelope=envelope,
            gate=gate,
            level_bias=level_bias,
            level_scale=level_scale,
            time_scale=time_scale,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def done_action(self):
        """
        Gets `done_action` input of EnvGen.

        ::

            >>> done_action = 0
            >>> env_gen = supriya.ugens.EnvGen.ar(
            ...     done_action=done_action,
            ...     )
            >>> env_gen.done_action
            0.0

        Returns input.
        """
        index = self._ordered_input_names.index('done_action')
        return self._inputs[index]

    @property
    def envelope(self):
        """
        Gets `envelope` input of EnvGen.

        ::

            >>> envelope = supriya.synthdefs.Envelope.percussive()
            >>> env_gen = supriya.ugens.EnvGen.ar(
            ...     envelope=envelope,
            ...     )
            >>> env_gen.envelope
            (0.0, 2.0, -99.0, -99.0, 1.0, 0.01, 5.0, -4.0, 0.0, 1.0, 5.0, -4.0)

        Returns input.
        """
        index = self._ordered_input_names.index('envelope')
        return tuple(self._inputs[index:])

    @property
    def gate(self):
        """
        Gets `gate` input of EnvGen.

        ::

            >>> gate = 1
            >>> env_gen = supriya.ugens.EnvGen.ar(
            ...     gate=gate,
            ...     )
            >>> env_gen.gate
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('gate')
        return self._inputs[index]

    @property
    def has_done_flag(self):
        """
        Is true if UGen has a done flag.

        Returns boolean.
        """
        return True

    @property
    def level_bias(self):
        """
        Gets `level_bias` input of EnvGen.

        ::

            >>> level_bias = 0
            >>> env_gen = supriya.ugens.EnvGen.ar(
            ...     level_bias=level_bias,
            ...     )
            >>> env_gen.level_bias
            0.0

        Returns input.
        """
        index = self._ordered_input_names.index('level_bias')
        return self._inputs[index]

    @property
    def level_scale(self):
        """
        Gets `level_scale` input of EnvGen.

        ::

            >>> level_scale = 1
            >>> env_gen = supriya.ugens.EnvGen.ar(
            ...     level_scale=level_scale,
            ...     )
            >>> env_gen.level_scale
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('level_scale')
        return self._inputs[index]

    @property
    def time_scale(self):
        """
        Gets `time_scale` input of EnvGen.

        ::

            >>> time_scale = 1
            >>> env_gen = supriya.ugens.EnvGen.ar(
            ...     time_scale=time_scale,
            ...     )
            >>> env_gen.time_scale
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('time_scale')
        return self._inputs[index]
