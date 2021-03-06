import supriya.osc
from supriya.commands.Request import Request


class BufferAllocateRequest(Request):
    """
    A /b_alloc request.

    ::

        >>> import supriya.commands
        >>> request = supriya.commands.BufferAllocateRequest(
        ...     buffer_id=23,
        ...     frame_count=512,
        ...     channel_count=2,
        ...     )
        >>> request
        BufferAllocateRequest(
            buffer_id=23,
            channel_count=2,
            frame_count=512,
            )

    ::

        >>> message = request.to_osc_message()
        >>> message
        OscMessage(28, 23, 512, 2)

    ::

        >>> message.address == supriya.commands.RequestId.BUFFER_ALLOCATE
        True

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_buffer_id',
        '_channel_count',
        '_completion_message',
        '_frame_count',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        buffer_id=None,
        frame_count=None,
        channel_count=None,
        completion_message=None,
        ):
        Request.__init__(self)
        self._buffer_id = int(buffer_id)
        self._frame_count = frame_count
        if channel_count is not None:
            channel_count = int(channel_count)
            assert 0 < channel_count
        self._channel_count = channel_count
        self._completion_message = self._coerce_completion_message_input(
            completion_message)

    ### PUBLIC METHODS ###

    def to_osc_message(self, with_textual_osc_command=False):
        if with_textual_osc_command:
            request_id = self.request_command
        else:
            request_id = int(self.request_id)
        buffer_id = int(self.buffer_id)
        frame_count = int(self.frame_count)
        channel_count = int(self.channel_count)
        contents = [
            request_id,
            buffer_id,
            frame_count,
            channel_count,
            ]
        self._coerce_completion_message_output(contents)
        message = supriya.osc.OscMessage(*contents)
        return message

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        return self._buffer_id

    @property
    def channel_count(self):
        return self._channel_count

    @property
    def completion_message(self):
        return self._completion_message

    @property
    def frame_count(self):
        return self._frame_count

    @property
    def request_id(self):
        import supriya.commands
        return supriya.commands.RequestId.BUFFER_ALLOCATE

    @property
    def response_specification(self):
        import supriya.commands
        return {
            supriya.commands.DoneResponse: {
                'action': ('/b_alloc', self.buffer_id),
                },
            }
