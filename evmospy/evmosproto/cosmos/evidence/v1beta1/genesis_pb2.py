# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/evidence/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/evidence/v1beta1/genesis.proto\x12\x17\x63osmos.evidence.v1beta1\x1a\x19google/protobuf/any.proto\"6\n\x0cGenesisState\x12&\n\x08\x65vidence\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB/Z-github.com/cosmos/cosmos-sdk/x/evidence/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.evidence.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.evidence.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/evidence/types'
  _GENESISSTATE._serialized_start=93
  _GENESISSTATE._serialized_end=147
# @@protoc_insertion_point(module_scope)
