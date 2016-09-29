#!/usr/bin/env python
"""Celery worker."""

import hvac

from celery import Celery

app = Celery()

client = hvac.Client(token='token')


@app.task
def get_credentials(tenant):
    """Get credentials for a given tenant."""
    print('Get credentials for: {}\n'.format(tenant))
    path = 'secret/{}'.format(tenant)
    document = client.read(path)
    print('Credentials: {}\n'.format(document))
    return document


@app.task
def put_credentials(tenant, document):
    """Put credentials for a given tenant."""
    print('Put credentials for {}: {}\n'.format(tenant, document))
    path = 'secret/{}'.format(tenant)
    return client.write(path, **document)

if __name__ == '__main__':
    app.worker_main()
