# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/connection/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmospy.evmosproto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from evmospy.evmosproto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from evmospy.evmosproto.ibc.core.connection.v1 import connection_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2
from evmospy.evmosproto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from evmospy.evmosproto.google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"ibc/core/connection/v1/query.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/connection/v1/connection.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\"/\n\x16QueryConnectionRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\t\"\x9b\x01\n\x17QueryConnectionResponse\x12\x39\n\nconnection\x18\x01 \x01(\x0b\x32%.ibc.core.connection.v1.ConnectionEnd\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"U\n\x17QueryConnectionsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xcc\x01\n\x18QueryConnectionsResponse\x12\x41\n\x0b\x63onnections\x18\x01 \x03(\x0b\x32,.ibc.core.connection.v1.IdentifiedConnection\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\x12\x30\n\x06height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"2\n\x1dQueryClientConnectionsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\"\x81\x01\n\x1eQueryClientConnectionsResponse\x12\x18\n\x10\x63onnection_paths\x18\x01 \x03(\t\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"T\n!QueryConnectionClientStateRequest\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"\"\xb7\x01\n\"QueryConnectionClientStateResponse\x12J\n\x17identified_client_state\x18\x01 \x01(\x0b\x32).ibc.core.client.v1.IdentifiedClientState\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"\x89\x01\n$QueryConnectionConsensusStateRequest\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"\x12\x17\n\x0frevision_number\x18\x02 \x01(\x04\x12\x17\n\x0frevision_height\x18\x03 \x01(\x04\"\xb0\x01\n%QueryConnectionConsensusStateResponse\x12-\n\x0f\x63onsensus_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\r\n\x05proof\x18\x03 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x32\x8f\x08\n\x05Query\x12\xaa\x01\n\nConnection\x12..ibc.core.connection.v1.QueryConnectionRequest\x1a/.ibc.core.connection.v1.QueryConnectionResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/ibc/core/connection/v1/connections/{connection_id}\x12\x9d\x01\n\x0b\x43onnections\x12/.ibc.core.connection.v1.QueryConnectionsRequest\x1a\x30.ibc.core.connection.v1.QueryConnectionsResponse\"+\x82\xd3\xe4\x93\x02%\x12#/ibc/core/connection/v1/connections\x12\xc2\x01\n\x11\x43lientConnections\x12\x35.ibc.core.connection.v1.QueryClientConnectionsRequest\x1a\x36.ibc.core.connection.v1.QueryClientConnectionsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/ibc/core/connection/v1/client_connections/{client_id}\x12\xd8\x01\n\x15\x43onnectionClientState\x12\x39.ibc.core.connection.v1.QueryConnectionClientStateRequest\x1a:.ibc.core.connection.v1.QueryConnectionClientStateResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/ibc/core/connection/v1/connections/{connection_id}/client_state\x12\x98\x02\n\x18\x43onnectionConsensusState\x12<.ibc.core.connection.v1.QueryConnectionConsensusStateRequest\x1a=.ibc.core.connection.v1.QueryConnectionConsensusStateResponse\"\x7f\x82\xd3\xe4\x93\x02y\x12w/ibc/core/connection/v1/connections/{connection_id}/consensus_state/revision/{revision_number}/height/{revision_height}B>Z<github.com/cosmos/ibc-go/v3/modules/core/03-connection/typesb\x06proto3')



_QUERYCONNECTIONREQUEST = DESCRIPTOR.message_types_by_name['QueryConnectionRequest']
_QUERYCONNECTIONRESPONSE = DESCRIPTOR.message_types_by_name['QueryConnectionResponse']
_QUERYCONNECTIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryConnectionsRequest']
_QUERYCONNECTIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryConnectionsResponse']
_QUERYCLIENTCONNECTIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryClientConnectionsRequest']
_QUERYCLIENTCONNECTIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryClientConnectionsResponse']
_QUERYCONNECTIONCLIENTSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryConnectionClientStateRequest']
_QUERYCONNECTIONCLIENTSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryConnectionClientStateResponse']
_QUERYCONNECTIONCONSENSUSSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryConnectionConsensusStateRequest']
_QUERYCONNECTIONCONSENSUSSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryConnectionConsensusStateResponse']
QueryConnectionRequest = _reflection.GeneratedProtocolMessageType('QueryConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONNECTIONREQUEST,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryConnectionRequest)
  })
_sym_db.RegisterMessage(QueryConnectionRequest)

QueryConnectionResponse = _reflection.GeneratedProtocolMessageType('QueryConnectionResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONNECTIONRESPONSE,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryConnectionResponse)
  })
_sym_db.RegisterMessage(QueryConnectionResponse)

QueryConnectionsRequest = _reflection.GeneratedProtocolMessageType('QueryConnectionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONNECTIONSREQUEST,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryConnectionsRequest)
  })
_sym_db.RegisterMessage(QueryConnectionsRequest)

QueryConnectionsResponse = _reflection.GeneratedProtocolMessageType('QueryConnectionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONNECTIONSRESPONSE,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryConnectionsResponse)
  })
_sym_db.RegisterMessage(QueryConnectionsResponse)

QueryClientConnectionsRequest = _reflection.GeneratedProtocolMessageType('QueryClientConnectionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTCONNECTIONSREQUEST,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryClientConnectionsRequest)
  })
_sym_db.RegisterMessage(QueryClientConnectionsRequest)

QueryClientConnectionsResponse = _reflection.GeneratedProtocolMessageType('QueryClientConnectionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTCONNECTIONSRESPONSE,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryClientConnectionsResponse)
  })
_sym_db.RegisterMessage(QueryClientConnectionsResponse)

