import collections
from supriya import utils
from supriya.synthdefs.CalculationRate import CalculationRate
from supriya.ugens.UGen import UGen


class Klank(UGen):
    """
    A bank of resonators.

    ::

        >>> frequencies = [200, 671, 1153, 1723]
        >>> amplitudes = None
        >>> decay_times = [1, 1, 1, 1]
        >>> specifications = [frequencies, amplitudes, decay_times]
        >>> source = supriya.ugens.BrownNoise.ar() * 0.001
        >>> klank = supriya.ugens.Klank.ar(
        ...     decay_scale=1,
        ...     frequency_offset=0,
        ...     frequency_scale=1,
        ...     source=source,
        ...     specifications=specifications,
        ...     )
        >>> klank
        Klank.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Filter UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'frequency_scale',
        'frequency_offset',
        'decay_scale',
        'specifications',
        )

    _unexpanded_input_names = (
        'specifications',
        )

    _valid_calculation_rates = (
        CalculationRate.AUDIO,
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        decay_scale=1,
        frequency_offset=0,
        frequency_scale=1,
        source=None,
        specifications=None,
        ):
        frequencies, amplitudes, decay_times = specifications
        assert len(frequencies)
        if not amplitudes:
            amplitudes = [1.0] * len(frequencies)
        elif not isinstance(amplitudes, collections.Sequence):
            amplitudes = [amplitudes] * len(frequencies)
        if not decay_times:
            decay_times = [1.0] * len(frequencies)
        elif not isinstance(decay_times, collections.Sequence):
            decay_times = [decay_times] * len(frequencies)
        specifications = utils.zip_sequences(
            frequencies, amplitudes, decay_times
            )
        specifications = utils.flatten_iterable(specifications)
        specifications = tuple(specifications)
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            decay_scale=decay_scale,
            frequency_offset=frequency_offset,
            frequency_scale=frequency_scale,
            source=source,
            specifications=specifications,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        decay_scale=1,
        frequency_offset=0,
        frequency_scale=1,
        source=None,
        specifications=None,
        ):
        """
        Constructs an audio-rate Klank.

        ::

            >>> source = supriya.ugens.BrownNoise.ar() * 0.001
            >>> frequencies = [200, 671, 1153, 1723]
            >>> amplitudes = None
            >>> decay_times = [1, 1, 1, 1]
            >>> specifications = [frequencies, amplitudes, decay_times]
            >>> klank = supriya.ugens.Klank.ar(
            ...     decay_scale=1,
            ...     frequency_offset=0,
            ...     frequency_scale=1,
            ...     source=source,
            ...     specifications=specifications,
            ...     )
            >>> klank
            Klank.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.synthdefs.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            decay_scale=decay_scale,
            frequency_offset=frequency_offset,
            frequency_scale=frequency_scale,
            source=source,
            specifications=specifications,
            )
        return ugen

    # def new1(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def decay_scale(self):
        """
        Gets `decay_scale` source of Klank.

        ::

            >>> frequencies = [200, 671, 1153, 1723]
            >>> amplitudes = None
            >>> decay_times = [1, 1, 1, 1]
            >>> specifications = [frequencies, amplitudes, decay_times]
            >>> source = supriya.ugens.BrownNoise.ar() * 0.001
            >>> klank = supriya.ugens.Klank.ar(
            ...     decay_scale=1,
            ...     frequency_offset=0,
            ...     frequency_scale=1,
            ...     source=source,
            ...     specifications=specifications,
            ...     )
            >>> klank.decay_scale
            1.0

        Returns ugen source.
        """
        index = self._ordered_input_names.index('decay_scale')
        return self._inputs[index]

    @property
    def frequency_offset(self):
        """
        Gets `frequency_offset` source of Klank.

        ::

            >>> frequencies = [200, 671, 1153, 1723]
            >>> amplitudes = None
            >>> decay_times = [1, 1, 1, 1]
            >>> specifications = [frequencies, amplitudes, decay_times]
            >>> source = supriya.ugens.BrownNoise.ar() * 0.001
            >>> klank = supriya.ugens.Klank.ar(
            ...     decay_scale=1,
            ...     frequency_offset=0,
            ...     frequency_scale=1,
            ...     source=source,
            ...     specifications=specifications,
            ...     )
            >>> klank.frequency_offset
            0.0

        Returns ugen source.
        """
        index = self._ordered_input_names.index('frequency_offset')
        return self._inputs[index]

    @property
    def frequency_scale(self):
        """
        Gets `frequency_scale` source of Klank.

        ::

            >>> frequencies = [200, 671, 1153, 1723]
            >>> amplitudes = None
            >>> decay_times = [1, 1, 1, 1]
            >>> specifications = [frequencies, amplitudes, decay_times]
            >>> source = supriya.ugens.BrownNoise.ar() * 0.001
            >>> klank = supriya.ugens.Klank.ar(
            ...     decay_scale=1,
            ...     frequency_offset=0,
            ...     frequency_scale=1,
            ...     source=source,
            ...     specifications=specifications,
            ...     )
            >>> klank.frequency_scale
            1.0

        Returns ugen source.
        """
        index = self._ordered_input_names.index('frequency_scale')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` source of Klank.

        ::

            >>> frequencies = [200, 671, 1153, 1723]
            >>> amplitudes = None
            >>> decay_times = [1, 1, 1, 1]
            >>> specifications = [frequencies, amplitudes, decay_times]
            >>> source = supriya.ugens.BrownNoise.ar() * 0.001
            >>> klank = supriya.ugens.Klank.ar(
            ...     decay_scale=1,
            ...     frequency_offset=0,
            ...     frequency_scale=1,
            ...     source=source,
            ...     specifications=specifications,
            ...     )
            >>> klank.source
            BinaryOpUGen.ar()[0]

        Returns ugen source.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]

    @property
    def specifications(self):
        """
        Gets `specifications` source of Klank.

        ::

            >>> frequencies = [200, 671, 1153, 1723]
            >>> amplitudes = None
            >>> decay_times = [1, 1, 1, 1]
            >>> specifications = [frequencies, amplitudes, decay_times]
            >>> source = supriya.ugens.BrownNoise.ar() * 0.001
            >>> klank = supriya.ugens.Klank.ar(
            ...     decay_scale=1,
            ...     frequency_offset=0,
            ...     frequency_scale=1,
            ...     source=source,
            ...     specifications=specifications,
            ...     )
            >>> klank.specifications
            (200.0, 1.0, 1.0, 671.0, 1.0, 1.0, 1153.0, 1.0, 1.0, 1723.0, 1.0, 1.0)

        Returns ugen source.
        """
        index = self._ordered_input_names.index('specifications')
        return tuple(self._inputs[index:])
