#!/bin/sh

set -e

export DEBUG=1
export DISABLE_ODOO_BUS_POLL=0
export AGENT_UID=test
export AGENT_ADDRESS=agent
export AGENT_PORT=40000
#export AGENT_TIMEOUT=5 # Agent will override this setting on start.
export ODOO_SCHEME=http
export ODOO_HOST=odoo
export ODOO_PORT=8069
export ODOO_POLLING_PORT=8072
export ODOO_DB=test
export ODOO_LOGIN=test_agent
export ODOO_PASSWORD=test
export VERIFY_CERT=0 # Set to 1 if u use nginx with https and a public certificate.
export ODOO_RECONNECT_TIMEOUT=1 # Reconnect every 1 seconds

exec python2.7 agent.py
