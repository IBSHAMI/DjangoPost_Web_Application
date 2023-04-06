#!/bin/bash

SE_OPTS="--allowed-ips=*"

/usr/bin/supervisord --configuration /etc/supervisor/conf.d/supervisord.conf --nodaemon