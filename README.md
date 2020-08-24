# Simple xAPI Client

This is a minimalistic [xAPI](http://https://xapi.com) client written in Python 3. So far, only writing xAPI statements is supported.

Be aware that this is not a full implementation of xAPI but rather a purpusfully minimalistic starting point.
Have a look at [gtoffoli/django-xapi-client](https://github.com/gtoffoli/django-xapi-client) and [TinCanPython](https://rusticisoftware.github.io/TinCanPython) for more advanced approaches in Python.

## Basic Usage

```Python
from simple_xapi_client import LRS, XapiStatement, XapiActor, XapiVerb, XapiObject

actor = XapiActor('Demo', 'demo@url.com')
obj = XapiObject('https://url.com/essay', 'Essay')
verb = XapiVerb('created')

statement = XapiStatement(actor, verb, obj)

client = LRS('https://lrs.url.com/data/xAPI', 'Username', 'Password')

client.put_statement(statement)
```

## Vocabulary

Both activites and verbs can either be loaded from the inbuild vocabulary `simple_xapi_client\vocabulary.py` (tiny so far) or constructed manually.

### Inbuild Vocabulary

```Python
# If 'created' or 'Essay' is available in the vocabulary, it will be used.
verb = XapiVerb('created')
obj = XapiObject('https://url.com/essay', 'Essay')
```

### Manually Created

```Python
# Manually constructed verb; works similarly for objects
verb = XapiVerb({'id': 'http://url.com/demoverb', 'display': {'en-US': 'demoverb'}})
```

## Development

If you want to run the tests using `pytest`, you will have to copy and modify `settings.conf.default` to `settings.conf`.