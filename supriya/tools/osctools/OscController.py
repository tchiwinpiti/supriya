# -*- encoding: utf-8 -*-
from __future__ import print_function
try:
    import queue
except ImportError:
    import Queue as queue
import socket
from supriya.tools.systemtools.SupriyaObject import SupriyaObject


class OscController(SupriyaObject):
    '''An OSC controller.

    ::

        >>> from supriya import osctools
        >>> controller = osctools.OscController(
        ...     server_ip_address='127.0.0.1',
        ...     server_port=57751,
        ...     )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_dispatcher',
        '_incoming_message_queue',
        '_listener',
        '_server_ip_address',
        '_server_port',
        '_socket_instance',
        '_timeout',
        )

    class CleanableQueue(queue.Queue):

        def __init__(self, maximum_length=0):
            queue.Queue.__init__(self)
            self._maximum_length = int(maximum_length)

        def clean(self):
            while not self.empty() and self.maximum_length < self.qsize():
                self.get()

        @property
        def maximum_length(self):
            return self._maximum_length

    ### INITIALIZER ###

    def __init__(self,
        server_ip_address='127.0.0.1',
        server_port=57751,
        timeout=2,
        verbose=True,
        ):
        from supriya.tools import osctools
        self._server_ip_address = server_ip_address
        self._server_port = int(server_port)
        assert 0 < int(timeout)
        self._timeout = int(timeout)
        self._socket_instance = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM,
            )
        self._socket_instance.settimeout(self.timeout)
        self._dispatcher = osctools.OscDispatcher()
        self._listener = osctools.OscListener(self)
        self._listener.start()
        self._socket_instance.bind(('', 0))
        if verbose:
            self._dispatcher.register_osc_callback(
                osctools.OscCallback(
                    address_pattern='/*', 
                    procedure=self._print_message,
                    )
                )

    ### SPECIAL METHODS ###

    def __del__(self):
        self._listener.quit(wait=True)

    ### PRIVATE METHODS ###

    def _print_message(self, message):
        if message.address != '/status.reply':
            print('RECV:', message)

    ### PUBLIC METHODS ###

    def register_osc_callback(self, osc_callback):
        self._dispatcher.register_osc_callback(osc_callback)

    def send(self, message):
        from supriya.tools import osctools
        prototype = (str, tuple, osctools.OscMessage, osctools.OscBundle)
        assert isinstance(message, prototype)
        if isinstance(message, str):
            message = osctools.OscMessage(message)
        elif isinstance(message, tuple):
            assert len(message)
            message = osctools.OscMessage(
                message[0],
                *message[1:]
                )
        datagram = message.to_datagram()
        self.socket_instance.sendto(
            datagram,
            (self.server_ip_address, self.server_port),
            )

    def unregister_osc_callback(self, osc_callback):
        self._dispatcher.unregister_osc_callback(osc_callback)

    ### PUBLIC PROPERTIES ###

    @property
    def dispatcher(self):
        return self._dispatcher

    @property
    def listener(self):
        return self._listener

    @property
    def server_ip_address(self):
        return self._server_ip_address

    @property
    def server_port(self):
        return self._server_port

    @property
    def socket_instance(self):
        return self._socket_instance

    @property
    def timeout(self):
        return self._timeout