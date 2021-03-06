from supriya.ugens.PV_ChainUGen import PV_ChainUGen


class PV_MagShift(PV_ChainUGen):
    """
    Shifts and stretches magnitude bin position.

    ::

        >>> pv_chain = supriya.ugens.FFT(
        ...     source=supriya.ugens.WhiteNoise.ar(),
        ...     )
        >>> pv_mag_shift = supriya.ugens.PV_MagShift(
        ...     pv_chain=pv_chain,
        ...     shift=0,
        ...     stretch=1,
        ...     )
        >>> pv_mag_shift
        PV_MagShift.kr()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'FFT UGens'

    __slots__ = ()

    _ordered_input_names = (
        'pv_chain',
        'stretch',
        'shift',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pv_chain=None,
        shift=0,
        stretch=1,
        ):
        PV_ChainUGen.__init__(
            self,
            pv_chain=pv_chain,
            shift=shift,
            stretch=stretch,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        pv_chain=None,
        shift=0,
        stretch=1,
        ):
        """
        Constructs a PV_MagShift.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_mag_shift = supriya.ugens.PV_MagShift.new(
            ...     pv_chain=pv_chain,
            ...     shift=0,
            ...     stretch=1,
            ...     )
            >>> pv_mag_shift
            PV_MagShift.kr()

        Returns ugen graph.
        """
        ugen = cls._new_expanded(
            pv_chain=pv_chain,
            shift=shift,
            stretch=stretch,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def pv_chain(self):
        """
        Gets `pv_chain` input of PV_MagShift.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_mag_shift = supriya.ugens.PV_MagShift(
            ...     pv_chain=pv_chain,
            ...     shift=0,
            ...     stretch=1,
            ...     )
            >>> pv_mag_shift.pv_chain
            FFT.kr()[0]

        Returns ugen input.
        """
        index = self._ordered_input_names.index('pv_chain')
        return self._inputs[index]

    @property
    def shift(self):
        """
        Gets `shift` input of PV_MagShift.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_mag_shift = supriya.ugens.PV_MagShift(
            ...     pv_chain=pv_chain,
            ...     shift=0,
            ...     stretch=1,
            ...     )
            >>> pv_mag_shift.shift
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('shift')
        return self._inputs[index]

    @property
    def stretch(self):
        """
        Gets `stretch` input of PV_MagShift.

        ::

            >>> pv_chain = supriya.ugens.FFT(
            ...     source=supriya.ugens.WhiteNoise.ar(),
            ...     )
            >>> pv_mag_shift = supriya.ugens.PV_MagShift(
            ...     pv_chain=pv_chain,
            ...     shift=0,
            ...     stretch=1,
            ...     )
            >>> pv_mag_shift.stretch
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('stretch')
        return self._inputs[index]
