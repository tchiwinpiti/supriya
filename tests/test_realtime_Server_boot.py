import supriya.realtime


def test_boot():
    server = supriya.realtime.Server(port=57757)
    try:
        for i in range(4):
            print(i)
            assert not server.is_running
            print('\tbooting...')
            server.boot()
            assert server.is_running
            print('\tquiting...')
            server.quit()
        assert not server.is_running
    finally:
        if server.is_running:
            server.quit()


def test_server_options():
    server = supriya.realtime.Server(port=57757)
    try:
        server_options = supriya.realtime.ServerOptions(
            memory_size=8192 * 32,
            load_synthdefs=False,
            )
        # Default
        server.boot()
        assert isinstance(server.server_options, type(server_options))
        assert server.server_options.memory_size == 8192
        assert server.server_options.load_synthdefs is True
        server.quit()
        # With ServerOptions
        server.boot(server_options=server_options)
        assert isinstance(server.server_options, type(server_options))
        assert server.server_options.memory_size == 8192 * 32
        assert server.server_options.load_synthdefs is False
        server.quit()
        # With **kwargs
        server.boot(load_synthdefs=False)
        assert isinstance(server.server_options, type(server_options))
        assert server.server_options.memory_size == 8192
        assert server.server_options.load_synthdefs is False
        server.quit()
        # With ServerOptions and **kwargs
        server.boot(load_synthdefs=False, server_options=server_options)
        assert isinstance(server.server_options, type(server_options))
        assert server.server_options.memory_size == 8192 * 32
        assert server.server_options.load_synthdefs is False
        server.quit()
    finally:
        if server.is_running:
            server.quit()
