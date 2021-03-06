from supriya.ugens.DUGen import DUGen


class Dseries(DUGen):
    """
    A demand-rate arithmetic series.

    ::

        >>> dseries = supriya.ugens.Dseries.new(
        ...     length=float('inf'),
        ...     start=1,
        ...     step=1,
        ...     )
        >>> dseries
        Dseries()

    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    _ordered_input_names = (
        'start',
        'step',
        'length',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        length=float('inf'),
        start=1,
        step=1,
        ):
        if length is None:
            length = float('inf')
        DUGen.__init__(
            self,
            length=length,
            start=start,
            step=step,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        length=float('inf'),
        start=1,
        step=1,
        ):
        """
        Constructs a Dseries.

        ::

            >>> dseries = supriya.ugens.Dseries.new(
            ...     length=float('inf'),
            ...     start=1,
            ...     step=1,
            ...     )
            >>> dseries
            Dseries()

        Returns ugen graph.
        """
        ugen = cls._new_expanded(
            length=length,
            start=start,
            step=step,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def length(self):
        """
        Gets `length` input of Dseries.

        ::

            >>> dseries = supriya.ugens.Dseries.new(
            ...     length=float('inf'),
            ...     start=1,
            ...     step=1,
            ...     )
            >>> dseries.length
            inf

        Returns ugen input.
        """
        index = self._ordered_input_names.index('length')
        return self._inputs[index]

    @property
    def start(self):
        """
        Gets `start` input of Dseries.

        ::

            >>> dseries = supriya.ugens.Dseries.new(
            ...     length=float('inf'),
            ...     start=1,
            ...     step=1,
            ...     )
            >>> dseries.start
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('start')
        return self._inputs[index]

    @property
    def step(self):
        """
        Gets `step` input of Dseries.

        ::

            >>> dseries = supriya.ugens.Dseries.new(
            ...     length=float('inf'),
            ...     start=1,
            ...     step=1,
            ...     )
            >>> dseries.step
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('step')
        return self._inputs[index]
