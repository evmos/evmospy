# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/capability/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmosproto.cosmos.capability.v1beta1 import capability_pb2 as cosmos_dot_capability_dot_v1beta1_dot_capability__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/capability/v1beta1/genesis.proto',
  package='cosmos.capability.v1beta1',
  syntax='proto3',
  serialized_options=b'Z/github.com/cosmos/cosmos-sdk/x/capability/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'cosmos/capability/v1beta1/genesis.proto\x12\x19\x63osmos.capability.v1beta1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/capability/v1beta1/capability.proto\"~\n\rGenesisOwners\x12\r\n\x05index\x18\x01 \x01(\x04\x12^\n\x0cindex_owners\x18\x02 \x01(\x0b\x32+.cosmos.capability.v1beta1.CapabilityOwnersB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:\"index_owners\"\"]\n\x0cGenesisState\x12\r\n\x05index\x18\x01 \x01(\x04\x12>\n\x06owners\x18\x02 \x03(\x0b\x32(.cosmos.capability.v1beta1.GenesisOwnersB\x04\xc8\xde\x1f\x00\x42\x31Z/github.com/cosmos/cosmos-sdk/x/capability/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_capability_dot_v1beta1_dot_capability__pb2.DESCRIPTOR,])




_GENESISOWNERS = _descriptor.Descriptor(
  name='GenesisOwners',
  full_name='cosmos.capability.v1beta1.GenesisOwners',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='cosmos.capability.v1beta1.GenesisOwners.index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_owners', full_name='cosmos.capability.v1beta1.GenesisOwners.index_owners', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\023yaml:\"index_owners\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=262,
)


_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.capability.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='cosmos.capability.v1beta1.GenesisState.index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owners', full_name='cosmos.capability.v1beta1.GenesisState.owners', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=357,
)

_GENESISOWNERS.fields_by_name['index_owners'].message_type = cosmos_dot_capability_dot_v1beta1_dot_capability__pb2._CAPABILITYOWNERS
_GENESISSTATE.fields_by_name['owners'].message_type = _GENESISOWNERS
DESCRIPTOR.message_types_by_name['GenesisOwners'] = _GENESISOWNERS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisOwners = _reflection.GeneratedProtocolMessageType('GenesisOwners', (_message.Message,), {
  'DESCRIPTOR' : _GENESISOWNERS,
  '__module__' : 'cosmos.capability.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.capability.v1beta1.GenesisOwners)
  })
_sym_db.RegisterMessage(GenesisOwners)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.capability.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.capability.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISOWNERS.fields_by_name['index_owners']._options = None
_GENESISSTATE.fields_by_name['owners']._options = None
# @@protoc_insertion_point(module_scope)
