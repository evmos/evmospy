# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/event.proto\x12\x14\x63osmos.authz.v1beta1\"D\n\nEventGrant\x12\x14\n\x0cmsg_type_url\x18\x02 \x01(\t\x12\x0f\n\x07granter\x18\x03 \x01(\t\x12\x0f\n\x07grantee\x18\x04 \x01(\t\"E\n\x0b\x45ventRevoke\x12\x14\n\x0cmsg_type_url\x18\x02 \x01(\t\x12\x0f\n\x07granter\x18\x03 \x01(\t\x12\x0f\n\x07grantee\x18\x04 \x01(\tB&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3')



_EVENTGRANT = DESCRIPTOR.message_types_by_name['EventGrant']
_EVENTREVOKE = DESCRIPTOR.message_types_by_name['EventRevoke']
EventGrant = _reflection.GeneratedProtocolMessageType('EventGrant', (_message.Message,), {
  'DESCRIPTOR' : _EVENTGRANT,
  '__module__' : 'cosmos.authz.v1beta1.event_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.EventGrant)
  })
_sym_db.RegisterMessage(EventGrant)

EventRevoke = _reflection.GeneratedProtocolMessageType('EventRevoke', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREVOKE,
  '__module__' : 'cosmos.authz.v1beta1.event_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.EventRevoke)
  })
_sym_db.RegisterMessage(EventRevoke)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz'
  _EVENTGRANT._serialized_start=58
  _EVENTGRANT._serialized_end=126
  _EVENTREVOKE._serialized_start=128
  _EVENTREVOKE._serialized_end=197
# @@protoc_insertion_point(module_scope)
