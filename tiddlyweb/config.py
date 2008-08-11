"""
The System's Configuration, to be carried
around in the environ. Eventually this
be in a userside actual file.
"""

import os

default_config = {
        'server_store': ['text', {'store_root': 'store'}],
        'server_host': {},
        'server_prefix': '',
        'extension_types': {
            'txt': 'text/plain',
            'html': 'text/html',
            'json': 'application/json',
            'wiki': 'text/x-tiddlywiki',
        },
        'serializers': {
            'text/x-tiddlywiki': ['wiki', 'text/html; charset=UTF-8'],
            'text/html': ['html', 'text/html; charset=UTF-8'],
            'text/plain': ['text', 'text/plain; charset=UTF-8'],
            'application/json': ['json', 'application/json; charset=UTF-8'],
            'default': ['html', 'text/html; charset=UTF-8'],
        },
        'extractors': [
            'http_basic',
            'simple_cookie',
            ],
        'auth_systems': [
            'cookie_form',
            'openid',
            ],
        # XXX this should come from a file
        'secret': 'this should come from a file',

        }
"""
A dict explaining the scheme, host and port of our server.
FIXME: a hack to get the server.host set properly in outgoing
wikis.
"""

if os.path.exists('tiddlywebconfig.py'):
    """
    Read in a local configuration override, but only
    from the current working directory (for now). If the
    file can't be imported things will blow up and the
    server not run.

    What's expected in the override file is a dict with the
    name config.
    """
    from tiddlywebconfig import config as custom_config
    config = default_config
    for key in custom_config:
        try:
            keys = custom_config[key].keys()
            for deep_key in keys:
                config[key].update(custom_config[key])
        except AttributeError:
            config[key] = custom_config[key]
else:
    config = default_config

