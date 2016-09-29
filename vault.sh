#!/bin/bash
docker run -p 8200:8200 -e VAULT_DEV_ROOT_TOKEN_ID='token' vault
