from evmospy.evmosgrpc.builder import TransactionBuilder
from evmospy.evmosgrpc.transaction import Transaction
from evmospy.evmosgrpc.messages.msgsend import create_msg_send
from google.protobuf.json_format import MessageToDict

builder = TransactionBuilder(
    "enlist jar utility clog satoshi advance worth hundred style lemon know faith quick wedding decline vital broom approve patrol history dinosaur area kangaroo cereal"
)
msg = create_msg_send(
    builder.address, # from address, must be the same as the singer address
    builder.address, # destination address
    10, # amount to send
    denom="aevmos", # transfer denom
)
res = builder.send_tx(Transaction().generate_tx(builder, msg, memo="", fee="200000", gas_limit="400000"))

dictResponse = MessageToDict(res)
if 'code' in dictResponse['txResponse'].keys():
    print(dictResponse['txResponse']['rawLog'])
else:
    print(dictResponse['txResponse']['txhash'])
