# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/commitment/v1/commitment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
import proofs_pb2 as proofs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ibc/core/commitment/v1/commitment.proto\x12\x16ibc.core.commitment.v1\x1a\x14gogoproto/gogo.proto\x1a\x0cproofs.proto\" \n\nMerkleRoot\x12\x0c\n\x04hash\x18\x01 \x01(\x0c:\x04\x88\xa0\x1f\x00\"9\n\x0cMerklePrefix\x12)\n\nkey_prefix\x18\x01 \x01(\x0c\x42\x15\xf2\xde\x1f\x11yaml:\"key_prefix\"\"9\n\nMerklePath\x12%\n\x08key_path\x18\x01 \x03(\tB\x13\xf2\xde\x1f\x0fyaml:\"key_path\":\x04\x98\xa0\x1f\x00\"5\n\x0bMerkleProof\x12&\n\x06proofs\x18\x01 \x03(\x0b\x32\x16.ics23.CommitmentProofB>Z<github.com/cosmos/ibc-go/v3/modules/core/23-commitment/typesb\x06proto3')



_MERKLEROOT = DESCRIPTOR.message_types_by_name['MerkleRoot']
_MERKLEPREFIX = DESCRIPTOR.message_types_by_name['MerklePrefix']
_MERKLEPATH = DESCRIPTOR.message_types_by_name['MerklePath']
_MERKLEPROOF = DESCRIPTOR.message_types_by_name['MerkleProof']
MerkleRoot = _reflection.GeneratedProtocolMessageType('MerkleRoot', (_message.Message,), {
  'DESCRIPTOR' : _MERKLEROOT,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerkleRoot)
  })
_sym_db.RegisterMessage(MerkleRoot)

MerklePrefix = _reflection.GeneratedProtocolMessageType('MerklePrefix', (_message.Message,), {
  'DESCRIPTOR' : _MERKLEPREFIX,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerklePrefix)
  })
_sym_db.RegisterMessage(MerklePrefix)

MerklePath = _reflection.GeneratedProtocolMessageType('MerklePath', (_message.Message,), {
  'DESCRIPTOR' : _MERKLEPATH,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerklePath)
  })
_sym_db.RegisterMessage(MerklePath)

MerkleProof = _reflection.GeneratedProtocolMessageType('MerkleProof', (_message.Message,), {
  'DESCRIPTOR' : _MERKLEPROOF,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerkleProof)
  })
_sym_db.RegisterMessage(MerkleProof)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z<github.com/cosmos/ibc-go/v3/modules/core/23-commitment/types'
  _MERKLEROOT._options = None
  _MERKLEROOT._serialized_options = b'\210\240\037\000'
  _MERKLEPREFIX.fields_by_name['key_prefix']._options = None
  _MERKLEPREFIX.fields_by_name['key_prefix']._serialized_options = b'\362\336\037\021yaml:\"key_prefix\"'
  _MERKLEPATH.fields_by_name['key_path']._options = None
  _MERKLEPATH.fields_by_name['key_path']._serialized_options = b'\362\336\037\017yaml:\"key_path\"'
  _MERKLEPATH._options = None
  _MERKLEPATH._serialized_options = b'\230\240\037\000'
  _MERKLEROOT._serialized_start=103
  _MERKLEROOT._serialized_end=135
  _MERKLEPREFIX._serialized_start=137
  _MERKLEPREFIX._serialized_end=194
  _MERKLEPATH._serialized_start=196
  _MERKLEPATH._serialized_end=253
  _MERKLEPROOF._serialized_start=255
  _MERKLEPROOF._serialized_end=308
# @@protoc_insertion_point(module_scope)
