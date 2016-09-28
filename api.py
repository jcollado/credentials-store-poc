#!/usr/bin/env python
"""API server."""

from flask import (
    Flask,
    json,
    request,
)

import tasks

app = Flask(__name__)


@app.route('/credentials/<tenant>', methods=['GET'])
def get_credentials(tenant):
    """Get credentials for a given tenant."""
    response = tasks.get_credentials(tenant)
    return json.jsonify(**response['data'])


@app.route('/credentials/<tenant>', methods=['PUT'])
def put_credentials(tenant):
    """Store credentials for a given tenant."""
    document = json.loads(request.data)
    tasks.put_credentials(tenant, document)
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
