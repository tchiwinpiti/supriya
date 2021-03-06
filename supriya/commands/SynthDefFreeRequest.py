import supriya.osc
from supriya.commands.Request import Request


class SynthDefFreeRequest(Request):
    """
    A /d_free request.

    ::

        >>> import supriya.commands
        >>> request = supriya.commands.SynthDefFreeRequest(
        ...     synthdef='test',
        ...     )
        >>> request
        SynthDefFreeRequest(
            synthdef='test',
            )

    ::

        >>> message = request.to_osc_message()
        >>> message
        OscMessage(53, 'test')

    ::

        >>> message.address == supriya.commands.RequestId.SYNTHDEF_FREE
        True

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_synthdef',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        synthdef=None,
        ):
        import supriya.synthdefs
        Request.__init__(self)
        prototype = (str, supriya.synthdefs.SynthDef)
        assert isinstance(synthdef, prototype)
        self._synthdef = synthdef

    ### PUBLIC METHODS ###

    def to_osc_message(self, with_textual_osc_command=False):
        import supriya.synthdefs
        if with_textual_osc_command:
            request_id = self.request_command
        else:
            request_id = int(self.request_id)
        synthdef = self.synthdef
        if isinstance(synthdef, supriya.synthdefs.SynthDef):
            synthdef = synthdef.actual_name
        message = supriya.osc.OscMessage(
            request_id,
            synthdef,
            )
        return message

    ### PUBLIC PROPERTIES ###

    @property
    def response_specification(self):
        return None

    @property
    def request_id(self):
        import supriya.commands
        return supriya.commands.RequestId.SYNTHDEF_FREE

    @property
    def synthdef(self):
        return self._synthdef
