# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/slashing/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmospy.evmosproto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from evmospy.evmosproto.cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/slashing/v1beta1/query.proto\x12\x17\x63osmos.slashing.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\"\x14\n\x12QueryParamsRequest\"L\n\x13QueryParamsResponse\x12\x35\n\x06params\x18\x01 \x01(\x0b\x32\x1f.cosmos.slashing.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"/\n\x17QuerySigningInfoRequest\x12\x14\n\x0c\x63ons_address\x18\x01 \x01(\t\"i\n\x18QuerySigningInfoResponse\x12M\n\x10val_signing_info\x18\x01 \x01(\x0b\x32-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\x04\xc8\xde\x1f\x00\"V\n\x18QuerySigningInfosRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x9b\x01\n\x19QuerySigningInfosResponse\x12\x41\n\x04info\x18\x01 \x03(\x0b\x32-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xf2\x03\n\x05Query\x12\x8c\x01\n\x06Params\x12+.cosmos.slashing.v1beta1.QueryParamsRequest\x1a,.cosmos.slashing.v1beta1.QueryParamsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/slashing/v1beta1/params\x12\xb1\x01\n\x0bSigningInfo\x12\x30.cosmos.slashing.v1beta1.QuerySigningInfoRequest\x1a\x31.cosmos.slashing.v1beta1.QuerySigningInfoResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/cosmos/slashing/v1beta1/signing_infos/{cons_address}\x12\xa5\x01\n\x0cSigningInfos\x12\x31.cosmos.slashing.v1beta1.QuerySigningInfosRequest\x1a\x32.cosmos.slashing.v1beta1.QuerySigningInfosResponse\".\x82\xd3\xe4\x93\x02(\x12&/cosmos/slashing/v1beta1/signing_infosB/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')



_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYSIGNINGINFOREQUEST = DESCRIPTOR.message_types_by_name['QuerySigningInfoRequest']
_QUERYSIGNINGINFORESPONSE = DESCRIPTOR.message_types_by_name['QuerySigningInfoResponse']
_QUERYSIGNINGINFOSREQUEST = DESCRIPTOR.message_types_by_name['QuerySigningInfosRequest']
_QUERYSIGNINGINFOSRESPONSE = DESCRIPTOR.message_types_by_name['QuerySigningInfosResponse']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'cosmos.slashing.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'cosmos.slashing.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QuerySigningInfoRequest = _reflection.GeneratedProtocolMessageType('QuerySigningInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSIGNINGINFOREQUEST,
  '__module__' : 'cosmos.slashing.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.QuerySigningInfoRequest)
  })
_sym_db.RegisterMessage(QuerySigningInfoRequest)

QuerySigningInfoResponse = _reflection.GeneratedProtocolMessageType('QuerySigningInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSIGNINGINFORESPONSE,
  '__module__' : 'cosmos.slashing.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.QuerySigningInfoResponse)
  })
_sym_db.RegisterMessage(QuerySigningInfoResponse)

QuerySigningInfosRequest = _reflection.GeneratedProtocolMessageType('QuerySigningInfosRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSIGNINGINFOSREQUEST,
  '__module__' : 'cosmos.slashing.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.QuerySigningInfosRequest)
  })
_sym_db.RegisterMessage(QuerySigningInfosRequest)

QuerySigningInfosResponse = _reflection.GeneratedProtocolMessageType('QuerySigningInfosResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSIGNINGINFOSRESPONSE,
  '__module__' : 'cosmos.slashing.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.QuerySigningInfosResponse)
  })
_sym_db.RegisterMessage(QuerySigningInfosResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYSIGNINGINFORESPONSE.fields_by_name['val_signing_info']._options = None
  _QUERYSIGNINGINFORESPONSE.fields_by_name['val_signing_info']._serialized_options = b'\310\336\037\000'
  _QUERYSIGNINGINFOSRESPONSE.fields_by_name['info']._options = None
  _QUERYSIGNINGINFOSRESPONSE.fields_by_name['info']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002!\022\037/cosmos/slashing/v1beta1/params'
  _QUERY.methods_by_name['SigningInfo']._options = None
  _QUERY.methods_by_name['SigningInfo']._serialized_options = b'\202\323\344\223\0027\0225/cosmos/slashing/v1beta1/signing_infos/{cons_address}'
  _QUERY.methods_by_name['SigningInfos']._options = None
  _QUERY.methods_by_name['SigningInfos']._serialized_options = b'\202\323\344\223\002(\022&/cosmos/slashing/v1beta1/signing_infos'
  _QUERYPARAMSREQUEST._serialized_start=200
  _QUERYPARAMSREQUEST._serialized_end=220
  _QUERYPARAMSRESPONSE._serialized_start=222
  _QUERYPARAMSRESPONSE._serialized_end=298
  _QUERYSIGNINGINFOREQUEST._serialized_start=300
  _QUERYSIGNINGINFOREQUEST._serialized_end=347
  _QUERYSIGNINGINFORESPONSE._serialized_start=349
  _QUERYSIGNINGINFORESPONSE._serialized_end=454
  _QUERYSIGNINGINFOSREQUEST._serialized_start=456
  _QUERYSIGNINGINFOSREQUEST._serialized_end=542
  _QUERYSIGNINGINFOSRESPONSE._serialized_start=545
  _QUERYSIGNINGINFOSRESPONSE._serialized_end=700
  _QUERY._serialized_start=703
  _QUERY._serialized_end=1201
# @@protoc_insertion_point(module_scope)
