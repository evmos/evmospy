# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/authz.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmospy.evmosproto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from evmospy.evmosproto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cosmos/staking/v1beta1/authz.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x90\x03\n\x12StakeAuthorization\x12Z\n\nmax_tokens\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB+\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12K\n\nallow_list\x18\x02 \x01(\x0b\x32\x35.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsH\x00\x12J\n\tdeny_list\x18\x03 \x01(\x0b\x32\x35.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsH\x00\x12\x45\n\x12\x61uthorization_type\x18\x04 \x01(\x0e\x32).cosmos.staking.v1beta1.AuthorizationType\x1a\x1d\n\nValidators\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x03(\t:\x11\xd2\xb4-\rAuthorizationB\x0c\n\nvalidators*\x9e\x01\n\x11\x41uthorizationType\x12\"\n\x1e\x41UTHORIZATION_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x41UTHORIZATION_TYPE_DELEGATE\x10\x01\x12!\n\x1d\x41UTHORIZATION_TYPE_UNDELEGATE\x10\x02\x12!\n\x1d\x41UTHORIZATION_TYPE_REDELEGATE\x10\x03\x42.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')

_AUTHORIZATIONTYPE = DESCRIPTOR.enum_types_by_name['AuthorizationType']
AuthorizationType = enum_type_wrapper.EnumTypeWrapper(_AUTHORIZATIONTYPE)
AUTHORIZATION_TYPE_UNSPECIFIED = 0
AUTHORIZATION_TYPE_DELEGATE = 1
AUTHORIZATION_TYPE_UNDELEGATE = 2
AUTHORIZATION_TYPE_REDELEGATE = 3


_STAKEAUTHORIZATION = DESCRIPTOR.message_types_by_name['StakeAuthorization']
_STAKEAUTHORIZATION_VALIDATORS = _STAKEAUTHORIZATION.nested_types_by_name['Validators']
StakeAuthorization = _reflection.GeneratedProtocolMessageType('StakeAuthorization', (_message.Message,), {

  'Validators' : _reflection.GeneratedProtocolMessageType('Validators', (_message.Message,), {
    'DESCRIPTOR' : _STAKEAUTHORIZATION_VALIDATORS,
    '__module__' : 'cosmos.staking.v1beta1.authz_pb2'
    # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.StakeAuthorization.Validators)
    })
  ,
  'DESCRIPTOR' : _STAKEAUTHORIZATION,
  '__module__' : 'cosmos.staking.v1beta1.authz_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.StakeAuthorization)
  })
_sym_db.RegisterMessage(StakeAuthorization)
_sym_db.RegisterMessage(StakeAuthorization.Validators)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
  _STAKEAUTHORIZATION.fields_by_name['max_tokens']._options = None
  _STAKEAUTHORIZATION.fields_by_name['max_tokens']._serialized_options = b'\252\337\037\'github.com/cosmos/cosmos-sdk/types.Coin'
  _STAKEAUTHORIZATION._options = None
  _STAKEAUTHORIZATION._serialized_options = b'\322\264-\rAuthorization'
  _AUTHORIZATIONTYPE._serialized_start=547
  _AUTHORIZATIONTYPE._serialized_end=705
  _STAKEAUTHORIZATION._serialized_start=144
  _STAKEAUTHORIZATION._serialized_end=544
  _STAKEAUTHORIZATION_VALIDATORS._serialized_start=482
  _STAKEAUTHORIZATION_VALIDATORS._serialized_end=511
# @@protoc_insertion_point(module_scope)
