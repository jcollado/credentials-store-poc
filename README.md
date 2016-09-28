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
