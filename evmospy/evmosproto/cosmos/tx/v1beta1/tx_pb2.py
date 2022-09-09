# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/tx/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmospy.evmosproto.cosmos.crypto.multisig.v1beta1 import multisig_pb2 as cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2
from evmospy.evmosproto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from evmospy.evmosproto.cosmos.tx.signing.v1beta1 import signing_pb2 as cosmos_dot_tx_dot_signing_dot_v1beta1_dot_signing__pb2
from evmospy.evmosproto.google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63osmos/tx/v1beta1/tx.proto\x12\x11\x63osmos.tx.v1beta1\x1a\x14gogoproto/gogo.proto\x1a-cosmos/crypto/multisig/v1beta1/multisig.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\'cosmos/tx/signing/v1beta1/signing.proto\x1a\x19google/protobuf/any.proto\"q\n\x02Tx\x12\'\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x19.cosmos.tx.v1beta1.TxBody\x12.\n\tauth_info\x18\x02 \x01(\x0b\x32\x1b.cosmos.tx.v1beta1.AuthInfo\x12\x12\n\nsignatures\x18\x03 \x03(\x0c\"H\n\x05TxRaw\x12\x12\n\nbody_bytes\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61uth_info_bytes\x18\x02 \x01(\x0c\x12\x12\n\nsignatures\x18\x03 \x03(\x0c\"`\n\x07SignDoc\x12\x12\n\nbody_bytes\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61uth_info_bytes\x18\x02 \x01(\x0c\x12\x10\n\x08\x63hain_id\x18\x03 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x04 \x01(\x04\"\xc7\x01\n\x06TxBody\x12&\n\x08messages\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04memo\x18\x02 \x01(\t\x12\x16\n\x0etimeout_height\x18\x03 \x01(\x04\x12\x30\n\x11\x65xtension_options\x18\xff\x07 \x03(\x0b\x32\x14.google.protobuf.Any\x12=\n\x1enon_critical_extension_options\x18\xff\x0f \x03(\x0b\x32\x14.google.protobuf.Any\"d\n\x08\x41uthInfo\x12\x33\n\x0csigner_infos\x18\x01 \x03(\x0b\x32\x1d.cosmos.tx.v1beta1.SignerInfo\x12#\n\x03\x66\x65\x65\x18\x02 \x01(\x0b\x32\x16.cosmos.tx.v1beta1.Fee\"x\n\nSignerInfo\x12(\n\npublic_key\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12.\n\tmode_info\x18\x02 \x01(\x0b\x32\x1b.cosmos.tx.v1beta1.ModeInfo\x12\x10\n\x08sequence\x18\x03 \x01(\x04\"\xb5\x02\n\x08ModeInfo\x12\x34\n\x06single\x18\x01 \x01(\x0b\x32\".cosmos.tx.v1beta1.ModeInfo.SingleH\x00\x12\x32\n\x05multi\x18\x02 \x01(\x0b\x32!.cosmos.tx.v1beta1.ModeInfo.MultiH\x00\x1a;\n\x06Single\x12\x31\n\x04mode\x18\x01 \x01(\x0e\x32#.cosmos.tx.signing.v1beta1.SignMode\x1a{\n\x05Multi\x12\x41\n\x08\x62itarray\x18\x01 \x01(\x0b\x32/.cosmos.crypto.multisig.v1beta1.CompactBitArray\x12/\n\nmode_infos\x18\x02 \x03(\x0b\x32\x1b.cosmos.tx.v1beta1.ModeInfoB\x05\n\x03sum\"\x95\x01\n\x03\x46\x65\x65\x12[\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x11\n\tgas_limit\x18\x02 \x01(\x04\x12\r\n\x05payer\x18\x03 \x01(\t\x12\x0f\n\x07granter\x18\x04 \x01(\tB\'Z%github.com/cosmos/cosmos-sdk/types/txb\x06proto3')



