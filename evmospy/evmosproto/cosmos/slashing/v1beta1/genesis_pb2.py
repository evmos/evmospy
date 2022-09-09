# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/slashing/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmospy.evmosproto.cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/slashing/v1beta1/genesis.proto\x12\x17\x63osmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\"\x85\x02\n\x0cGenesisState\x12\x35\n\x06params\x18\x01 \x01(\x0b\x32\x1f.cosmos.slashing.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12Y\n\rsigning_infos\x18\x02 \x03(\x0b\x32$.cosmos.slashing.v1beta1.SigningInfoB\x1c\xf2\xde\x1f\x14yaml:\"signing_infos\"\xc8\xde\x1f\x00\x12\x63\n\rmissed_blocks\x18\x03 \x03(\x0b\x32..cosmos.slashing.v1beta1.ValidatorMissedBlocksB\x1c\xf2\xde\x1f\x14yaml:\"missed_blocks\"\xc8\xde\x1f\x00\"\x94\x01\n\x0bSigningInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12t\n\x16validator_signing_info\x18\x02 \x01(\x0b\x32-.cosmos.slashing.v1beta1.ValidatorSigningInfoB%\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:\"validator_signing_info\"\"\x83\x01\n\x15ValidatorMissedBlocks\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12Y\n\rmissed_blocks\x18\x02 \x03(\x0b\x32$.cosmos.slashing.v1beta1.MissedBlockB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:\"missed_blocks\"\",\n\x0bMissedBlock\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x0e\n\x06missed\x18\x02 \x01(\x08\x42/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_SIGNINGINFO = DESCRIPTOR.message_types_by_name['SigningInfo']
_VALIDATORMISSEDBLOCKS = DESCRIPTOR.message_types_by_name['ValidatorMissedBlocks']
_MISSEDBLOCK = DESCRIPTOR.message_types_by_name['MissedBlock']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.slashing.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

SigningInfo = _reflection.GeneratedProtocolMessageType('SigningInfo', (_message.Message,), {
  'DESCRIPTOR' : _SIGNINGINFO,
  '__module__' : 'cosmos.slashing.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.SigningInfo)
  })
_sym_db.RegisterMessage(SigningInfo)

ValidatorMissedBlocks = _reflection.GeneratedProtocolMessageType('ValidatorMissedBlocks', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORMISSEDBLOCKS,
  '__module__' : 'cosmos.slashing.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.ValidatorMissedBlocks)
  })
_sym_db.RegisterMessage(ValidatorMissedBlocks)

MissedBlock = _reflection.GeneratedProtocolMessageType('MissedBlock', (_message.Message,), {
  'DESCRIPTOR' : _MISSEDBLOCK,
  '__module__' : 'cosmos.slashing.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.MissedBlock)
  })
_sym_db.RegisterMessage(MissedBlock)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['signing_infos']._options = None
  _GENESISSTATE.fields_by_name['signing_infos']._serialized_options = b'\362\336\037\024yaml:\"signing_infos\"\310\336\037\000'
  _GENESISSTATE.fields_by_name['missed_blocks']._options = None
  _GENESISSTATE.fields_by_name['missed_blocks']._serialized_options = b'\362\336\037\024yaml:\"missed_blocks\"\310\336\037\000'
  _SIGNINGINFO.fields_by_name['validator_signing_info']._options = None
  _SIGNINGINFO.fields_by_name['validator_signing_info']._serialized_options = b'\310\336\037\000\362\336\037\035yaml:\"validator_signing_info\"'
  _VALIDATORMISSEDBLOCKS.fields_by_name['missed_blocks']._options = None
  _VALIDATORMISSEDBLOCKS.fields_by_name['missed_blocks']._serialized_options = b'\310\336\037\000\362\336\037\024yaml:\"missed_blocks\"'
  _GENESISSTATE._serialized_start=129
  _GENESISSTATE._serialized_end=390
  _SIGNINGINFO._serialized_start=393
  _SIGNINGINFO._serialized_end=541
  _VALIDATORMISSEDBLOCKS._serialized_start=544
  _VALIDATORMISSEDBLOCKS._serialized_end=675
  _MISSEDBLOCK._serialized_start=677
  _MISSEDBLOCK._serialized_end=721
# @@protoc_insertion_point(module_scope)
