import uuid
import configparser

from simple_xapi_client import LRS, XapiStatement, XapiActor, XapiVerb, XapiObject


config = configparser.ConfigParser()
config.read('settings.conf')
test_cfg = config['test']


def test_config():
    assert(config.sections() == ['test'])


def test_simple_put_statement():
    statement = {
        'id': str(uuid.uuid1()),
        'actor': {'name': 'TestUser', 'mbox': 'mailto:test@simple-xapi-client.com'},
        'verb': {'id': 'http://activitystrea.ms/schema/1.0/accept'},
        'object': {'id': 'http://simple-xapi-client.com/test'}
    }

    client = LRS(test_cfg['xapi_endpoint'], test_cfg['xapi_basica_username'], test_cfg['xapi_basica_password'])

    assert(client.put_statement(statement) in [200, 204])


def test_statement():
    actor = XapiActor('Tester', 'tester@simple-xapi-client.com')
    obj = XapiObject('http://simple-xapi-client.com/essay', 'Essay')
    verb = XapiVerb('created')

    statement = XapiStatement(actor, verb, obj)

    client = LRS(test_cfg['xapi_endpoint'], test_cfg['xapi_basica_username'], test_cfg['xapi_basica_password'])

    assert(client.put_statement(statement) in [200, 204])

def test_statement_custom_object():
    actor = XapiActor('Tester', 'tester@simple-xapi-client.com')
    custom_object_definition = {
        'type': 'http://adlnet.gov/expapi/activities/course',
        'name': {'en-US': 'Python Test'},
        'description': {'en-US': 'A simple test'}
    }
    obj = XapiObject('http://simple-xapi-client.com/custom', custom_object_definition)
    verb = XapiVerb('created')

    statement = XapiStatement(actor, verb, obj)

    client = LRS(test_cfg['xapi_endpoint'], test_cfg['xapi_basica_username'], test_cfg['xapi_basica_password'])

    assert(client.put_statement(statement) in [200, 204])


def test_statement_context():
    actor = XapiActor('Tester', 'tester@simple-xapi-client.com')
    obj = XapiObject('http://simple-xapi-client.com/essay', 'Essay')
    verb = XapiVerb('created')
    context = {'instructor': {'name': 'Tester', 'mbox': 'mailto:tester@simple-xapi-client.com'}}

    statement = XapiStatement(actor, verb, obj, context=context)

    client = LRS(test_cfg['xapi_endpoint'], test_cfg['xapi_basica_username'], test_cfg['xapi_basica_password'])

    assert(client.put_statement(statement) in [200, 204])


def test_statement_result():
    actor = XapiActor('Tester', 'tester@simple-xapi-client.com')
    obj = XapiObject('http://simple-xapi-client.com/essay', 'Essay')
    verb = XapiVerb('created')
    result = {'completion': True, 'success': True}

    statement = XapiStatement(actor, verb, obj, result=result)

    client = LRS(test_cfg['xapi_endpoint'], test_cfg['xapi_basica_username'], test_cfg['xapi_basica_password'])

    assert(client.put_statement(statement) in [200, 204])