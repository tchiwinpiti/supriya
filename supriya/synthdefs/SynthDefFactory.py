import copy
import types
from supriya.system.SupriyaObject import SupriyaObject


class SynthDefFactory(SupriyaObject):
    """
    A factory class for building SynthDefs with common signal flow structures.

    ..  container:: example

        ::

            >>> factory = supriya.synthdefs.SynthDefFactory()

        ::

            >>> def signal_block(builder, source, state):
            ...     iterations = state.get('iterations') or 2
            ...     for _ in range(iterations):
            ...         source = supriya.ugens.AllpassC.ar(
            ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
            ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
            ...             source=source,
            ...             maximum_delay_time=0.1,
            ...             )
            ...     return source

        ::

            >>> factory = factory.with_input()
            >>> factory = factory.with_output()
            >>> factory = factory.with_signal_block(signal_block)
            >>> synthdef = factory.build()
            >>> graph(synthdef)  # doctest: +SKIP

        ::

            >>> print(synthdef)
            synthdef:
                name: 93e1ac306eb2501b3ef8737186e34ab9
                ugens:
                -   Control.ir: null
                -   In.ar:
                        bus: Control.ir[0:out]
                -   ExpRand.ir/0:
                        maximum: 0.01
                        minimum: 0.1
                -   ExpRand.ir/1:
                        maximum: 0.01
                        minimum: 0.1
                -   AllpassC.ar/0:
                        decay_time: ExpRand.ir/0[0]
                        delay_time: ExpRand.ir/1[0]
                        maximum_delay_time: 0.1
                        source: In.ar[0]
                -   ExpRand.ir/2:
                        maximum: 0.01
                        minimum: 0.1
                -   ExpRand.ir/3:
                        maximum: 0.01
                        minimum: 0.1
                -   AllpassC.ar/1:
                        decay_time: ExpRand.ir/2[0]
                        delay_time: ExpRand.ir/3[0]
                        maximum_delay_time: 0.1
                        source: AllpassC.ar/0[0]
                -   Out.ar:
                        bus: Control.ir[0:out]
                        source[0]: AllpassC.ar/1[0]

    ..  container:: example

        ::

            >>> synthdef = factory.build(iterations=4)
            >>> graph(synthdef)  # doctest: +SKIP

        ::

            >>> print(synthdef)
            synthdef:
                name: 9be4856556bc7986e05f858f3805551b
                ugens:
                -   Control.ir: null
                -   In.ar:
                        bus: Control.ir[0:out]
                -   ExpRand.ir/0:
                        maximum: 0.01
                        minimum: 0.1
                -   ExpRand.ir/1:
                        maximum: 0.01
                        minimum: 0.1
                -   AllpassC.ar/0:
                        decay_time: ExpRand.ir/0[0]
                        delay_time: ExpRand.ir/1[0]
                        maximum_delay_time: 0.1
                        source: In.ar[0]
                -   ExpRand.ir/2:
                        maximum: 0.01
                        minimum: 0.1
                -   ExpRand.ir/3:
                        maximum: 0.01
                        minimum: 0.1
                -   AllpassC.ar/1:
                        decay_time: ExpRand.ir/2[0]
                        delay_time: ExpRand.ir/3[0]
                        maximum_delay_time: 0.1
                        source: AllpassC.ar/0[0]
                -   ExpRand.ir/4:
                        maximum: 0.01
                        minimum: 0.1
                -   ExpRand.ir/5:
                        maximum: 0.01
                        minimum: 0.1
                -   AllpassC.ar/2:
                        decay_time: ExpRand.ir/4[0]
                        delay_time: ExpRand.ir/5[0]
                        maximum_delay_time: 0.1
                        source: AllpassC.ar/1[0]
                -   ExpRand.ir/6:
                        maximum: 0.01
                        minimum: 0.1
                -   ExpRand.ir/7:
                        maximum: 0.01
                        minimum: 0.1
                -   AllpassC.ar/3:
                        decay_time: ExpRand.ir/6[0]
                        delay_time: ExpRand.ir/7[0]
                        maximum_delay_time: 0.1
                        source: AllpassC.ar/2[0]
                -   Out.ar:
                        bus: Control.ir[0:out]
                        source[0]: AllpassC.ar/3[0]

    ..  container:: example

        ::

            >>> synthdef = factory.build(channel_count=2)
            >>> graph(synthdef)  # doctest: +SKIP

        ::

            >>> print(synthdef)
            synthdef:
                name: 42450f0bb42c5e21b27c159ad6572390
                ugens:
                -   Control.ir: null
                -   In.ar:
                        bus: Control.ir[0:out]
                -   ExpRand.ir/0:
                        maximum: 0.01
                        minimum: 0.1
                -   ExpRand.ir/1:
                        maximum: 0.01
                        minimum: 0.1
                -   AllpassC.ar/0:
                        decay_time: ExpRand.ir/0[0]
                        delay_time: ExpRand.ir/1[0]
                        maximum_delay_time: 0.1
                        source: In.ar[0]
                -   AllpassC.ar/1:
                        decay_time: ExpRand.ir/0[0]
                        delay_time: ExpRand.ir/1[0]
                        maximum_delay_time: 0.1
                        source: In.ar[1]
                -   ExpRand.ir/2:
                        maximum: 0.01
                        minimum: 0.1
                -   ExpRand.ir/3:
                        maximum: 0.01
                        minimum: 0.1
                -   AllpassC.ar/2:
                        decay_time: ExpRand.ir/2[0]
                        delay_time: ExpRand.ir/3[0]
                        maximum_delay_time: 0.1
                        source: AllpassC.ar/0[0]
                -   AllpassC.ar/3:
                        decay_time: ExpRand.ir/2[0]
                        delay_time: ExpRand.ir/3[0]
                        maximum_delay_time: 0.1
                        source: AllpassC.ar/1[0]
                -   Out.ar:
                        bus: Control.ir[0:out]
                        source[0]: AllpassC.ar/2[0]
                        source[1]: AllpassC.ar/3[0]

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_channel_count',
        '_feedback_loop',
        '_gate',
        '_initial_state',
        '_input',
        '_output',
        '_parameter_blocks',
        '_parameters',
        '_rand_id',
        '_signal_blocks',
        '_silence_detection',
        )

    ### INITIALIZER ###

    def __init__(self, channel_count=1, **kwargs):
        channel_count = int(channel_count)
        assert channel_count > 0
        self._channel_count = channel_count
        self._feedback_loop = None
        self._gate = {}
        self._initial_state = {}
        self._input = {}
        self._output = {}
        self._parameter_blocks = []
        self._parameters = sorted(tuple(kwargs.items()))
        self._rand_id = None
        self._signal_blocks = []
        self._silence_detection = None

    ### PRIVATE METHODS ###

    def _setup_parameters_and_state(self, builder, state, kwargs):
        import supriya.synthdefs
        import supriya.ugens
        state['channel_count'] = self._channel_count
        state.update(kwargs)
        for parameter_block in self._parameter_blocks:
            parameter_block(builder, state)
        if self._rand_id:
            builder._add_parameter('rand_id', self._rand_id, 'SCALAR')
            supriya.ugens.RandID.ir(rand_id=builder['rand_id'])
        if self._gate:
            builder._add_parameter('gate', 1, 'TRIGGER')
            state['gate'] = supriya.ugens.Linen.kr(
                attack_time=self._gate['attack_time'],
                done_action=supriya.synthdefs.DoneAction.FREE_SYNTH,
                gate=builder['gate'],
                release_time=self._gate['release_time'],
                )
        if self._output or self._input:
            builder._add_parameter('out', 0, 'SCALAR')
        if (
            self._output.get('windowed') or
            self._input.get('windowed')
            ):
            builder._add_parameter('duration', 1, 'SCALAR')
            state['line'] = supriya.ugens.Line.kr(
                done_action=supriya.synthdefs.DoneAction.FREE_SYNTH,
                duration=builder['duration'],
                )
            state['window'] = state['line'].hanning_window()
        if (
            not self._output.get('windowed') and
            self._output.get('crossfaded')
            ):
            builder._add_parameter('crossfade', 0, 'CONTROL')
        if self._output.get('leveled'):
            builder._add_parameter('level', 1, 'CONTROL')
        for key, value in self._parameters:
            builder._add_parameter(key, value)

    def _build_input(self, builder, state):
        import supriya.ugens
        if not self._input:
            return
        source = supriya.ugens.In.ar(
            bus=builder['out'],
            channel_count=state['channel_count'],
            )
        if self._input.get('windowed'):
            source *= state['window']
        return source

    def _build_feedback_loop_input(self, builder, source, state):
        import supriya.ugens
        if self._feedback_loop:
            local_in = supriya.ugens.LocalIn.ar(
                channel_count=state['channel_count'],
                )
            if source is None:
                source = local_in
            else:
                source += local_in
        return source

    def _build_feedback_loop_output(self, builder, source, state):
        import supriya.ugens
        if not self._feedback_loop:
            return
        if isinstance(self._feedback_loop, types.FunctionType):
            source = self._feedback_loop(builder, source, state)
        supriya.ugens.LocalOut.ar(
            source=source,
            )

    def _build_output(self, builder, source, state):
        import supriya.ugens
        if not self._output:
            return
        crossfaded = self._output.get('crossfaded')
        replacing = self._output.get('replacing')
        windowed = self._output.get('windowed')
        gate = state.get('gate')
        if self._output.get('leveled') and not crossfaded:
            source *= builder['level']
        out_class = supriya.ugens.Out
        kwargs = dict(
            bus=builder['out'],
            source=source,
            )
        if replacing:
            out_class = supriya.ugens.ReplaceOut
        if crossfaded:
            out_class = supriya.ugens.XOut
            if windowed:
                window = state['window']
                if self._output.get('leveled'):
                    window *= builder['level']
                kwargs['crossfade'] = window
            else:
                kwargs['crossfade'] = builder['crossfade']
            if gate:
                kwargs['crossfade'] *= gate
        elif windowed:
            window = state['window']
            kwargs['source'] *= window
            if gate:
                kwargs['source'] *= gate
        elif gate:
            kwargs['source'] *= gate
        out_class.ar(**kwargs)

    def _build_silence_detection(self, builder, source, state):
        import supriya.synthdefs
        import supriya.ugens
        if not self._silence_detection:
            return
        supriya.ugens.DetectSilence.kr(
            done_action=supriya.synthdefs.DoneAction.FREE_SYNTH,
            source=supriya.ugens.Mix.new(source),
            )

    def _clone(self):
        clone = type(self)()
        for name in self.__slots__:
            value = getattr(self, name)
            setattr(clone, name, copy.copy(value))
        return clone

    ### PUBLIC METHODS ###

    def build(self, name=None, **kwargs):
        """
        Build the SynthDef.
        """
        import supriya.synthdefs
        builder = supriya.synthdefs.SynthDefBuilder()
        state = self._initial_state.copy()
        with builder:
            state.update(**kwargs)
            self._setup_parameters_and_state(builder, state, kwargs)
            source = self._build_input(builder, state)
            source = self._build_feedback_loop_input(builder, source, state)
            for signal_block in self._signal_blocks:
                source = signal_block(builder, source, state)
                assert isinstance(source, supriya.synthdefs.UGenMethodMixin)
            self._build_output(builder, source, state)
            self._build_feedback_loop_output(builder, source, state)
            self._build_silence_detection(builder, source, state)
        return builder.build(name=name)

    def with_channel_count(self, channel_count):
        """
        Return a new factory configured with `channel_count`.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_input()
                >>> factory = factory.with_output()
                >>> factory = factory.with_signal_block(signal_block)

        ..  container:: example

            Configure the factory with 4 channels:

            ::

                >>> factory = factory.with_channel_count(4)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: a94da97d30cbb05fe8d1b79d11b7ca26
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[1]
                    -   AllpassC.ar/2:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[2]
                    -   AllpassC.ar/3:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[3]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/4:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   AllpassC.ar/5:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/1[0]
                    -   AllpassC.ar/6:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/2[0]
                    -   AllpassC.ar/7:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/3[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/4[0]
                            source[1]: AllpassC.ar/5[0]
                            source[2]: AllpassC.ar/6[0]
                            source[3]: AllpassC.ar/7[0]

        ..  container:: example

            Channel count can be overridden at build time:

            ::

                >>> synthdef = factory.build(channel_count=3)
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 4fc8b719bbc57ac050e6b6fbe632d3e6
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[1]
                    -   AllpassC.ar/2:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[2]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/3:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   AllpassC.ar/4:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/1[0]
                    -   AllpassC.ar/5:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/2[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/3[0]
                            source[1]: AllpassC.ar/4[0]
                            source[2]: AllpassC.ar/5[0]

        """
        channel_count = int(channel_count)
        assert channel_count > 0
        clone = self._clone()
        clone._channel_count = channel_count
        return clone

    def with_feedback_loop(self, block_function=None):
        """
        Return a new factory configured with a feedback loop.

        Feedback block functions follow the same guidelines as other signal
        block functions.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_input()
                >>> factory = factory.with_output()
                >>> factory = factory.with_signal_block(signal_block)

        ..  container:: example

            Configure the factory with a basic feedback loop:

            ::

                >>> factory = factory.with_feedback_loop()
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 9e42aa261e0b5a913cf6256723da941b
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   LocalIn.ar:
                            default[0]: 0.0
                    -   BinaryOpUGen(ADDITION).ar:
                            left: In.ar[0]
                            right: LocalIn.ar[0]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: BinaryOpUGen(ADDITION).ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/1[0]
                    -   LocalOut.ar:
                            source[0]: AllpassC.ar/1[0]

        ..  container:: example

            Configure the factory with a modulated feedback loop via a signal
            block function:

            ::

                >>> def feedback_block(builder, source, state):
                ...     return source * supriya.ugens.SinOsc.kr(frequency=0.3)

            ::

                >>> factory = factory.with_feedback_loop(feedback_block)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: c9fcaca9d89ff2799922976ba00b0e74
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   LocalIn.ar:
                            default[0]: 0.0
                    -   BinaryOpUGen(ADDITION).ar:
                            left: In.ar[0]
                            right: LocalIn.ar[0]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: BinaryOpUGen(ADDITION).ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/1[0]
                    -   SinOsc.kr:
                            frequency: 0.3
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: AllpassC.ar/1[0]
                            right: SinOsc.kr[0]
                    -   LocalOut.ar:
                            source[0]: BinaryOpUGen(MULTIPLICATION).ar[0]

        """
        clone = self._clone()
        if block_function:
            clone._feedback_loop = block_function
        else:
            clone._feedback_loop = True
        return clone

    def with_gate(
        self,
        attack_time=0.02,
        release_time=0.02,
        ):
        """
        Return a new factory configured with a gate.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_input()
                >>> factory = factory.with_output()
                >>> factory = factory.with_signal_block(signal_block)

        ..  container:: example

            Configure the factory with a gate envelope and corresponding gate
            parameter:

            ::

                >>> factory = factory.with_gate()
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 18bb48452af6de95a01169c2ac9a1843
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   TrigControl.kr: null
                    -   Linen.kr:
                            attack_time: 0.02
                            done_action: 2.0
                            gate: TrigControl.kr[0:gate]
                            release_time: 0.02
                            sustain_level: 1.0
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: AllpassC.ar/1[0]
                            right: Linen.kr[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: BinaryOpUGen(MULTIPLICATION).ar[0]

        """
        clone = self._clone()
        clone._gate.update(
            attack_time=float(attack_time),
            release_time=float(release_time),
            )
        return clone

    def with_initial_state(self, **state):
        """
        Return a new factory configured with an inital state comprised of
        key/value pairs.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_input()
                >>> factory = factory.with_output()
                >>> factory = factory.with_signal_block(signal_block)

        ..  container:: example

            Configure the factory with an initial state consisting of a single
            key/value pair which can be accessed in the previously configured
            signal block function:

            ::

                >>> factory = factory.with_initial_state(iterations=4)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 9be4856556bc7986e05f858f3805551b
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   ExpRand.ir/4:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/5:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/2:
                            decay_time: ExpRand.ir/4[0]
                            delay_time: ExpRand.ir/5[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/1[0]
                    -   ExpRand.ir/6:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/7:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/3:
                            decay_time: ExpRand.ir/6[0]
                            delay_time: ExpRand.ir/7[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/2[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/3[0]

        """
        clone = self._clone()
        clone._initial_state.update(**state)
        return clone

    def with_input(
        self,
        windowed=False,
        ):
        """
        Return a new factory configured with a bus input.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_signal_block(signal_block)
                >>> factory = factory.with_output()

        ..  container:: example

            Configure the factory with a basic bus input:

            ::

                >>> factory = factory.with_input()
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 93e1ac306eb2501b3ef8737186e34ab9
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/1[0]

        ..  container:: example

            Configure the factory with a windowed bus input:

            ::

                >>> factory = factory.with_input(windowed=True)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 6dabe7ebb4a52a0daa6eb54adbe7ccee
                    ugens:
                    -   Control.ir: null
                    -   Line.kr:
                            done_action: 2.0
                            duration: Control.ir[0:duration]
                            start: 0.0
                            stop: 1.0
                    -   UnaryOpUGen(HANNING_WINDOW).kr:
                            source: Line.kr[0]
                    -   In.ar:
                            bus: Control.ir[1:out]
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: In.ar[0]
                            right: UnaryOpUGen(HANNING_WINDOW).kr[0]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: BinaryOpUGen(MULTIPLICATION).ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   Out.ar:
                            bus: Control.ir[1:out]
                            source[0]: AllpassC.ar/1[0]

        ..  container:: example

            A factory configured with both a windowed bus input and output will
            re-use the windowing signal:

            ::

                >>> factory = factory.with_input(windowed=True)
                >>> factory = factory.with_output(windowed=True)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 8e3abddff837fac19c9225c86736790f
                    ugens:
                    -   Control.ir: null
                    -   Line.kr:
                            done_action: 2.0
                            duration: Control.ir[0:duration]
                            start: 0.0
                            stop: 1.0
                    -   UnaryOpUGen(HANNING_WINDOW).kr:
                            source: Line.kr[0]
                    -   In.ar:
                            bus: Control.ir[1:out]
                    -   BinaryOpUGen(MULTIPLICATION).ar/0:
                            left: In.ar[0]
                            right: UnaryOpUGen(HANNING_WINDOW).kr[0]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: BinaryOpUGen(MULTIPLICATION).ar/0[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   BinaryOpUGen(MULTIPLICATION).ar/1:
                            left: AllpassC.ar/1[0]
                            right: UnaryOpUGen(HANNING_WINDOW).kr[0]
                    -   Out.ar:
                            bus: Control.ir[1:out]
                            source[0]: BinaryOpUGen(MULTIPLICATION).ar/1[0]

        """
        clone = self._clone()
        clone._input.update(
            windowed=bool(windowed),
            )
        return clone

    def with_output(
        self,
        crossfaded=False,
        leveled=False,
        replacing=False,
        windowed=False,
        ):
        """
        Return a new factory configured with a bus output.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_input()
                >>> factory = factory.with_signal_block(signal_block)

        ..  container:: example


            Configure the factory with a basic bus output:

            ::

                >>> factory = factory.with_output()
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 93e1ac306eb2501b3ef8737186e34ab9
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/1[0]

        ..  container:: example

            Configure the factory with a windowed bus output:

            ::

                >>> factory = factory.with_output(windowed=True)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 4457d151cbd44a8ca6061a0bff7ce2a9
                    ugens:
                    -   Control.ir: null
                    -   Line.kr:
                            done_action: 2.0
                            duration: Control.ir[0:duration]
                            start: 0.0
                            stop: 1.0
                    -   UnaryOpUGen(HANNING_WINDOW).kr:
                            source: Line.kr[0]
                    -   In.ar:
                            bus: Control.ir[1:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: AllpassC.ar/1[0]
                            right: UnaryOpUGen(HANNING_WINDOW).kr[0]
                    -   Out.ar:
                            bus: Control.ir[1:out]
                            source[0]: BinaryOpUGen(MULTIPLICATION).ar[0]

        ..  container:: example

            Configure the factory with a crossfade-able bus output:

            ::

                >>> factory = factory.with_output(crossfaded=True)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 0d965f5316259794ff2dba023ee46cce
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   Control.kr: null
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   XOut.ar:
                            bus: Control.ir[0:out]
                            crossfade: Control.kr[0:crossfade]
                            source[0]: AllpassC.ar/1[0]

        ..  container:: example

            Configure the factory with a basic bus output preceded by an
            amplitude level control:

            ::

                >>> factory = factory.with_output(leveled=True)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: ecb4d44b80293e1bd27623849a81dbdb
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   Control.kr: null
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: AllpassC.ar/1[0]
                            right: Control.kr[0:level]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: BinaryOpUGen(MULTIPLICATION).ar[0]

        ..  container:: example

            A factory configured with a crossfaded *and* windowed bus output
            will use the windowing signal to control the crossfade:

            ::

                >>> factory = factory.with_output(
                ...     crossfaded=True,
                ...     windowed=True,
                ...     )
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: ab4814d778db920cd705270a3667580b
                    ugens:
                    -   Control.ir: null
                    -   Line.kr:
                            done_action: 2.0
                            duration: Control.ir[0:duration]
                            start: 0.0
                            stop: 1.0
                    -   UnaryOpUGen(HANNING_WINDOW).kr:
                            source: Line.kr[0]
                    -   In.ar:
                            bus: Control.ir[1:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   XOut.ar:
                            bus: Control.ir[1:out]
                            crossfade: UnaryOpUGen(HANNING_WINDOW).kr[0]
                            source[0]: AllpassC.ar/1[0]

        ..  container:: example

            A level-control can be combined with the windowing and crossfading:

            ::

                >>> factory = factory.with_output(
                ...     crossfaded=True,
                ...     leveled=True,
                ...     windowed=True,
                ...     )
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 6c7d16a174a3b8b2fc3fdbf989978553
                    ugens:
                    -   Control.ir: null
                    -   Line.kr:
                            done_action: 2.0
                            duration: Control.ir[0:duration]
                            start: 0.0
                            stop: 1.0
                    -   UnaryOpUGen(HANNING_WINDOW).kr:
                            source: Line.kr[0]
                    -   In.ar:
                            bus: Control.ir[1:out]
                    -   Control.kr: null
                    -   BinaryOpUGen(MULTIPLICATION).kr:
                            left: UnaryOpUGen(HANNING_WINDOW).kr[0]
                            right: Control.kr[0:level]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   XOut.ar:
                            bus: Control.ir[1:out]
                            crossfade: BinaryOpUGen(MULTIPLICATION).kr[0]
                            source[0]: AllpassC.ar/1[0]

        ..  container:: example

            A factory configured with both a windowed bus input and output will
            re-use the windowing signal:

            ::

                >>> factory = factory.with_input(windowed=True)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: ee9b6124f194df8c11034f734cfae051
                    ugens:
                    -   Control.ir: null
                    -   Line.kr:
                            done_action: 2.0
                            duration: Control.ir[0:duration]
                            start: 0.0
                            stop: 1.0
                    -   UnaryOpUGen(HANNING_WINDOW).kr:
                            source: Line.kr[0]
                    -   In.ar:
                            bus: Control.ir[1:out]
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: In.ar[0]
                            right: UnaryOpUGen(HANNING_WINDOW).kr[0]
                    -   Control.kr: null
                    -   BinaryOpUGen(MULTIPLICATION).kr:
                            left: UnaryOpUGen(HANNING_WINDOW).kr[0]
                            right: Control.kr[0:level]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: BinaryOpUGen(MULTIPLICATION).ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   XOut.ar:
                            bus: Control.ir[1:out]
                            crossfade: BinaryOpUGen(MULTIPLICATION).kr[0]
                            source[0]: AllpassC.ar/1[0]

        """
        assert not (replacing and crossfaded)
        clone = self._clone()
        clone._output.update(
            crossfaded=bool(crossfaded),
            leveled=bool(leveled),
            replacing=bool(replacing),
            windowed=bool(windowed),
            )
        return clone

    def with_parameter_block(self, block_function):
        """
        Return a new factory configured with a parameter block function.

        Use parameter block functions to build repetitive sets of SynthDef
        parameters, e.g. each set of band parameters for a multi-band
        compressor.

        Parameter block functions take two parameters:

        builder
            the SynthDef builder instance

        state
            a dictionary of arbitrary key/value pairs for parameterizing the
            signal and parameter block functions

        The return values of parameter block functions are ignored.

        ..  container:: example

            A factory configured to build multi-band compressor SynthDefs,
            using frequency bands split at ``frequencies``:

            ::

                >>> def parameter_block(builder, state):
                ...     frequencies = state['frequencies']
                ...     band_count = len(frequencies) + 1
                ...     for i in range(band_count):
                ...         band_name = 'band_{}_'.format(i + 1)
                ...         builder._add_parameter(band_name + 'pregain', 0)
                ...         builder._add_parameter(band_name + 'clamp_time', 0.01)
                ...         builder._add_parameter(band_name + 'relax_time', 0.1)
                ...         builder._add_parameter(band_name + 'threshold', -6)
                ...         builder._add_parameter(band_name + 'slope_above', 0.5)
                ...         builder._add_parameter(band_name + 'slope_below', 1.0)
                ...         builder._add_parameter(band_name + 'postgain', 0)

            ::

                >>> def signal_block(builder, source, state):
                ...     bands = []
                ...     frequencies = state['frequencies']
                ...     for frequency in frequencies:
                ...         band = supriya.ugens.LPF.ar(source=source, frequency=frequency)
                ...         bands.append(band)
                ...         source -= band
                ...     bands.append(source)
                ...     compressors = []
                ...     for i, band in enumerate(bands):
                ...         band_name = 'band_{}_'.format(i + 1)
                ...         band *= builder[band_name + 'pregain'].db_to_amplitude()
                ...         band = supriya.ugens.CompanderD.ar(
                ...             source=band,
                ...             clamp_time=builder[band_name + 'clamp_time'],
                ...             relax_time=builder[band_name + 'relax_time'],
                ...             slope_above=builder[band_name + 'slope_above'],
                ...             slope_below=builder[band_name + 'slope_below'],
                ...             threshold=builder[band_name + 'threshold'].db_to_amplitude(),
                ...             )
                ...         band *= builder[band_name + 'postgain'].db_to_amplitude()
                ...         compressors.extend(band)
                ...     source = supriya.ugens.Mix.multichannel(
                ...         compressors,
                ...         state['channel_count'],
                ...         )
                ...     return source

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()
                >>> factory = factory.with_initial_state(frequencies=(300, 1200, 9600))
                >>> factory = factory.with_parameter_block(parameter_block)
                >>> factory = factory.with_input()
                >>> factory = factory.with_signal_block(signal_block)
                >>> factory = factory.with_output(crossfaded=True)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 05302097b47611a26cb99c052708d21b
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   LPF.ar/0:
                            frequency: 300.0
                            source: In.ar[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/0:
                            left: In.ar[0]
                            right: LPF.ar/0[0]
                    -   LPF.ar/1:
                            frequency: 1200.0
                            source: BinaryOpUGen(SUBTRACTION).ar/0[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/1:
                            left: BinaryOpUGen(SUBTRACTION).ar/0[0]
                            right: LPF.ar/1[0]
                    -   LPF.ar/2:
                            frequency: 9600.0
                            source: BinaryOpUGen(SUBTRACTION).ar/1[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/2:
                            left: BinaryOpUGen(SUBTRACTION).ar/1[0]
                            right: LPF.ar/2[0]
                    -   Control.kr: null
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/0:
                            source: Control.kr[2:band_1_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/0:
                            left: LPF.ar/0[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/0[0]
                    -   DelayN.ar/0:
                            delay_time: Control.kr[0:band_1_clamp_time]
                            maximum_delay_time: Control.kr[0:band_1_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/0[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/1:
                            source: Control.kr[6:band_1_threshold]
                    -   Compander.ar/0:
                            clamp_time: Control.kr[0:band_1_clamp_time]
                            control: DelayN.ar/0[0]
                            relax_time: Control.kr[3:band_1_relax_time]
                            slope_above: Control.kr[4:band_1_slope_above]
                            slope_below: Control.kr[5:band_1_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/0[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/1[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/2:
                            source: Control.kr[1:band_1_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/1:
                            left: Compander.ar/0[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/2[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/3:
                            source: Control.kr[9:band_2_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/2:
                            left: LPF.ar/1[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/3[0]
                    -   DelayN.ar/1:
                            delay_time: Control.kr[7:band_2_clamp_time]
                            maximum_delay_time: Control.kr[7:band_2_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/2[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/4:
                            source: Control.kr[13:band_2_threshold]
                    -   Compander.ar/1:
                            clamp_time: Control.kr[7:band_2_clamp_time]
                            control: DelayN.ar/1[0]
                            relax_time: Control.kr[10:band_2_relax_time]
                            slope_above: Control.kr[11:band_2_slope_above]
                            slope_below: Control.kr[12:band_2_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/2[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/4[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/5:
                            source: Control.kr[8:band_2_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/3:
                            left: Compander.ar/1[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/5[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/6:
                            source: Control.kr[16:band_3_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/4:
                            left: LPF.ar/2[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/6[0]
                    -   DelayN.ar/2:
                            delay_time: Control.kr[14:band_3_clamp_time]
                            maximum_delay_time: Control.kr[14:band_3_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/4[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/7:
                            source: Control.kr[20:band_3_threshold]
                    -   Compander.ar/2:
                            clamp_time: Control.kr[14:band_3_clamp_time]
                            control: DelayN.ar/2[0]
                            relax_time: Control.kr[17:band_3_relax_time]
                            slope_above: Control.kr[18:band_3_slope_above]
                            slope_below: Control.kr[19:band_3_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/4[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/7[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/8:
                            source: Control.kr[15:band_3_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/5:
                            left: Compander.ar/2[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/8[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/9:
                            source: Control.kr[23:band_4_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/6:
                            left: BinaryOpUGen(SUBTRACTION).ar/2[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/9[0]
                    -   DelayN.ar/3:
                            delay_time: Control.kr[21:band_4_clamp_time]
                            maximum_delay_time: Control.kr[21:band_4_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/6[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/10:
                            source: Control.kr[27:band_4_threshold]
                    -   Compander.ar/3:
                            clamp_time: Control.kr[21:band_4_clamp_time]
                            control: DelayN.ar/3[0]
                            relax_time: Control.kr[24:band_4_relax_time]
                            slope_above: Control.kr[25:band_4_slope_above]
                            slope_below: Control.kr[26:band_4_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/6[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/10[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/11:
                            source: Control.kr[22:band_4_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/7:
                            left: Compander.ar/3[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/11[0]
                    -   Sum4.ar:
                            input_four: BinaryOpUGen(MULTIPLICATION).ar/7[0]
                            input_one: BinaryOpUGen(MULTIPLICATION).ar/1[0]
                            input_three: BinaryOpUGen(MULTIPLICATION).ar/5[0]
                            input_two: BinaryOpUGen(MULTIPLICATION).ar/3[0]
                    -   XOut.ar:
                            bus: Control.ir[0:out]
                            crossfade: Control.kr[28:crossfade]
                            source[0]: Sum4.ar[0]

        ..  container:: example

            The above factory can be parameterized to use smaller or larger
            numbers of bands during the build stage:

            ::

                >>> frequencies = (150, 300, 600, 1200, 2400, 4800, 9600)
                >>> synthdef = factory.build(frequencies=frequencies)
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 01601b63f9fe591dd0711d083a3343a7
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   LPF.ar/0:
                            frequency: 150.0
                            source: In.ar[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/0:
                            left: In.ar[0]
                            right: LPF.ar/0[0]
                    -   LPF.ar/1:
                            frequency: 300.0
                            source: BinaryOpUGen(SUBTRACTION).ar/0[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/1:
                            left: BinaryOpUGen(SUBTRACTION).ar/0[0]
                            right: LPF.ar/1[0]
                    -   LPF.ar/2:
                            frequency: 600.0
                            source: BinaryOpUGen(SUBTRACTION).ar/1[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/2:
                            left: BinaryOpUGen(SUBTRACTION).ar/1[0]
                            right: LPF.ar/2[0]
                    -   LPF.ar/3:
                            frequency: 1200.0
                            source: BinaryOpUGen(SUBTRACTION).ar/2[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/3:
                            left: BinaryOpUGen(SUBTRACTION).ar/2[0]
                            right: LPF.ar/3[0]
                    -   LPF.ar/4:
                            frequency: 2400.0
                            source: BinaryOpUGen(SUBTRACTION).ar/3[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/4:
                            left: BinaryOpUGen(SUBTRACTION).ar/3[0]
                            right: LPF.ar/4[0]
                    -   LPF.ar/5:
                            frequency: 4800.0
                            source: BinaryOpUGen(SUBTRACTION).ar/4[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/5:
                            left: BinaryOpUGen(SUBTRACTION).ar/4[0]
                            right: LPF.ar/5[0]
                    -   LPF.ar/6:
                            frequency: 9600.0
                            source: BinaryOpUGen(SUBTRACTION).ar/5[0]
                    -   BinaryOpUGen(SUBTRACTION).ar/6:
                            left: BinaryOpUGen(SUBTRACTION).ar/5[0]
                            right: LPF.ar/6[0]
                    -   Control.kr: null
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/0:
                            source: Control.kr[2:band_1_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/0:
                            left: LPF.ar/0[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/0[0]
                    -   DelayN.ar/0:
                            delay_time: Control.kr[0:band_1_clamp_time]
                            maximum_delay_time: Control.kr[0:band_1_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/0[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/1:
                            source: Control.kr[6:band_1_threshold]
                    -   Compander.ar/0:
                            clamp_time: Control.kr[0:band_1_clamp_time]
                            control: DelayN.ar/0[0]
                            relax_time: Control.kr[3:band_1_relax_time]
                            slope_above: Control.kr[4:band_1_slope_above]
                            slope_below: Control.kr[5:band_1_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/0[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/1[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/2:
                            source: Control.kr[1:band_1_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/1:
                            left: Compander.ar/0[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/2[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/3:
                            source: Control.kr[9:band_2_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/2:
                            left: LPF.ar/1[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/3[0]
                    -   DelayN.ar/1:
                            delay_time: Control.kr[7:band_2_clamp_time]
                            maximum_delay_time: Control.kr[7:band_2_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/2[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/4:
                            source: Control.kr[13:band_2_threshold]
                    -   Compander.ar/1:
                            clamp_time: Control.kr[7:band_2_clamp_time]
                            control: DelayN.ar/1[0]
                            relax_time: Control.kr[10:band_2_relax_time]
                            slope_above: Control.kr[11:band_2_slope_above]
                            slope_below: Control.kr[12:band_2_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/2[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/4[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/5:
                            source: Control.kr[8:band_2_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/3:
                            left: Compander.ar/1[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/5[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/6:
                            source: Control.kr[16:band_3_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/4:
                            left: LPF.ar/2[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/6[0]
                    -   DelayN.ar/2:
                            delay_time: Control.kr[14:band_3_clamp_time]
                            maximum_delay_time: Control.kr[14:band_3_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/4[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/7:
                            source: Control.kr[20:band_3_threshold]
                    -   Compander.ar/2:
                            clamp_time: Control.kr[14:band_3_clamp_time]
                            control: DelayN.ar/2[0]
                            relax_time: Control.kr[17:band_3_relax_time]
                            slope_above: Control.kr[18:band_3_slope_above]
                            slope_below: Control.kr[19:band_3_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/4[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/7[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/8:
                            source: Control.kr[15:band_3_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/5:
                            left: Compander.ar/2[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/8[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/9:
                            source: Control.kr[23:band_4_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/6:
                            left: LPF.ar/3[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/9[0]
                    -   DelayN.ar/3:
                            delay_time: Control.kr[21:band_4_clamp_time]
                            maximum_delay_time: Control.kr[21:band_4_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/6[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/10:
                            source: Control.kr[27:band_4_threshold]
                    -   Compander.ar/3:
                            clamp_time: Control.kr[21:band_4_clamp_time]
                            control: DelayN.ar/3[0]
                            relax_time: Control.kr[24:band_4_relax_time]
                            slope_above: Control.kr[25:band_4_slope_above]
                            slope_below: Control.kr[26:band_4_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/6[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/10[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/11:
                            source: Control.kr[22:band_4_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/7:
                            left: Compander.ar/3[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/11[0]
                    -   Sum4.ar/0:
                            input_four: BinaryOpUGen(MULTIPLICATION).ar/7[0]
                            input_one: BinaryOpUGen(MULTIPLICATION).ar/1[0]
                            input_three: BinaryOpUGen(MULTIPLICATION).ar/5[0]
                            input_two: BinaryOpUGen(MULTIPLICATION).ar/3[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/12:
                            source: Control.kr[30:band_5_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/8:
                            left: LPF.ar/4[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/12[0]
                    -   DelayN.ar/4:
                            delay_time: Control.kr[28:band_5_clamp_time]
                            maximum_delay_time: Control.kr[28:band_5_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/8[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/13:
                            source: Control.kr[34:band_5_threshold]
                    -   Compander.ar/4:
                            clamp_time: Control.kr[28:band_5_clamp_time]
                            control: DelayN.ar/4[0]
                            relax_time: Control.kr[31:band_5_relax_time]
                            slope_above: Control.kr[32:band_5_slope_above]
                            slope_below: Control.kr[33:band_5_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/8[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/13[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/14:
                            source: Control.kr[29:band_5_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/9:
                            left: Compander.ar/4[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/14[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/15:
                            source: Control.kr[37:band_6_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/10:
                            left: LPF.ar/5[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/15[0]
                    -   DelayN.ar/5:
                            delay_time: Control.kr[35:band_6_clamp_time]
                            maximum_delay_time: Control.kr[35:band_6_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/10[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/16:
                            source: Control.kr[41:band_6_threshold]
                    -   Compander.ar/5:
                            clamp_time: Control.kr[35:band_6_clamp_time]
                            control: DelayN.ar/5[0]
                            relax_time: Control.kr[38:band_6_relax_time]
                            slope_above: Control.kr[39:band_6_slope_above]
                            slope_below: Control.kr[40:band_6_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/10[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/16[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/17:
                            source: Control.kr[36:band_6_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/11:
                            left: Compander.ar/5[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/17[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/18:
                            source: Control.kr[44:band_7_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/12:
                            left: LPF.ar/6[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/18[0]
                    -   DelayN.ar/6:
                            delay_time: Control.kr[42:band_7_clamp_time]
                            maximum_delay_time: Control.kr[42:band_7_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/12[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/19:
                            source: Control.kr[48:band_7_threshold]
                    -   Compander.ar/6:
                            clamp_time: Control.kr[42:band_7_clamp_time]
                            control: DelayN.ar/6[0]
                            relax_time: Control.kr[45:band_7_relax_time]
                            slope_above: Control.kr[46:band_7_slope_above]
                            slope_below: Control.kr[47:band_7_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/12[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/19[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/20:
                            source: Control.kr[43:band_7_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/13:
                            left: Compander.ar/6[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/20[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/21:
                            source: Control.kr[51:band_8_pregain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/14:
                            left: BinaryOpUGen(SUBTRACTION).ar/6[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/21[0]
                    -   DelayN.ar/7:
                            delay_time: Control.kr[49:band_8_clamp_time]
                            maximum_delay_time: Control.kr[49:band_8_clamp_time]
                            source: BinaryOpUGen(MULTIPLICATION).ar/14[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/22:
                            source: Control.kr[55:band_8_threshold]
                    -   Compander.ar/7:
                            clamp_time: Control.kr[49:band_8_clamp_time]
                            control: DelayN.ar/7[0]
                            relax_time: Control.kr[52:band_8_relax_time]
                            slope_above: Control.kr[53:band_8_slope_above]
                            slope_below: Control.kr[54:band_8_slope_below]
                            source: BinaryOpUGen(MULTIPLICATION).ar/14[0]
                            threshold: UnaryOpUGen(DB_TO_AMPLITUDE).kr/22[0]
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).kr/23:
                            source: Control.kr[50:band_8_postgain]
                    -   BinaryOpUGen(MULTIPLICATION).ar/15:
                            left: Compander.ar/7[0]
                            right: UnaryOpUGen(DB_TO_AMPLITUDE).kr/23[0]
                    -   Sum4.ar/1:
                            input_four: BinaryOpUGen(MULTIPLICATION).ar/15[0]
                            input_one: BinaryOpUGen(MULTIPLICATION).ar/9[0]
                            input_three: BinaryOpUGen(MULTIPLICATION).ar/13[0]
                            input_two: BinaryOpUGen(MULTIPLICATION).ar/11[0]
                    -   BinaryOpUGen(ADDITION).ar:
                            left: Sum4.ar/0[0]
                            right: Sum4.ar/1[0]
                    -   XOut.ar:
                            bus: Control.ir[0:out]
                            crossfade: Control.kr[56:crossfade]
                            source[0]: BinaryOpUGen(ADDITION).ar[0]

        """
        clone = self._clone()
        clone._parameter_blocks.append(block_function)
        return clone

    def with_rand_id(self, rand_id=0):
        """
        Return a new factory configured with a random number generator ID.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_input()
                >>> factory = factory.with_output()
                >>> factory = factory.with_signal_block(signal_block)

        ..  container:: example

            Configure the factory with a random number generator ID, defaulting
            to 23:

            ::

                >>> factory = factory.with_rand_id(rand_id=23)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 71b359ac47a02b833c16587c3b7030d1
                    ugens:
                    -   Control.ir: null
                    -   RandID.ir:
                            rand_id: Control.ir[1:rand_id]
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/1[0]

        """
        clone = self._clone()
        if rand_id is not None:
            clone._rand_id = int(rand_id)
        else:
            clone._rand_id = None
        return clone

    def with_signal_block(self, block_function):
        """
        Return a new factory configured with an additional signal block
        function.

        Signal block functions take three parameters:

        builder
            the SynthDef builder instance

        source
            a UGenMethodMixin representing the signal flow

        state
            a dictionary of arbitrary key/value pairs for parameterizing the
            signal and parameter block functions

        Signal block functions should return a UGenMethodMixin.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_input()
                >>> factory = factory.with_output()
                >>> factory = factory.with_signal_block(signal_block)

        ..  container:: example

            Configure the factory with an additional signal block:

            ::

                >>> def signal_block_post(builder, source, state):
                ...     source = supriya.ugens.LeakDC.ar(source=source)
                ...     source = supriya.ugens.Limiter.ar(
                ...         duration=supriya.ugens.Rand.ir(0.005, 0.015),
                ...         source=source,
                ...         )
                ...     return source

            ::

                >>> factory = factory.with_signal_block(signal_block_post)
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: 6677f1ecc1b5477c33c91cc4ff752942
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   LeakDC.ar:
                            coefficient: 0.995
                            source: AllpassC.ar/1[0]
                    -   Rand.ir:
                            maximum: 0.015
                            minimum: 0.005
                    -   Limiter.ar:
                            duration: Rand.ir[0]
                            level: 1.0
                            source: LeakDC.ar[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: Limiter.ar[0]

        """
        clone = self._clone()
        clone._signal_blocks.append(block_function)
        return clone

    def with_silence_detection(self):
        """
        Return a new factory configured with silence detection.

        ..  container:: example

            ::

                >>> factory = supriya.synthdefs.SynthDefFactory()

            ::

                >>> def signal_block(builder, source, state):
                ...     iterations = state.get('iterations') or 2
                ...     for _ in range(iterations):
                ...         source = supriya.ugens.AllpassC.ar(
                ...             decay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             delay_time=supriya.ugens.ExpRand.ir(0.01, 0.1),
                ...             source=source,
                ...             maximum_delay_time=0.1,
                ...             )
                ...     return source

            ::

                >>> factory = factory.with_input()
                >>> factory = factory.with_output()
                >>> factory = factory.with_signal_block(signal_block)

        ..  container:: example

            Configure the factory with silence detection.

            ::

                >>> factory = factory.with_silence_detection()
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: a5db914f81bdc61c95dbeaa39c6e8a43
                    ugens:
                    -   Control.ir: null
                    -   In.ar:
                            bus: Control.ir[0:out]
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   Out.ar:
                            bus: Control.ir[0:out]
                            source[0]: AllpassC.ar/1[0]
                    -   DetectSilence.kr:
                            done_action: 2.0
                            source: AllpassC.ar/1[0]
                            threshold: 0.0001
                            time: 0.1

        ..  container:: example

            Silence detection is applied before any output leveling or
            windowing.

            ::

                >>> factory = factory.with_output(
                ...     leveled=True,
                ...     windowed=True,
                ...     )
                >>> synthdef = factory.build()
                >>> graph(synthdef)  # doctest: +SKIP

            ::

                >>> print(synthdef)
                synthdef:
                    name: d24f54c02874a1aafc1fdac685735d67
                    ugens:
                    -   Control.ir: null
                    -   Line.kr:
                            done_action: 2.0
                            duration: Control.ir[0:duration]
                            start: 0.0
                            stop: 1.0
                    -   UnaryOpUGen(HANNING_WINDOW).kr:
                            source: Line.kr[0]
                    -   In.ar:
                            bus: Control.ir[1:out]
                    -   Control.kr: null
                    -   ExpRand.ir/0:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/1:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/0:
                            decay_time: ExpRand.ir/0[0]
                            delay_time: ExpRand.ir/1[0]
                            maximum_delay_time: 0.1
                            source: In.ar[0]
                    -   ExpRand.ir/2:
                            maximum: 0.01
                            minimum: 0.1
                    -   ExpRand.ir/3:
                            maximum: 0.01
                            minimum: 0.1
                    -   AllpassC.ar/1:
                            decay_time: ExpRand.ir/2[0]
                            delay_time: ExpRand.ir/3[0]
                            maximum_delay_time: 0.1
                            source: AllpassC.ar/0[0]
                    -   BinaryOpUGen(MULTIPLICATION).ar/0:
                            left: AllpassC.ar/1[0]
                            right: Control.kr[0:level]
                    -   BinaryOpUGen(MULTIPLICATION).ar/1:
                            left: BinaryOpUGen(MULTIPLICATION).ar/0[0]
                            right: UnaryOpUGen(HANNING_WINDOW).kr[0]
                    -   Out.ar:
                            bus: Control.ir[1:out]
                            source[0]: BinaryOpUGen(MULTIPLICATION).ar/1[0]
                    -   DetectSilence.kr:
                            done_action: 2.0
                            source: AllpassC.ar/1[0]
                            threshold: 0.0001
                            time: 0.1

        """
        clone = self._clone()
        clone._silence_detection = True
        return clone
