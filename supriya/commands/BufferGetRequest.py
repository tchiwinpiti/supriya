import supriya.osc
from supriya.commands.Request import Request


class BufferGetRequest(Request):
    """
    A /b_get request.

    ::

        >>> import supriya.commands
        >>> request = supriya.commands.BufferGetRequest(
        ...     buffer_id=23,
        ...     indices=(0, 4, 8, 16),
        ...     )
        >>> request
        BufferGetRequest(
            buffer_id=23,
            indices=(0, 4, 8, 16),
            )

    ::

        >>> message = request.to_osc_message()
        >>> message
        OscMessage(42, 23, 0, 4, 8, 16)

    ::

        >>> message.address == supriya.commands.RequestId.BUFFER_GET
        True

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_buffer_id',
        '_indices',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        buffer_id=None,
        indices=None,
        ):
        Request.__init__(self)
        self._buffer_id = int(buffer_id)
        self._indices = tuple(int(index) for index in indices)

    ### PUBLIC METHODS ###

    def to_osc_message(self, with_textual_osc_command=False):
        if with_textual_osc_command:
            request_id = self.request_command
        else:
            request_id = int(self.request_id)
        buffer_id = int(self.buffer_id)
        contents = [
            request_id,
            buffer_id,
            ]
        if self.indices:
            for index in self.indices:
                contents.append(index)
        message = supriya.osc.OscMessage(*contents)
        return message

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        return self._buffer_id

    @property
    def indices(self):
        return self._indices

    @property
    def response_specification(self):
        import supriya.commands
        return {
            supriya.commands.BufferSetResponse: {
                'buffer_id': self.buffer_id,
                },
            supriya.commands.FailResponse: {
                'failed_command': '/b_get',
                }
            }

    @property
    def request_id(self):
        import supriya.commands
        return supriya.commands.RequestId.BUFFER_GET
