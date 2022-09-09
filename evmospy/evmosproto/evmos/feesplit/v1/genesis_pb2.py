# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evmos/feesplit/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.evmos.feesplit.v1 import feesplit_pb2 as evmos_dot_feesplit_dot_v1_dot_feesplit__pb2
from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x65vmos/feesplit/v1/genesis.proto\x12\x11\x65vmos.feesplit.v1\x1a evmos/feesplit/v1/feesplit.proto\x1a\x14gogoproto/gogo.proto\"v\n\x0cGenesisState\x12/\n\x06params\x18\x01 \x01(\x0b\x32\x19.evmos.feesplit.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x35\n\nfee_splits\x18\x02 \x03(\x0b\x32\x1b.evmos.feesplit.v1.FeeSplitB\x04\xc8\xde\x1f\x00\"\x91\x01\n\x06Params\x12\x18\n\x10\x65nable_fee_split\x18\x01 \x01(\x08\x12H\n\x10\x64\x65veloper_shares\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12#\n\x1b\x61\x64\x64r_derivation_cost_create\x18\x03 \x01(\x04\x42,Z*github.com/evmos/evmos/v8/x/feesplit/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'evmos.feesplit.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:evmos.feesplit.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'evmos.feesplit.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:evmos.feesplit.v1.Params)
  })
_sym_db.RegisterMessage(Params)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/evmos/evmos/v8/x/feesplit/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['fee_splits']._options = None
  _GENESISSTATE.fields_by_name['fee_splits']._serialized_options = b'\310\336\037\000'
  _PARAMS.fields_by_name['developer_shares']._options = None
  _PARAMS.fields_by_name['developer_shares']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _GENESISSTATE._serialized_start=110
  _GENESISSTATE._serialized_end=228
  _PARAMS._serialized_start=231
  _PARAMS._serialized_end=376
# @@protoc_insertion_point(module_scope)