import itertools
import sys
from supriya.system.SupriyaObject import SupriyaObject


class ResponseManager(SupriyaObject):
    """
    Handles OSC responses from scsynth.

    ::

        >>> import supriya.commands
        >>> import supriya.osc
        >>> manager = supriya.commands.ResponseManager

    ::

        >>> message = supriya.osc.OscMessage(
        ...     '/status.reply', 1, 0, 0, 2, 4,
        ...     0.040679048746824265, 0.15118031203746796,
        ...     44100.0, 44100.00077873274,
        ...     )
        >>> manager.handle_message(message)
        StatusResponse(
            actual_sample_rate=44100.00077873274,
            average_cpu_usage=0.040679048746824265,
            group_count=2,
            peak_cpu_usage=0.15118031203746796,
            synth_count=0,
            synthdef_count=4,
            target_sample_rate=44100.0,
            ugen_count=0,
            )

    ::

        >>> message = supriya.osc.OscMessage('/b_info', 1100, 512, 1, 44100.0)
        >>> manager.handle_message(message)[0]
        BufferInfoResponse(
            buffer_id=1100,
            channel_count=1,
            frame_count=512,
            sample_rate=44100.0,
            )

    ::

        >>> message = supriya.osc.OscMessage('/n_set', 1023, '/one', -1, '/two', 0)
        >>> manager.handle_message(message)
        NodeSetResponse(
            items=(
                NodeSetItem(
                    control_index_or_name='/one',
                    control_value=-1,
                    ),
                NodeSetItem(
                    control_index_or_name='/two',
                    control_value=0,
                    ),
                ),
            node_id=1023,
            )

    ::

        >>> message = supriya.osc.OscMessage('/b_setn', 1, 0, 8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        >>> manager.handle_message(message)
        BufferSetContiguousResponse(
            buffer_id=1,
            items=(
                BufferSetContiguousItem(
                    sample_values=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                    starting_sample_index=0,
                    ),
                ),
            )

    ::

        >>> message = supriya.osc.OscMessage('/g_queryTree.reply', 0, 0, 1, 1, 2, 1001, 0, 1000, 1, 1002, 0)
        >>> manager.handle_message(message)
        QueryTreeResponse(
            node_id=0,
            query_tree_group=QueryTreeGroup(
                children=(
                    QueryTreeGroup(
                        children=(
                            QueryTreeGroup(
                                children=(),
                                node_id=1001,
                                ),
                            QueryTreeGroup(
                                children=(
                                    QueryTreeGroup(
                                        children=(),
                                        node_id=1002,
                                        ),
                                    ),
                                node_id=1000,
                                ),
                            ),
                        node_id=1,
                        ),
                    ),
                node_id=0,
                ),
            )

    ::

        >>> print(manager.handle_message(message))
        NODE TREE 0 group
            1 group
                1001 group
                1000 group
                    1002 group

    """

    ### PUBLIC METHODS ###

    @staticmethod
    def group_items(items, length):
        iterators = [iter(items)] * length
        if sys.version_info[0] == 2:
            iterator = itertools.izip(*iterators)
        else:
            iterator = zip(*iterators)
        return iterator

    @staticmethod
    def handle_message(message):
        address, contents = message.address, message.contents
        if address in _response_handlers:
            handler = _response_handlers[address]
            response = handler(address, contents)
            return response
        #print('UNHANDLED:', message)

    @staticmethod
    def handle_b_info(command, contents):
        import supriya.commands
        responses = []
        for group in ResponseManager.group_items(contents, 4):
            response = supriya.commands.BufferInfoResponse(*group)
            responses.append(response)
        responses = tuple(responses)
        return responses

    @staticmethod
    def handle_b_set(command, contents):
        import supriya.commands
        buffer_id, remainder = contents[0], contents[1:]
        items = []
        for group in ResponseManager.group_items(remainder, 2):
            item = supriya.commands.BufferSetItem(*group)
            items.append(item)
        items = tuple(items)
        response = supriya.commands.BufferSetResponse(
            buffer_id=buffer_id,
            items=items,
            )
        return response

    @staticmethod
    def handle_b_setn(command, contents):
        import supriya.commands
        buffer_id, remainder = contents[0], contents[1:]
        items = []
        while remainder:
            starting_sample_index = remainder[0]
            sample_count = remainder[1]
            sample_values = tuple(remainder[2:2 + sample_count])
            item = supriya.commands.BufferSetContiguousItem(
                starting_sample_index=starting_sample_index,
                sample_values=sample_values,
                )
            items.append(item)
            remainder = remainder[2 + sample_count:]
        items = tuple(items)
        response = supriya.commands.BufferSetContiguousResponse(
            buffer_id=buffer_id,
            items=items,
            )
        return response

    @staticmethod
    def handle_c_set(command, contents):
        import supriya.commands
        items = []
        for group in ResponseManager.group_items(contents, 2):
            item = supriya.commands.ControlBusSetItem(*group)
            items.append(item)
        response = supriya.commands.ControlBusSetResponse(
            items=tuple(items),
            )
        return response

    @staticmethod
    def handle_c_setn(command, contents):
        import supriya.commands
        items = []
        while contents:
            starting_bus_id = contents[0]
            bus_count = contents[1]
            bus_values = tuple(contents[2:2 + bus_count])
            item = supriya.commands.ControlBusSetContiguousItem(
                starting_bus_id=starting_bus_id,
                bus_values=bus_values,
                )
            items.append(item)
            contents = contents[2 + bus_count:]
        items = tuple(items)
        response = supriya.commands.ControlBusSetContiguousResponse(
            items=items,
            )
        return response

    @staticmethod
    def handle_d_removed(command, contents):
        import supriya.commands
        synthdef_name = contents[0]
        response = supriya.commands.SynthDefRemovedResponse(
            synthdef_name=synthdef_name,
            )
        return response

    @staticmethod
    def handle_done(command, contents):
        import supriya.commands
        arguments = contents
        response = supriya.commands.DoneResponse(action=tuple(arguments))
        return response

    @staticmethod
    def handle_fail(command, contents):
        import supriya.commands
        failed_command = contents[0]
        failure_reason = contents[1:]
        if failure_reason:
            failure_reason = tuple(failure_reason)
        response = supriya.commands.FailResponse(
            failed_command=failed_command,
            failure_reason=failure_reason,
            )
        return response

    @staticmethod
    def handle_g_query_tree_reply(command, contents):
        def recurse(contents, control_flag):
            node_id = contents.pop(0)
            child_count = contents.pop(0)
            if child_count == -1:
                controls = []
                synthdef_name = contents.pop(0)
                if control_flag:
                    control_count = contents.pop(0)
                    for i in range(control_count):
                        control_name_or_index = contents.pop(0)
                        control_value = contents.pop(0)
                        control = supriya.commands.QueryTreeControl(
                            control_name_or_index=control_name_or_index,
                            control_value=control_value,
                            )
                        controls.append(control)
                controls = tuple(controls)
                result = supriya.commands.QueryTreeSynth(
                    node_id=node_id,
                    synthdef_name=synthdef_name,
                    controls=controls,
                    )
            else:
                children = []
                for i in range(child_count):
                    children.append(recurse(contents, control_flag))
                children = tuple(children)
                result = supriya.commands.QueryTreeGroup(
                    node_id=node_id,
                    children=children,
                    )
            return result
        import supriya.commands
        contents = list(contents)
        control_flag = bool(contents.pop(0))
        query_tree_group = recurse(contents, control_flag)
        response = supriya.commands.QueryTreeResponse(
            node_id=query_tree_group.node_id,
            query_tree_group=query_tree_group,
            )
        return response

    @staticmethod
    def handle_n_info(command, contents):
        import supriya.commands
        arguments = (command,) + contents
        response = supriya.commands.NodeInfoResponse(*arguments)
        return response

    @staticmethod
    def handle_n_set(command, contents):
        import supriya.commands
        node_id, remainder = contents[0], contents[1:]
        items = []
        for group in ResponseManager.group_items(remainder, 2):
            item = supriya.commands.NodeSetItem(*group)
            items.append(item)
        response = supriya.commands.NodeSetResponse(
            node_id=node_id,
            items=tuple(items),
            )
        return response

    @staticmethod
    def handle_n_setn(command, contents):
        import supriya.commands
        node_id, remainder = contents[0], contents[1:]
        items = []
        while remainder:
            control_index_or_name = remainder[0]
            control_count = remainder[1]
            control_values = tuple(remainder[2:2 + control_count])
            item = supriya.commands.NodeSetContiguousItem(
                control_index_or_name=control_index_or_name,
                control_values=control_values,
                )
            items.append(item)
            remainder = remainder[2 + control_count:]
        items = tuple(items)
        response = supriya.commands.NodeSetContiguousResponse(
            node_id=node_id,
            items=items,
            )
        return response

    @staticmethod
    def handle_status_reply(command, contents):
        import supriya.commands
        arguments = contents[1:]
        (
            ugen_count,
            synth_count,
            group_count,
            synthdef_count,
            average_cpu_usage,
            peak_cpu_usage,
            target_sample_rate,
            actual_sample_rate,
            ) = arguments
        response = supriya.commands.StatusResponse(
            actual_sample_rate=actual_sample_rate,
            average_cpu_usage=average_cpu_usage,
            group_count=group_count,
            peak_cpu_usage=peak_cpu_usage,
            synth_count=synth_count,
            synthdef_count=synthdef_count,
            target_sample_rate=target_sample_rate,
            ugen_count=ugen_count,
            )
        return response

    @staticmethod
    def handle_synced(command, contents):
        import supriya.commands
        arguments = contents
        response = supriya.commands.SyncedResponse(*arguments)
        return response

    @staticmethod
    def handle_tr(command, contents):
        import supriya.commands
        arguments = contents
        response = supriya.commands.TriggerResponse(*arguments)
        return response


_response_handlers = {
    '/b_info': ResponseManager.handle_b_info,
    '/b_set': ResponseManager.handle_b_set,
    '/b_setn': ResponseManager.handle_b_setn,
    '/c_set': ResponseManager.handle_c_set,
    '/c_setn': ResponseManager.handle_c_setn,
    '/d_removed': ResponseManager.handle_d_removed,
    '/done': ResponseManager.handle_done,
    '/fail': ResponseManager.handle_fail,
    '/g_queryTree.reply': ResponseManager.handle_g_query_tree_reply,
    '/n_end': ResponseManager.handle_n_info,
    '/n_go': ResponseManager.handle_n_info,
    '/n_info': ResponseManager.handle_n_info,
    '/n_move': ResponseManager.handle_n_info,
    '/n_off': ResponseManager.handle_n_info,
    '/n_on': ResponseManager.handle_n_info,
    '/n_set': ResponseManager.handle_n_set,
    '/n_setn': ResponseManager.handle_n_setn,
    '/status.reply': ResponseManager.handle_status_reply,
    '/synced': ResponseManager.handle_synced,
    '/tr': ResponseManager.handle_tr,
    }
