#!/bin/sh

set -e

wget -qc https://github.com/litnimax/remote_agent/archive/12.0.zip 
unzip -oq 12.0.zip && rm 12.0.zip
mkdir -p remote_agent
cp -r remote_agent-12.0/agent/* remote_agent/
rm -rf remote_agent-12.0
cp remote_agent/start_agent.sh .
pip install -qr remote_agent/requirements.txt
sed -i 's/gevent_agent/agent/' start_agent.sh
echo '***********************************************'
echo 'Installation done. Update now your settings in start_agent.sh.'
echo '***********************************************'
