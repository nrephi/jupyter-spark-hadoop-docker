#!/bin/bash
[ ! -d "/hadoop/data/nn" ] && /hadoop/bin/hdfs --config /etc/hadoop namenode -format 
/hadoop/sbin/start-dfs.sh