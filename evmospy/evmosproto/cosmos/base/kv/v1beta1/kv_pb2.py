# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/kv/v1beta1/kv.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/base/kv/v1beta1/kv.proto\x12\x16\x63osmos.base.kv.v1beta1\x1a\x14gogoproto/gogo.proto\":\n\x05Pairs\x12\x31\n\x05pairs\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.kv.v1beta1.PairB\x04\xc8\xde\x1f\x00\"\"\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x42\'Z%github.com/cosmos/cosmos-sdk/types/kvb\x06proto3')



_PAIRS = DESCRIPTOR.message_types_by_name['Pairs']
_PAIR = DESCRIPTOR.message_types_by_name['Pair']
Pairs = _reflection.GeneratedProtocolMessageType('Pairs', (_message.Message,), {
  'DESCRIPTOR' : _PAIRS,
  '__module__' : 'cosmos.base.kv.v1beta1.kv_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.kv.v1beta1.Pairs)
  })
_sym_db.RegisterMessage(Pairs)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
  'DESCRIPTOR' : _PAIR,
  '__module__' : 'cosmos.base.kv.v1beta1.kv_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.kv.v1beta1.Pair)
  })
_sym_db.RegisterMessage(Pair)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/kv'
  _PAIRS.fields_by_name['pairs']._options = None
  _PAIRS.fields_by_name['pairs']._serialized_options = b'\310\336\037\000'
  _PAIRS._serialized_start=81
  _PAIRS._serialized_end=139
  _PAIR._serialized_start=141
  _PAIR._serialized_end=175
# @@protoc_insertion_point(module_scope)
