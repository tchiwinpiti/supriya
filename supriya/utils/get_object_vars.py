import collections
import inspect


def get_object_vars(expr):
    from supriya import utils
    #print('VARS?', type(expr))
    signature = utils.get_object_signature(expr)
    args = collections.OrderedDict()
    var_args = []
    kwargs = {}
    if expr is None:
        return args, var_args, kwargs
    for i, (name, parameter) in enumerate(signature.parameters.items()):
        #print('   ', parameter)
        if parameter.kind is inspect._POSITIONAL_ONLY:
            try:
                args[name] = getattr(expr, name)
            except AttributeError:
                args[name] = expr[name]
        elif parameter.kind is inspect._POSITIONAL_OR_KEYWORD:
            try:
                args[name] = getattr(expr, name)
            except AttributeError:
                args[name] = expr[name]
        elif parameter.kind is inspect._VAR_POSITIONAL:
            try:
                var_args.extend(expr[:])
            except TypeError:
                var_args.extend(getattr(expr, name))
        elif parameter.kind is inspect._KEYWORD_ONLY:
            try:
                kwargs[name] = getattr(expr, name)
            except AttributeError:
                kwargs[name] = expr[name]
        elif parameter.kind is inspect._VAR_KEYWORD:
            items = {}
            if hasattr(expr, 'items'):
                items = expr.items()
            elif hasattr(expr, name):
                mapping = getattr(expr, name)
                if not isinstance(mapping, dict):
                    mapping = dict(mapping)
                items = mapping.items()
            elif hasattr(expr, '_' + name):
                mapping = getattr(expr, '_' + name)
                if not isinstance(mapping, dict):
                    mapping = dict(mapping)
                items = mapping.items()
            for key, value in items:
                if key not in args:
                    kwargs[key] = value
    return args, var_args, kwargs
