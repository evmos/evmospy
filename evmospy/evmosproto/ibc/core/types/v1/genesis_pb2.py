# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/types/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmospy.evmosproto.ibc.core.client.v1 import genesis_pb2 as ibc_dot_core_dot_client_dot_v1_dot_genesis__pb2
from evmospy.evmosproto.ibc.core.connection.v1 import genesis_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_genesis__pb2
from evmospy.evmosproto.ibc.core.channel.v1 import genesis_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_genesis__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fibc/core/types/v1/genesis.proto\x12\x11ibc.core.types.v1\x1a\x14gogoproto/gogo.proto\x1a ibc/core/client/v1/genesis.proto\x1a$ibc/core/connection/v1/genesis.proto\x1a!ibc/core/channel/v1/genesis.proto\"\xa8\x02\n\x0cGenesisState\x12W\n\x0e\x63lient_genesis\x18\x01 \x01(\x0b\x32 .ibc.core.client.v1.GenesisStateB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:\"client_genesis\"\x12\x63\n\x12\x63onnection_genesis\x18\x02 \x01(\x0b\x32$.ibc.core.connection.v1.GenesisStateB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:\"connection_genesis\"\x12Z\n\x0f\x63hannel_genesis\x18\x03 \x01(\x0b\x32!.ibc.core.channel.v1.GenesisStateB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:\"channel_genesis\"B0Z.github.com/cosmos/ibc-go/v3/modules/core/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'ibc.core.types.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.types.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/cosmos/ibc-go/v3/modules/core/types'
  _GENESISSTATE.fields_by_name['client_genesis']._options = None
  _GENESISSTATE.fields_by_name['client_genesis']._serialized_options = b'\310\336\037\000\362\336\037\025yaml:\"client_genesis\"'
  _GENESISSTATE.fields_by_name['connection_genesis']._options = None
  _GENESISSTATE.fields_by_name['connection_genesis']._serialized_options = b'\310\336\037\000\362\336\037\031yaml:\"connection_genesis\"'
  _GENESISSTATE.fields_by_name['channel_genesis']._options = None
  _GENESISSTATE.fields_by_name['channel_genesis']._serialized_options = b'\310\336\037\000\362\336\037\026yaml:\"channel_genesis\"'
  _GENESISSTATE._serialized_start=184
  _GENESISSTATE._serialized_end=480
# @@protoc_insertion_point(module_scope)
