# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evmos/recovery/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x65vmos/recovery/v1/genesis.proto\x12\x11\x65vmos.recovery.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\"?\n\x0cGenesisState\x12/\n\x06params\x18\x01 \x01(\x0b\x32\x19.evmos.recovery.v1.ParamsB\x04\xc8\xde\x1f\x00\"g\n\x06Params\x12\x17\n\x0f\x65nable_recovery\x18\x01 \x01(\x08\x12\x44\n\x17packet_timeout_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x42,Z*github.com/evmos/evmos/v8/x/recovery/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'evmos.recovery.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:evmos.recovery.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'evmos.recovery.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:evmos.recovery.v1.Params)
  })
_sym_db.RegisterMessage(Params)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/evmos/evmos/v8/x/recovery/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _PARAMS.fields_by_name['packet_timeout_duration']._options = None
  _PARAMS.fields_by_name['packet_timeout_duration']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _GENESISSTATE._serialized_start=108
  _GENESISSTATE._serialized_end=171
  _PARAMS._serialized_start=173
  _PARAMS._serialized_end=276
# @@protoc_insertion_point(module_scope)
