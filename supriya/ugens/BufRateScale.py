from supriya.ugens.BufInfoUGenBase import BufInfoUGenBase


class BufRateScale(BufInfoUGenBase):
    """
    A buffer sample-rate scale info unit generator.

    ::

        >>> supriya.ugens.BufRateScale.kr(buffer_id=0)
        BufRateScale.kr()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Buffer UGens'

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        buffer_id=None,
        calculation_rate=None,
        ):
        BufInfoUGenBase.__init__(
            self,
            buffer_id=buffer_id,
            calculation_rate=calculation_rate,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        """
        Gets `buffer_id` input of BufRateScale.

        ::

            >>> buffer_id = 23
            >>> buf_rate_scale = supriya.ugens.BufRateScale.kr(
            ...     buffer_id=buffer_id,
            ...     )
            >>> buf_rate_scale.buffer_id
            23.0

        Returns input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]