QueryConnectionClientStateRequest = _reflection.GeneratedProtocolMessageType('QueryConnectionClientStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONNECTIONCLIENTSTATEREQUEST,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryConnectionClientStateRequest)
  })
_sym_db.RegisterMessage(QueryConnectionClientStateRequest)

QueryConnectionClientStateResponse = _reflection.GeneratedProtocolMessageType('QueryConnectionClientStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONNECTIONCLIENTSTATERESPONSE,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryConnectionClientStateResponse)
  })
_sym_db.RegisterMessage(QueryConnectionClientStateResponse)

QueryConnectionConsensusStateRequest = _reflection.GeneratedProtocolMessageType('QueryConnectionConsensusStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONNECTIONCONSENSUSSTATEREQUEST,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryConnectionConsensusStateRequest)
  })
_sym_db.RegisterMessage(QueryConnectionConsensusStateRequest)

QueryConnectionConsensusStateResponse = _reflection.GeneratedProtocolMessageType('QueryConnectionConsensusStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONNECTIONCONSENSUSSTATERESPONSE,
  '__module__' : 'ibc.core.connection.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.QueryConnectionConsensusStateResponse)
  })
_sym_db.RegisterMessage(QueryConnectionConsensusStateResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z<github.com/cosmos/ibc-go/v3/modules/core/03-connection/types'
  _QUERYCONNECTIONRESPONSE.fields_by_name['proof_height']._options = None
  _QUERYCONNECTIONRESPONSE.fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _QUERYCONNECTIONSRESPONSE.fields_by_name['height']._options = None
  _QUERYCONNECTIONSRESPONSE.fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _QUERYCLIENTCONNECTIONSRESPONSE.fields_by_name['proof_height']._options = None
  _QUERYCLIENTCONNECTIONSRESPONSE.fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _QUERYCONNECTIONCLIENTSTATEREQUEST.fields_by_name['connection_id']._options = None
  _QUERYCONNECTIONCLIENTSTATEREQUEST.fields_by_name['connection_id']._serialized_options = b'\362\336\037\024yaml:\"connection_id\"'
  _QUERYCONNECTIONCLIENTSTATERESPONSE.fields_by_name['proof_height']._options = None
  _QUERYCONNECTIONCLIENTSTATERESPONSE.fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _QUERYCONNECTIONCONSENSUSSTATEREQUEST.fields_by_name['connection_id']._options = None
  _QUERYCONNECTIONCONSENSUSSTATEREQUEST.fields_by_name['connection_id']._serialized_options = b'\362\336\037\024yaml:\"connection_id\"'
  _QUERYCONNECTIONCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._options = None
  _QUERYCONNECTIONCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Connection']._options = None
  _QUERY.methods_by_name['Connection']._serialized_options = b'\202\323\344\223\0025\0223/ibc/core/connection/v1/connections/{connection_id}'
  _QUERY.methods_by_name['Connections']._options = None
  _QUERY.methods_by_name['Connections']._serialized_options = b'\202\323\344\223\002%\022#/ibc/core/connection/v1/connections'
  _QUERY.methods_by_name['ClientConnections']._options = None
  _QUERY.methods_by_name['ClientConnections']._serialized_options = b'\202\323\344\223\0028\0226/ibc/core/connection/v1/client_connections/{client_id}'
  _QUERY.methods_by_name['ConnectionClientState']._options = None
  _QUERY.methods_by_name['ConnectionClientState']._serialized_options = b'\202\323\344\223\002B\022@/ibc/core/connection/v1/connections/{connection_id}/client_state'
  _QUERY.methods_by_name['ConnectionConsensusState']._options = None
  _QUERY.methods_by_name['ConnectionConsensusState']._serialized_options = b'\202\323\344\223\002y\022w/ibc/core/connection/v1/connections/{connection_id}/consensus_state/revision/{revision_number}/height/{revision_height}'
  _QUERYCONNECTIONREQUEST._serialized_start=259
  _QUERYCONNECTIONREQUEST._serialized_end=306
  _QUERYCONNECTIONRESPONSE._serialized_start=309
  _QUERYCONNECTIONRESPONSE._serialized_end=464
  _QUERYCONNECTIONSREQUEST._serialized_start=466
  _QUERYCONNECTIONSREQUEST._serialized_end=551
  _QUERYCONNECTIONSRESPONSE._serialized_start=554
  _QUERYCONNECTIONSRESPONSE._serialized_end=758
  _QUERYCLIENTCONNECTIONSREQUEST._serialized_start=760
  _QUERYCLIENTCONNECTIONSREQUEST._serialized_end=810
  _QUERYCLIENTCONNECTIONSRESPONSE._serialized_start=813
  _QUERYCLIENTCONNECTIONSRESPONSE._serialized_end=942
  _QUERYCONNECTIONCLIENTSTATEREQUEST._serialized_start=944
  _QUERYCONNECTIONCLIENTSTATEREQUEST._serialized_end=1028
  _QUERYCONNECTIONCLIENTSTATERESPONSE._serialized_start=1031
  _QUERYCONNECTIONCLIENTSTATERESPONSE._serialized_end=1214
  _QUERYCONNECTIONCONSENSUSSTATEREQUEST._serialized_start=1217
  _QUERYCONNECTIONCONSENSUSSTATEREQUEST._serialized_end=1354
  _QUERYCONNECTIONCONSENSUSSTATERESPONSE._serialized_start=1357
  _QUERYCONNECTIONCONSENSUSSTATERESPONSE._serialized_end=1533
  _QUERY._serialized_start=1536
  _QUERY._serialized_end=2575
# @@protoc_insertion_point(module_scope)
