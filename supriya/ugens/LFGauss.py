from supriya.ugens.UGen import UGen


class LFGauss(UGen):
    """
    A non-band-limited gaussian function oscillator.

    ::

        >>> supriya.ugens.LFGauss.ar()
        LFGauss.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Oscillator UGens'

    __slots__ = ()

    _ordered_input_names = (
        'duration',
        'width',
        'initial_phase',
        'loop',
        'done_action',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        done_action=0,
        duration=1,
        initial_phase=0,
        loop=1,
        width=0.1,
        ):
        import supriya.synthdefs
        done_action = supriya.synthdefs.DoneAction.from_expr(done_action)
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            initial_phase=initial_phase,
            loop=loop,
            width=width,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        done_action=0,
        duration=1,
        initial_phase=0,
        loop=1,
        width=0.1,
        ):
        """
        Constructs an audio-rate non-band-limited gaussian function
        oscillator.

        ::

            >>> supriya.ugens.LFGauss.ar(
            ...     done_action=DoneAction.NOTHING,
            ...     duration=[1.0, 1.1],
            ...     initial_phase=0.0,
            ...     loop=True,
            ...     width=0.1,
            ...     )
            UGenArray({2})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            initial_phase=initial_phase,
            loop=loop,
            width=width,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        done_action=0,
        duration=1,
        initial_phase=0,
        loop=1,
        width=0.1,
        ):
        """
        Constructs a control-rate non-band-limited gaussian function
        oscillator.

        ::

            >>> supriya.ugens.LFGauss.kr(
            ...     done_action=DoneAction.NOTHING,
            ...     duration=[1.0, 1.1],
            ...     initial_phase=0.0,
            ...     loop=True,
            ...     width=0.1,
            ...     )
            UGenArray({2})

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            initial_phase=initial_phase,
            loop=loop,
            width=width,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def duration(self):
        """
        Gets `duration` input of LFSaw.

        ::

            >>> l_f_gauss = supriya.ugens.LFGauss.ar(
            ...     done_action=DoneAction.NOTHING,
            ...     duration=1.0,
            ...     initial_phase=0.0,
            ...     loop=True,
            ...     width=0.1,
            ...     )
            >>> l_f_gauss.duration
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('duration')
        return self._inputs[index]

    @property
    def done_action(self):
        """
        Gets `done_action` input of LFSaw.

        ::

            >>> l_f_gauss = supriya.ugens.LFGauss.ar(
            ...     done_action=DoneAction.NOTHING,
            ...     duration=1.0,
            ...     initial_phase=0.0,
            ...     loop=True,
            ...     width=0.1,
            ...     )
            >>> l_f_gauss.done_action
            0.0

        Returns input.
        """
        index = self._ordered_input_names.index('done_action')
        return self._inputs[index]

    @property
    def initial_phase(self):
        """
        Gets `initial_phase` input of LFSaw.

        ::

            >>> l_f_gauss = supriya.ugens.LFGauss.ar(
            ...     done_action=DoneAction.NOTHING,
            ...     duration=1.0,
            ...     initial_phase=0.0,
            ...     loop=True,
            ...     width=0.1,
            ...     )
            >>> l_f_gauss.initial_phase
            0.0

        Returns input.
        """
        index = self._ordered_input_names.index('initial_phase')
        return self._inputs[index]

    @property
    def loop(self):
        """
        Gets `loop` input of LFSaw.

        ::

            >>> l_f_gauss = supriya.ugens.LFGauss.ar(
            ...     done_action=DoneAction.NOTHING,
            ...     duration=1.0,
            ...     initial_phase=0.0,
            ...     loop=True,
            ...     width=0.1,
            ...     )
            >>> l_f_gauss.loop
            1.0

        Returns input.
        """
        index = self._ordered_input_names.index('loop')
        return self._inputs[index]

    @property
    def width(self):
        """
        Gets `width` input of LFSaw.

        ::

            >>> l_f_gauss = supriya.ugens.LFGauss.ar(
            ...     done_action=DoneAction.NOTHING,
            ...     duration=1.0,
            ...     initial_phase=0.0,
            ...     loop=True,
            ...     width=0.1,
            ...     )
            >>> l_f_gauss.width
            0.1

        Returns input.
        """
        index = self._ordered_input_names.index('width')
        return self._inputs[index]
