import supriya.osc
from supriya.commands.Request import Request


class SyncRequest(Request):
    """
    A /sync request.

    ::

        >>> import supriya.commands
        >>> request = supriya.commands.SyncRequest(
        ...     sync_id=1999,
        ...     )
        >>> request
        SyncRequest(
            sync_id=1999,
            )

    ::

        >>> message = request.to_osc_message()
        >>> message
        OscMessage(52, 1999)

    ::

        >>> message.address == supriya.commands.RequestId.SYNC
        True

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_sync_id',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        sync_id=None,
        ):
        Request.__init__(self)
        self._sync_id = int(sync_id)

    ### PUBLIC METHODS ###

    def to_osc_message(self, with_textual_osc_command=False):
        if with_textual_osc_command:
            request_id = self.request_command
        else:
            request_id = int(self.request_id)
        sync_id = int(self.sync_id)
        message = supriya.osc.OscMessage(
            request_id,
            sync_id,
            )
        return message

    ### PUBLIC PROPERTIES ###

    @property
    def response_specification(self):
        import supriya.commands
        return {
            supriya.commands.SyncedResponse: {
                'sync_id': self.sync_id,
                },
            }

    @property
    def request_id(self):
        import supriya.commands
        return supriya.commands.RequestId.SYNC

    @property
    def sync_id(self):
        return self._sync_id
