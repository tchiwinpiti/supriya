from supriya.ugens.PV_ChainUGen import PV_ChainUGen


class PV_MagDiv(PV_ChainUGen):
    """
    Divides magnitudes.

    ::

        >>> pv_chain_a = supriya.ugens.FFT(
        ...     source=supriya.ugens.WhiteNoise.ar(),
        ...     )
        >>> pv_chain_b = supriya.ugens.FFT(
        ...     source=supriya.ugens.LFSaw.ar(),
        ...     )
        >>> pv_mag_div = supriya.ugens.PV_MagDiv(
        ...     pv_chain_a=pv_chain_a,
        ...     pv_chain_b=pv_chain_b,
        ...     zeroed=0.0001,
        ...     )
        >>> pv_mag_div
        PV_MagDiv.kr()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'FFT UGens'

    __slots__ = ()

    _ordered_input_names = (
        'pv_chain_a',
        'pv_chain_b',
        'zeroed',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pv_chain_a=None,
        pv_chain_b=None,
        zeroed=0.0001,
        ):
        PV_ChainUGen.__init__(
            self,
            pv_chain_a=pv_chain_a,
            pv_chain_b=pv_chain_b,
            zeroed=zeroed,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        pv_chain_a=None,
        pv_chain_b=None,
        zeroed=0.0001,
        ):
        """
        Constructs a PV_MagDiv.

        ::

            >>> pv_chain_a = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = supriya.ugens.FFT(
            ...     source=supriya.ugens.LFSaw.ar(),
            ...     )
            >>> pv_mag_div = supriya.ugens.PV_MagDiv.new(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     zeroed=0.0001,
            ...     )
            >>> pv_mag_div
            PV_MagDiv.kr()

        Returns ugen graph.
        """
        ugen = cls._new_expanded(
            pv_chain_a=pv_chain_a,
            pv_chain_b=pv_chain_b,
            zeroed=zeroed,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def pv_chain_a(self):
        """
        Gets `pv_chain_a` input of PV_MagDiv.

        ::

            >>> pv_chain_a = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = supriya.ugens.FFT(
            ...     source=supriya.ugens.LFSaw.ar(),
            ...     )
            >>> pv_mag_div = supriya.ugens.PV_MagDiv(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     zeroed=0.0001,
            ...     )
            >>> pv_mag_div.pv_chain_a
            FFT.kr()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('pv_chain_a')
        return self._inputs[index]

    @property
    def pv_chain_b(self):
        """
        Gets `pv_chain_b` input of PV_MagDiv.

        ::

            >>> pv_chain_a = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = supriya.ugens.FFT(
            ...     source=supriya.ugens.LFSaw.ar(),
            ...     )
            >>> pv_mag_div = supriya.ugens.PV_MagDiv(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     zeroed=0.0001,
            ...     )
            >>> pv_mag_div.pv_chain_b
            FFT.kr()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('pv_chain_b')
        return self._inputs[index]

    @property
    def zeroed(self):
        """
        Gets `zeroed` input of PV_MagDiv.

        ::

            >>> pv_chain_a = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = supriya.ugens.FFT(
            ...     source=supriya.ugens.LFSaw.ar(),
            ...     )
            >>> pv_mag_div = supriya.ugens.PV_MagDiv(
            ...     pv_chain_a=pv_chain_b,
            ...     pv_chain_b=pv_chain_a,
            ...     zeroed=0.0001,
            ...     )
            >>> pv_mag_div.zeroed
            0.0001

        Returns ugen input.
        """
        index = self._ordered_input_names.index('zeroed')
        return self._inputs[index]
