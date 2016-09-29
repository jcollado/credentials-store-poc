# Credentials Store Proof of Concept

This is an experimental implementation of a credentials store service that
could be integrated in cloudify.

The overall design would be as follows:
- API server process listening to requests to get/put keys in the store (flask)
- Message queue waiting for tasks to get/put keys (rabbitmq)
- Worker process that performs actions on the internal credentials store (celery)
- Credentials store (vault)

Note that this implementation is not useful as it is because vault already
implements a server process with an API.

# Execution

To give a try to this example, follow these steps:

- Create a virtual environment
    mkvirtualenv credentials-store-poc

- Install dependencies
    pip install -r requirements.txt

- Launch services
    - Credentials store:

            ./vault.sh

    - Message queue:

            ./rabbitmq.sh

    - Celery worker:

            ./tasks.py

    - API server:

            ./api.py

- Store credentials

        # 204 NOT CONTENT returned
        http put localhost:5000/credentials/tenant hello=world


- Retrieve credentials

        # 200 OK returned with application/json data
        http put localhost:5000/credentials/tenant
