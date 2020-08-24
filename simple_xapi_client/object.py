import simple_xapi_client.vocabulary as vocab


class XapiObject():
    def __init__(self, id, definition, object_type='Actitivy'):
        self.id = id
        self.object_type = object_type

        if type(definition) == str:
            if definition in vocab.xapi_activities.keys():
                self.definition = vocab.xapi_activities[definition]
        else:
            self.definition = definition

    def get_object(self):
        return {
            'id': self.id,
            'definition': self.definition
        }

    def __repr__(self):
        return self.id
