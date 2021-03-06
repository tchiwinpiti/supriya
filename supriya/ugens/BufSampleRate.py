from supriya.ugens.BufInfoUGenBase import BufInfoUGenBase


class BufSampleRate(BufInfoUGenBase):
    """
    A buffer sample-rate info unit generator.

    ::

        >>> supriya.ugens.BufSampleRate.kr(buffer_id=0)
        BufSampleRate.kr()

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
        Gets `buffer_id` input of BufSampleRate.

        ::

            >>> buffer_id = 23
            >>> buf_sample_rate = supriya.ugens.BufSampleRate.kr(
            ...     buffer_id=buffer_id,
            ...     )
            >>> buf_sample_rate.buffer_id
            23.0

        Returns input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]
