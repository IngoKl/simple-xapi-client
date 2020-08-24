class XapiActor:
    def __init__(self, name, email):
        self.name = name
        self.mbox = f'mailto:{email}'

    def get_actor(self):
        return {'name': self.name, 'mbox': self.mbox}

    def __repr__(self):
        return {'name': self.name, 'mbox': self.mbox}
