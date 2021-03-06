from supriya.commands.Response import Response


class FailResponse(Response):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_failed_command',
        '_failure_reason',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        failed_command=None,
        failure_reason=None,
        osc_message=None,
        ):
        Response.__init__(
            self,
            osc_message=osc_message,
            )
        self._failed_command = failed_command
        self._failure_reason = failure_reason

    ### PUBLIC PROPERTIES ###

    @property
    def failed_command(self):
        return self._failed_command

    @property
    def failure_reason(self):
        return self._failure_reason
