import collections
from supriya.tools.patterntools.EventPattern import EventPattern


class Pbind(EventPattern):
    """
    A pattern binding.

    ::

        >>> pattern = patterntools.Pbind(
        ...     pitch=patterntools.Pseq([0, 3, 7]),
        ...     duration=patterntools.Pseq([0.5, 0.25, 0.25, 0.125]),
        ...     foo=[1, 2],
        ...     bar=3,
        ...     )

    ::

        >>> for event in pattern:
        ...     event
        ...
        NoteEvent(
            bar=3,
            delta=0.5,
            duration=0.5,
            foo=(1, 2),
            pitch=0,
            uuid=UUID('...'),
            )
        NoteEvent(
            bar=3,
            delta=0.25,
            duration=0.25,
            foo=(1, 2),
            pitch=3,
            uuid=UUID('...'),
            )
        NoteEvent(
            bar=3,
            delta=0.25,
            duration=0.25,
            foo=(1, 2),
            pitch=7,
            uuid=UUID('...'),
            )

    ::

        >>> pattern = patterntools.Pseq([
        ...     patterntools.Pbind(
        ...         pitch=patterntools.Pseq([1, 2, 3], 1),
        ...         ),
        ...     patterntools.Pbind(
        ...         pitch=patterntools.Pseq([4, 5, 6], 1),
        ...         ),
        ...     ], 1)

    ::

        >>> for event in pattern:
        ...     event
        ...
        NoteEvent(
            pitch=1,
            uuid=UUID('...'),
            )
        NoteEvent(
            pitch=2,
            uuid=UUID('...'),
            )
        NoteEvent(
            pitch=3,
            uuid=UUID('...'),
            )
        NoteEvent(
            pitch=4,
            uuid=UUID('...'),
            )
        NoteEvent(
            pitch=5,
            uuid=UUID('...'),
            )
        NoteEvent(
            pitch=6,
            uuid=UUID('...'),
            )

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_patterns',
        '_synthdef',
        )

    ### INITIALIZER ###

    def __init__(self, synthdef=None, **patterns):
        from supriya.tools import patterntools
        from supriya.tools import synthdeftools
        assert isinstance(synthdef, (
            synthdeftools.SynthDef,
            patterntools.Pattern,
            type(None),
            ))
        self._synthdef = synthdef
        self._patterns = tuple(sorted(patterns.items()))

    ### SPECIAL METHODS ###

    def __getitem__(self, item):
        return self.patterns[item]

    ### PRIVATE METHODS ###

    def _coerce_pattern_pairs(self, patterns):
        from supriya.tools import patterntools
        patterns = dict(patterns)
        for name, pattern in sorted(patterns.items()):
            if not isinstance(pattern, patterntools.Pattern):
                pattern = patterntools.Pseq([pattern], None)
            patterns[name] = iter(pattern)
        synthdef = self.synthdef
        if not isinstance(synthdef, patterntools.Pattern):
            synthdef = patterntools.Pseq([synthdef], None)
        patterns['synthdef'] = iter(synthdef)
        return patterns

    def _get_format_specification(self):
        from abjad.tools import systemtools
        agent = systemtools.StorageFormatAgent(self)
        names = agent.signature_keyword_names
        names.extend(self.patterns)
        names.sort()
        return systemtools.FormatSpecification(
            client=self,
            storage_format_kwargs_names=names,
            template_names=names,
            )

    def _iterate(self, state=None):
        patterns = self._coerce_pattern_pairs(self._patterns)
        while True:
            expr = {}
            for name, pattern in sorted(patterns.items()):
                try:
                    expr[name] = next(pattern)
                except StopIteration:
                    return
            expr = self._coerce_iterator_output(expr)
            should_stop = yield expr
            if should_stop:
                return

    ### PUBLIC PROPERTIES ###

    @property
    def arity(self):
        return max(self._get_arity(v) for _, v in self._patterns)

    @property
    def is_infinite(self):
        from supriya.tools import patterntools
        for _, value in self._patterns:
            if (
                isinstance(value, patterntools.Pattern) and
                not value.is_infinite
                ):
                return False
            elif isinstance(value, collections.Sequence):
                return False
        return True

    @property
    def patterns(self):
        return dict(self._patterns)

    @property
    def synthdef(self):
        return self._synthdef
