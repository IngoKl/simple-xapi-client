import requests
import simple_xapi_client


class LRS:
    def __init__(self, endpoint, basica_username, basica_password):
        self.endpoint = endpoint
        self.basica_username = basica_username
        self.basica_password = basica_password

    def __repr__(self):
        return self.endpoint

    def put_statement(self, statement):
        headers = {
            'X-Experience-API-Version': '1.0.3',
            'Content-Type': 'application/json'
        }

        if type(statement) == dict:
            statement_id = statement['id']

        if type(statement) == simple_xapi_client.statement.XapiStatement:
            statement = statement.get_statement()
            statement_id = statement['id']

        r = requests.put(f'{self.endpoint}/statements?statementId={statement_id}', json=statement, headers=headers, auth=(self.basica_username, self.basica_password))
        return r.status_code
