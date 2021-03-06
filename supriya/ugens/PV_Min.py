from supriya.ugens.PV_ChainUGen import PV_ChainUGen


class PV_Min(PV_ChainUGen):
    """
    Minimum magnitude.

    ::

        >>> pv_chain_a = supriya.ugens.FFT(
        ...     source=supriya.ugens.WhiteNoise.ar(),
        ...     )
        >>> pv_chain_b = supriya.ugens.FFT(
        ...     source=supriya.ugens.LFSaw.ar(),
        ...     )
        >>> pv_min = supriya.ugens.PV_Min(
        ...     pv_chain_a=pv_chain_a,
        ...     pv_chain_b=pv_chain_b,
        ...     )
        >>> pv_min
        PV_Min.kr()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'FFT UGens'

    __slots__ = ()

    _ordered_input_names = (
        'pv_chain_a',
        'pv_chain_b',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pv_chain_a=None,
        pv_chain_b=None,
        ):
        PV_ChainUGen.__init__(
            self,
            pv_chain_a=pv_chain_a,
            pv_chain_b=pv_chain_b,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        pv_chain_a=None,
        pv_chain_b=None,
        ):
        """
        Constructs a PV_Min.

        ::

            >>> pv_chain_a = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = supriya.ugens.FFT(
            ...     source=supriya.ugens.LFSaw.ar(),
            ...     )
            >>> pv_min = supriya.ugens.PV_Min.new(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     )
            >>> pv_min
            PV_Min.kr()

        Returns ugen graph.
        """
        ugen = cls._new_expanded(
            pv_chain_a=pv_chain_a,
            pv_chain_b=pv_chain_b,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def pv_chain_a(self):
        """
        Gets `pv_chain_a` input of PV_Min.

        ::

            >>> pv_chain_a = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = supriya.ugens.FFT(
            ...     source=supriya.ugens.LFSaw.ar(),
            ...     )
            >>> pv_min = supriya.ugens.PV_Min(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     )
            >>> pv_min.pv_chain_a
            FFT.kr()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('pv_chain_a')
        return self._inputs[index]

    @property
    def pv_chain_b(self):
        """
        Gets `pv_chain_b` input of PV_Min.

        ::

            >>> pv_chain_a = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = supriya.ugens.FFT(
            ...     source=supriya.ugens.LFSaw.ar(),
            ...     )
            >>> pv_min = supriya.ugens.PV_Min(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     )
            >>> pv_min.pv_chain_b
            FFT.kr()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('pv_chain_b')
        return self._inputs[index]
