# Evmos proto

Compiled evmos' `protobuf` files ready to use with `python3.9+`.

## Usage

```python
import grpc
from evmospy.evmosproto.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub
from evmospy.evmosproto.cosmos.tx.v1beta1.service_pb2 import BroadcastTxRequest
channel = grpc.insecure_channel('127.0.0.1:9090')
stub = ServiceStub(channel)

msg = BroadcastTxRequest()

# Set your msg params...

send = stub.BroadcastTx(msg)
print(send)
```
