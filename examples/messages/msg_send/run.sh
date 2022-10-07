#!/bin/bash
export GRPC_ENDPOINT=127.0.0.1:9090
export CHAIN_ID=evmos_9000-1
export DENOM=aevmos

. .venv/bin/activate
python example.py
