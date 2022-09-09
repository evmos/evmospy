# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/store/v1beta1/snapshot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(cosmos/base/store/v1beta1/snapshot.proto\x12\x19\x63osmos.base.store.v1beta1\x1a\x14gogoproto/gogo.proto\"\x9c\x01\n\x0cSnapshotItem\x12=\n\x05store\x18\x01 \x01(\x0b\x32,.cosmos.base.store.v1beta1.SnapshotStoreItemH\x00\x12\x45\n\x04iavl\x18\x02 \x01(\x0b\x32+.cosmos.base.store.v1beta1.SnapshotIAVLItemB\x08\xe2\xde\x1f\x04IAVLH\x00\x42\x06\n\x04item\"!\n\x11SnapshotStoreItem\x12\x0c\n\x04name\x18\x01 \x01(\t\"O\n\x10SnapshotIAVLItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x0e\n\x06height\x18\x04 \x01(\x05\x42*Z(github.com/cosmos/cosmos-sdk/store/typesb\x06proto3')



_SNAPSHOTITEM = DESCRIPTOR.message_types_by_name['SnapshotItem']
_SNAPSHOTSTOREITEM = DESCRIPTOR.message_types_by_name['SnapshotStoreItem']
_SNAPSHOTIAVLITEM = DESCRIPTOR.message_types_by_name['SnapshotIAVLItem']
SnapshotItem = _reflection.GeneratedProtocolMessageType('SnapshotItem', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTITEM,
  '__module__' : 'cosmos.base.store.v1beta1.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.SnapshotItem)
  })
_sym_db.RegisterMessage(SnapshotItem)

SnapshotStoreItem = _reflection.GeneratedProtocolMessageType('SnapshotStoreItem', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTSTOREITEM,
  '__module__' : 'cosmos.base.store.v1beta1.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.SnapshotStoreItem)
  })
_sym_db.RegisterMessage(SnapshotStoreItem)

SnapshotIAVLItem = _reflection.GeneratedProtocolMessageType('SnapshotIAVLItem', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTIAVLITEM,
  '__module__' : 'cosmos.base.store.v1beta1.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.SnapshotIAVLItem)
  })
_sym_db.RegisterMessage(SnapshotIAVLItem)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/store/types'
  _SNAPSHOTITEM.fields_by_name['iavl']._options = None
  _SNAPSHOTITEM.fields_by_name['iavl']._serialized_options = b'\342\336\037\004IAVL'
  _SNAPSHOTITEM._serialized_start=94
  _SNAPSHOTITEM._serialized_end=250
  _SNAPSHOTSTOREITEM._serialized_start=252
  _SNAPSHOTSTOREITEM._serialized_end=285
  _SNAPSHOTIAVLITEM._serialized_start=287
  _SNAPSHOTIAVLITEM._serialized_end=366
# @@protoc_insertion_point(module_scope)
