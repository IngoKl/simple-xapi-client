import simple_xapi_client.vocabulary as vocab


class XapiVerb():
    def __init__(self, verb):
        if type(verb) == str:
            if verb in vocab.xapi_verbs.keys():
                self.verb = vocab.xapi_verbs[verb]
        else:
            self.verb = verb

    def get_verb(self):
        return self.verb

    def __repr__(self):
        return self.verb
