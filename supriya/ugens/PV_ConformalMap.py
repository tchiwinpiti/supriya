from supriya.ugens.PV_ChainUGen import PV_ChainUGen


class PV_ConformalMap(PV_ChainUGen):
    """
    Complex plane attack.

    ::

        >>> pv_chain = supriya.ugens.FFT(
        ...     source=supriya.ugens.WhiteNoise.ar(),
        ...     )
        >>> pv_conformal_map = supriya.ugens.PV_ConformalMap(
        ...     aimag=0,
        ...     areal=0,
        ...     pv_chain=pv_chain,
        ...     )
        >>> pv_conformal_map
        PV_ConformalMap.kr()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'FFT UGens'

    __slots__ = ()

    _ordered_input_names = (
        'pv_chain',
        'areal',
        'aimag',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        aimag=0,
        areal=0,
        pv_chain=None,
        ):
        PV_ChainUGen.__init__(
            self,
            aimag=aimag,
            areal=areal,
            pv_chain=pv_chain,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        aimag=0,
        areal=0,
        pv_chain=None,
        ):
        """
        Constructs a PV_ConformalMap.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_conformal_map = supriya.ugens.PV_ConformalMap.new(
            ...     aimag=0,
            ...     areal=0,
            ...     pv_chain=pv_chain,
            ...     )
            >>> pv_conformal_map
            PV_ConformalMap.kr()

        Returns ugen graph.
        """
        ugen = cls._new_expanded(
            aimag=aimag,
            areal=areal,
            pv_chain=pv_chain,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def aimag(self):
        """
        Gets `aimag` input of PV_ConformalMap.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_conformal_map = supriya.ugens.PV_ConformalMap(
            ...     aimag=0,
            ...     areal=0,
            ...     pv_chain=pv_chain,
            ...     )
            >>> pv_conformal_map.aimag
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('aimag')
        return self._inputs[index]

    @property
    def areal(self):
        """
        Gets `areal` input of PV_ConformalMap.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_conformal_map = supriya.ugens.PV_ConformalMap(
            ...     aimag=0,
            ...     areal=0,
            ...     pv_chain=pv_chain,
            ...     )
            >>> pv_conformal_map.areal
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('areal')
        return self._inputs[index]

    @property
    def pv_chain(self):
        """
        Gets `pv_chain` input of PV_ConformalMap.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_conformal_map = supriya.ugens.PV_ConformalMap(
            ...     aimag=0,
            ...     areal=0,
            ...     pv_chain=pv_chain,
            ...     )
            >>> pv_conformal_map.pv_chain
            FFT.kr()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('pv_chain')
        return self._inputs[index]
