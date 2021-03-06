from supriya.ugens.UGen import UGen


class Line(UGen):
    """
    A line generating unit generator.

    ::

        >>> supriya.ugens.Line.ar()
        Line.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Line Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'start',
        'stop',
        'duration',
        'done_action',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        done_action=0.,
        duration=1.,
        start=0.,
        stop=1.,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            start=start,
            stop=stop,
            )

    ### PRIVATE METHODS ###

    @classmethod
    def _new_expanded(
        cls,
        calculation_rate=None,
        done_action=None,
        duration=None,
        stop=None,
        start=None,
        ):
        import supriya.synthdefs
        done_action = supriya.synthdefs.DoneAction.from_expr(done_action)
        return super(Line, cls)._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            stop=stop,
            start=start,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        done_action=0,
        duration=1,
        stop=1,
        start=0,
        ):
        """
        Constructs an audio-rate line generator.

        ::

            >>> supriya.ugens.Line.ar(
            ...     done_action=supriya.synthdefs.DoneAction.FREE_SYNTH,
            ...     duration=5.5,
            ...     stop=12.1,
            ...     start=0.1,
            ...     )
            Line.ar()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        return cls._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            stop=stop,
            start=start,
            )

    @classmethod
    def kr(
        cls,
        done_action=0,
        duration=1,
        stop=1,
        start=0,
        ):
        """
        Constructs an audio-rate line generator.

        ::

            >>> supriya.ugens.Line.kr(
            ...     done_action=supriya.synthdefs.DoneAction.FREE_SYNTH,
            ...     duration=5.5,
            ...     stop=12.1,
            ...     start=0.1,
            ...     )
            Line.kr()

        Returns unit generator graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.CONTROL
        return cls._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            stop=stop,
            start=start,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def done_action(self):
        """
        Gets `done_action` input of Line.

        ::

            >>> done_action = 0
            >>> line = supriya.ugens.Line.ar(
            ...     done_action=done_action,
            ...     )
            >>> line.done_action
            0.0

        Returns input.
        """
        index = self._ordered_input_names.index('done_action')
        return self._inputs[index]

    @property
    def duration(self):
        """
        Gets `duration` input of Line.

        ::

            >>> duration = 5.5
            >>> line = supriya.ugens.Line.ar(
            ...     duration=duration,
            ...     )
            >>> line.duration
            5.5

        Returns input.
        """
        index = self._ordered_input_names.index('duration')
        return self._inputs[index]

    @property
    def has_done_flag(self):
        """
        Is true if UGen has a done flag.

        Returns boolean.
        """
        return True

    @property
    def start(self):
        """
        Gets `start` input of Line.

        ::

            >>> start = 0.1
            >>> line = supriya.ugens.Line.ar(
            ...     start=start,
            ...     )
            >>> line.start
            0.1

        Returns input.
        """
        index = self._ordered_input_names.index('start')
        return self._inputs[index]

    @property
    def stop(self):
        """
        Gets `stop` input of Line.

        ::

            >>> stop = 12.1
            >>> line = supriya.ugens.Line.ar(
            ...     stop=stop,
            ...     )
            >>> line.stop
            12.1

        Returns input.
        """
        index = self._ordered_input_names.index('stop')
        return self._inputs[index]