_TX = DESCRIPTOR.message_types_by_name['Tx']
_TXRAW = DESCRIPTOR.message_types_by_name['TxRaw']
_SIGNDOC = DESCRIPTOR.message_types_by_name['SignDoc']
_TXBODY = DESCRIPTOR.message_types_by_name['TxBody']
_AUTHINFO = DESCRIPTOR.message_types_by_name['AuthInfo']
_SIGNERINFO = DESCRIPTOR.message_types_by_name['SignerInfo']
_MODEINFO = DESCRIPTOR.message_types_by_name['ModeInfo']
_MODEINFO_SINGLE = _MODEINFO.nested_types_by_name['Single']
_MODEINFO_MULTI = _MODEINFO.nested_types_by_name['Multi']
_FEE = DESCRIPTOR.message_types_by_name['Fee']
Tx = _reflection.GeneratedProtocolMessageType('Tx', (_message.Message,), {
  'DESCRIPTOR' : _TX,
  '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.Tx)
  })
_sym_db.RegisterMessage(Tx)

TxRaw = _reflection.GeneratedProtocolMessageType('TxRaw', (_message.Message,), {
  'DESCRIPTOR' : _TXRAW,
  '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.TxRaw)
  })
_sym_db.RegisterMessage(TxRaw)

SignDoc = _reflection.GeneratedProtocolMessageType('SignDoc', (_message.Message,), {
  'DESCRIPTOR' : _SIGNDOC,
  '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.SignDoc)
  })
_sym_db.RegisterMessage(SignDoc)

TxBody = _reflection.GeneratedProtocolMessageType('TxBody', (_message.Message,), {
  'DESCRIPTOR' : _TXBODY,
  '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.TxBody)
  })
_sym_db.RegisterMessage(TxBody)

AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), {
  'DESCRIPTOR' : _AUTHINFO,
  '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.AuthInfo)
  })
_sym_db.RegisterMessage(AuthInfo)

SignerInfo = _reflection.GeneratedProtocolMessageType('SignerInfo', (_message.Message,), {
  'DESCRIPTOR' : _SIGNERINFO,
  '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.SignerInfo)
  })
_sym_db.RegisterMessage(SignerInfo)

ModeInfo = _reflection.GeneratedProtocolMessageType('ModeInfo', (_message.Message,), {

  'Single' : _reflection.GeneratedProtocolMessageType('Single', (_message.Message,), {
    'DESCRIPTOR' : _MODEINFO_SINGLE,
    '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
    # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.ModeInfo.Single)
    })
  ,

  'Multi' : _reflection.GeneratedProtocolMessageType('Multi', (_message.Message,), {
    'DESCRIPTOR' : _MODEINFO_MULTI,
    '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
    # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.ModeInfo.Multi)
    })
  ,
  'DESCRIPTOR' : _MODEINFO,
  '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.ModeInfo)
  })
_sym_db.RegisterMessage(ModeInfo)
_sym_db.RegisterMessage(ModeInfo.Single)
_sym_db.RegisterMessage(ModeInfo.Multi)

Fee = _reflection.GeneratedProtocolMessageType('Fee', (_message.Message,), {
  'DESCRIPTOR' : _FEE,
  '__module__' : 'cosmos.tx.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.v1beta1.Fee)
  })
_sym_db.RegisterMessage(Fee)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/tx'
  _FEE.fields_by_name['amount']._options = None
  _FEE.fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _TX._serialized_start=218
  _TX._serialized_end=331
  _TXRAW._serialized_start=333
  _TXRAW._serialized_end=405
  _SIGNDOC._serialized_start=407
  _SIGNDOC._serialized_end=503
  _TXBODY._serialized_start=506
  _TXBODY._serialized_end=705
  _AUTHINFO._serialized_start=707
  _AUTHINFO._serialized_end=807
  _SIGNERINFO._serialized_start=809
  _SIGNERINFO._serialized_end=929
  _MODEINFO._serialized_start=932
  _MODEINFO._serialized_end=1241
  _MODEINFO_SINGLE._serialized_start=1050
  _MODEINFO_SINGLE._serialized_end=1109
  _MODEINFO_MULTI._serialized_start=1111
  _MODEINFO_MULTI._serialized_end=1234
  _FEE._serialized_start=1244
  _FEE._serialized_end=1393
# @@protoc_insertion_point(module_scope)
