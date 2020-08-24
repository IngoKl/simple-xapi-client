import uuid


class XapiStatement:
    def __init__(self, actor, verb, obj, context=False, result=False):
        self.id = uuid.uuid1()
        self.actor = actor
        self.verb = verb
        self.object = obj
        self.context = context
        self.result = result

    def __repr__(self):
        return f'{self.actor.name}'

    def get_statement(self):
        statement = {
            'id': str(self.id),
            'actor': self.actor.get_actor(),
            'verb': self.verb.get_verb(),
            'object': self.object.get_object(),
        }

        if self.context:
            statement['context'] = self.context

        if self.result:
            statement['result'] = self.result

        return statement
