from supriya.ugens.PV_ChainUGen import PV_ChainUGen


class PV_MagSquared(PV_ChainUGen):
    """
    Squares magnitudes.

    ::

        >>> pv_chain = supriya.ugens.FFT(
        ...     source=supriya.ugens.WhiteNoise.ar(),
        ...     )
        >>> pv_mag_squared = supriya.ugens.PV_MagSquared(
        ...     pv_chain=pv_chain,
        ...     )
        >>> pv_mag_squared
        PV_MagSquared.kr()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'FFT UGens'

    __slots__ = ()

    _ordered_input_names = (
        'pv_chain',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pv_chain=None,
        ):
        PV_ChainUGen.__init__(
            self,
            pv_chain=pv_chain,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        pv_chain=None,
        ):
        """
        Constructs a PV_MagSquared.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_mag_squared = supriya.ugens.PV_MagSquared.new(
            ...     pv_chain=pv_chain,
            ...     )
            >>> pv_mag_squared
            PV_MagSquared.kr()

        Returns ugen graph.
        """
        ugen = cls._new_expanded(
            pv_chain=pv_chain,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def pv_chain(self):
        """
        Gets `pv_chain` input of PV_MagSquared.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_mag_squared = supriya.ugens.PV_MagSquared(
            ...     pv_chain=pv_chain,
            ...     )
            >>> pv_mag_squared.pv_chain
            FFT.kr()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('pv_chain')
        return self._inputs[index]
