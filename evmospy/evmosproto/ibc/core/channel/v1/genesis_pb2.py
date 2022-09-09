# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/channel/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmospy.evmosproto.ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/core/channel/v1/genesis.proto\x12\x13ibc.core.channel.v1\x1a\x14gogoproto/gogo.proto\x1a!ibc/core/channel/v1/channel.proto\"\xef\x04\n\x0cGenesisState\x12S\n\x08\x63hannels\x18\x01 \x03(\x0b\x32&.ibc.core.channel.v1.IdentifiedChannelB\x19\xfa\xde\x1f\x11IdentifiedChannel\xc8\xde\x1f\x00\x12@\n\x10\x61\x63knowledgements\x18\x02 \x03(\x0b\x32 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00\x12;\n\x0b\x63ommitments\x18\x03 \x03(\x0b\x32 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00\x12\x38\n\x08receipts\x18\x04 \x03(\x0b\x32 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00\x12Z\n\x0esend_sequences\x18\x05 \x03(\x0b\x32#.ibc.core.channel.v1.PacketSequenceB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:\"send_sequences\"\x12Z\n\x0erecv_sequences\x18\x06 \x03(\x0b\x32#.ibc.core.channel.v1.PacketSequenceB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:\"recv_sequences\"\x12X\n\rack_sequences\x18\x07 \x03(\x0b\x32#.ibc.core.channel.v1.PacketSequenceB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:\"ack_sequences\"\x12?\n\x15next_channel_sequence\x18\x08 \x01(\x04\x42 \xf2\xde\x1f\x1cyaml:\"next_channel_sequence\"\"r\n\x0ePacketSequence\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x42;Z9github.com/cosmos/ibc-go/v3/modules/core/04-channel/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_PACKETSEQUENCE = DESCRIPTOR.message_types_by_name['PacketSequence']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'ibc.core.channel.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

PacketSequence = _reflection.GeneratedProtocolMessageType('PacketSequence', (_message.Message,), {
  'DESCRIPTOR' : _PACKETSEQUENCE,
  '__module__' : 'ibc.core.channel.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.PacketSequence)
  })
_sym_db.RegisterMessage(PacketSequence)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/cosmos/ibc-go/v3/modules/core/04-channel/types'
  _GENESISSTATE.fields_by_name['channels']._options = None
  _GENESISSTATE.fields_by_name['channels']._serialized_options = b'\372\336\037\021IdentifiedChannel\310\336\037\000'
  _GENESISSTATE.fields_by_name['acknowledgements']._options = None
  _GENESISSTATE.fields_by_name['acknowledgements']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['commitments']._options = None
  _GENESISSTATE.fields_by_name['commitments']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['receipts']._options = None
  _GENESISSTATE.fields_by_name['receipts']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['send_sequences']._options = None
  _GENESISSTATE.fields_by_name['send_sequences']._serialized_options = b'\310\336\037\000\362\336\037\025yaml:\"send_sequences\"'
  _GENESISSTATE.fields_by_name['recv_sequences']._options = None
  _GENESISSTATE.fields_by_name['recv_sequences']._serialized_options = b'\310\336\037\000\362\336\037\025yaml:\"recv_sequences\"'
  _GENESISSTATE.fields_by_name['ack_sequences']._options = None
  _GENESISSTATE.fields_by_name['ack_sequences']._serialized_options = b'\310\336\037\000\362\336\037\024yaml:\"ack_sequences\"'
  _GENESISSTATE.fields_by_name['next_channel_sequence']._options = None
  _GENESISSTATE.fields_by_name['next_channel_sequence']._serialized_options = b'\362\336\037\034yaml:\"next_channel_sequence\"'
  _PACKETSEQUENCE.fields_by_name['port_id']._options = None
  _PACKETSEQUENCE.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _PACKETSEQUENCE.fields_by_name['channel_id']._options = None
  _PACKETSEQUENCE.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _GENESISSTATE._serialized_start=116
  _GENESISSTATE._serialized_end=739
  _PACKETSEQUENCE._serialized_start=741
  _PACKETSEQUENCE._serialized_end=855
# @@protoc_insertion_point(module_scope)
