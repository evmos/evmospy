# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from evmospy.evmosproto.google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmospy.evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmospy.evmosproto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from evmospy.evmosproto.cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/distribution/v1beta1/genesis.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\"\x91\x01\n\x15\x44\x65legatorWithdrawInfo\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"delegator_address\"\x12\x35\n\x10withdraw_address\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:\"withdraw_address\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xf5\x01\n!ValidatorOutstandingRewardsRecord\x12\x37\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12\x8c\x01\n\x13outstanding_rewards\x18\x02 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBQ\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:\"outstanding_rewards\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xd7\x01\n$ValidatorAccumulatedCommissionRecord\x12\x37\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12l\n\x0b\x61\x63\x63umulated\x18\x02 \x01(\x0b\x32;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:\"accumulated\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xd7\x01\n ValidatorHistoricalRewardsRecord\x12\x37\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12\x0e\n\x06period\x18\x02 \x01(\x04\x12`\n\x07rewards\x18\x03 \x01(\x0b\x32\x37.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsB\x16\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:\"rewards\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xc1\x01\n\x1dValidatorCurrentRewardsRecord\x12\x37\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12]\n\x07rewards\x18\x02 \x01(\x0b\x32\x34.cosmos.distribution.v1beta1.ValidatorCurrentRewardsB\x16\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:\"rewards\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x82\x02\n\x1b\x44\x65legatorStartingInfoRecord\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"delegator_address\"\x12\x37\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12g\n\rstarting_info\x18\x03 \x01(\x0b\x32\x32.cosmos.distribution.v1beta1.DelegatorStartingInfoB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:\"starting_info\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xe5\x01\n\x19ValidatorSlashEventRecord\x12\x37\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x0e\n\x06period\x18\x03 \x01(\x04\x12\x65\n\x15validator_slash_event\x18\x04 \x01(\x0b\x32\x30.cosmos.distribution.v1beta1.ValidatorSlashEventB\x14\xc8\xde\x1f\x00\xf2\xde\x1f\x0cyaml:\"event\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb1\t\n\x0cGenesisState\x12J\n\x06params\x18\x01 \x01(\x0b\x32#.cosmos.distribution.v1beta1.ParamsB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:\"params\"\x12O\n\x08\x66\x65\x65_pool\x18\x02 \x01(\x0b\x32$.cosmos.distribution.v1beta1.FeePoolB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"fee_pool\"\x12}\n\x18\x64\x65legator_withdraw_infos\x18\x03 \x03(\x0b\x32\x32.cosmos.distribution.v1beta1.DelegatorWithdrawInfoB\'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:\"delegator_withdraw_infos\"\x12\x37\n\x11previous_proposer\x18\x04 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"previous_proposer\"\x12\x7f\n\x13outstanding_rewards\x18\x05 \x03(\x0b\x32>.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecordB\"\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:\"outstanding_rewards\"\x12\x9e\x01\n!validator_accumulated_commissions\x18\x06 \x03(\x0b\x32\x41.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecordB0\xc8\xde\x1f\x00\xf2\xde\x1f(yaml:\"validator_accumulated_commissions\"\x12\x90\x01\n\x1cvalidator_historical_rewards\x18\x07 \x03(\x0b\x32=.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecordB+\xc8\xde\x1f\x00\xf2\xde\x1f#yaml:\"validator_historical_rewards\"\x12\x87\x01\n\x19validator_current_rewards\x18\x08 \x03(\x0b\x32:.cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecordB(\xc8\xde\x1f\x00\xf2\xde\x1f yaml:\"validator_current_rewards\"\x12\x83\x01\n\x18\x64\x65legator_starting_infos\x18\t \x03(\x0b\x32\x38.cosmos.distribution.v1beta1.DelegatorStartingInfoRecordB\'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:\"delegator_starting_infos\"\x12}\n\x16validator_slash_events\x18\n \x03(\x0b\x32\x36.cosmos.distribution.v1beta1.ValidatorSlashEventRecordB%\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:\"validator_slash_events\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42\x37Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3')



_DELEGATORWITHDRAWINFO = DESCRIPTOR.message_types_by_name['DelegatorWithdrawInfo']
_VALIDATOROUTSTANDINGREWARDSRECORD = DESCRIPTOR.message_types_by_name['ValidatorOutstandingRewardsRecord']
_VALIDATORACCUMULATEDCOMMISSIONRECORD = DESCRIPTOR.message_types_by_name['ValidatorAccumulatedCommissionRecord']
_VALIDATORHISTORICALREWARDSRECORD = DESCRIPTOR.message_types_by_name['ValidatorHistoricalRewardsRecord']
_VALIDATORCURRENTREWARDSRECORD = DESCRIPTOR.message_types_by_name['ValidatorCurrentRewardsRecord']
_DELEGATORSTARTINGINFORECORD = DESCRIPTOR.message_types_by_name['DelegatorStartingInfoRecord']
_VALIDATORSLASHEVENTRECORD = DESCRIPTOR.message_types_by_name['ValidatorSlashEventRecord']
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
DelegatorWithdrawInfo = _reflection.GeneratedProtocolMessageType('DelegatorWithdrawInfo', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATORWITHDRAWINFO,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegatorWithdrawInfo)
  })
_sym_db.RegisterMessage(DelegatorWithdrawInfo)

ValidatorOutstandingRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorOutstandingRewardsRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATOROUTSTANDINGREWARDSRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecord)
  })
_sym_db.RegisterMessage(ValidatorOutstandingRewardsRecord)

ValidatorAccumulatedCommissionRecord = _reflection.GeneratedProtocolMessageType('ValidatorAccumulatedCommissionRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORACCUMULATEDCOMMISSIONRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecord)
  })
_sym_db.RegisterMessage(ValidatorAccumulatedCommissionRecord)

ValidatorHistoricalRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorHistoricalRewardsRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORHISTORICALREWARDSRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecord)
  })
_sym_db.RegisterMessage(ValidatorHistoricalRewardsRecord)

ValidatorCurrentRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorCurrentRewardsRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORCURRENTREWARDSRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecord)
  })
_sym_db.RegisterMessage(ValidatorCurrentRewardsRecord)

DelegatorStartingInfoRecord = _reflection.GeneratedProtocolMessageType('DelegatorStartingInfoRecord', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATORSTARTINGINFORECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegatorStartingInfoRecord)
  })
_sym_db.RegisterMessage(DelegatorStartingInfoRecord)

ValidatorSlashEventRecord = _reflection.GeneratedProtocolMessageType('ValidatorSlashEventRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORSLASHEVENTRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorSlashEventRecord)
  })
_sym_db.RegisterMessage(ValidatorSlashEventRecord)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001'
  _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._options = None
  _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._serialized_options = b'\362\336\037\030yaml:\"delegator_address\"'
  _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._options = None
  _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._serialized_options = b'\362\336\037\027yaml:\"withdraw_address\"'
  _DELEGATORWITHDRAWINFO._options = None
  _DELEGATORWITHDRAWINFO._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._options = None
  _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._options = None
  _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._serialized_options = b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000\362\336\037\032yaml:\"outstanding_rewards\"'
  _VALIDATOROUTSTANDINGREWARDSRECORD._options = None
  _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._options = None
  _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._options = None
  _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._serialized_options = b'\310\336\037\000\362\336\037\022yaml:\"accumulated\"'
  _VALIDATORACCUMULATEDCOMMISSIONRECORD._options = None
  _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._options = None
  _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._options = None
  _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\310\336\037\000\362\336\037\016yaml:\"rewards\"'
  _VALIDATORHISTORICALREWARDSRECORD._options = None
  _VALIDATORHISTORICALREWARDSRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._options = None
  _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._options = None
  _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\310\336\037\000\362\336\037\016yaml:\"rewards\"'
  _VALIDATORCURRENTREWARDSRECORD._options = None
  _VALIDATORCURRENTREWARDSRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._options = None
  _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._serialized_options = b'\362\336\037\030yaml:\"delegator_address\"'
  _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._options = None
  _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._options = None
  _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._serialized_options = b'\310\336\037\000\362\336\037\024yaml:\"starting_info\"'
  _DELEGATORSTARTINGINFORECORD._options = None
  _DELEGATORSTARTINGINFORECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._options = None
  _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._options = None
  _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._serialized_options = b'\310\336\037\000\362\336\037\014yaml:\"event\"'
  _VALIDATORSLASHEVENTRECORD._options = None
  _VALIDATORSLASHEVENTRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000\362\336\037\ryaml:\"params\"'
  _GENESISSTATE.fields_by_name['fee_pool']._options = None
  _GENESISSTATE.fields_by_name['fee_pool']._serialized_options = b'\310\336\037\000\362\336\037\017yaml:\"fee_pool\"'
  _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._options = None
  _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._serialized_options = b'\310\336\037\000\362\336\037\037yaml:\"delegator_withdraw_infos\"'
  _GENESISSTATE.fields_by_name['previous_proposer']._options = None
  _GENESISSTATE.fields_by_name['previous_proposer']._serialized_options = b'\362\336\037\030yaml:\"previous_proposer\"'
  _GENESISSTATE.fields_by_name['outstanding_rewards']._options = None
  _GENESISSTATE.fields_by_name['outstanding_rewards']._serialized_options = b'\310\336\037\000\362\336\037\032yaml:\"outstanding_rewards\"'
  _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._options = None
  _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._serialized_options = b'\310\336\037\000\362\336\037(yaml:\"validator_accumulated_commissions\"'
  _GENESISSTATE.fields_by_name['validator_historical_rewards']._options = None
  _GENESISSTATE.fields_by_name['validator_historical_rewards']._serialized_options = b'\310\336\037\000\362\336\037#yaml:\"validator_historical_rewards\"'
  _GENESISSTATE.fields_by_name['validator_current_rewards']._options = None
  _GENESISSTATE.fields_by_name['validator_current_rewards']._serialized_options = b'\310\336\037\000\362\336\037 yaml:\"validator_current_rewards\"'
  _GENESISSTATE.fields_by_name['delegator_starting_infos']._options = None
  _GENESISSTATE.fields_by_name['delegator_starting_infos']._serialized_options = b'\310\336\037\000\362\336\037\037yaml:\"delegator_starting_infos\"'
  _GENESISSTATE.fields_by_name['validator_slash_events']._options = None
  _GENESISSTATE.fields_by_name['validator_slash_events']._serialized_options = b'\310\336\037\000\362\336\037\035yaml:\"validator_slash_events\"'
  _GENESISSTATE._options = None
  _GENESISSTATE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _DELEGATORWITHDRAWINFO._serialized_start=177
  _DELEGATORWITHDRAWINFO._serialized_end=322
  _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_start=325
  _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_end=570
  _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_start=573
  _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_end=788
  _VALIDATORHISTORICALREWARDSRECORD._serialized_start=791
  _VALIDATORHISTORICALREWARDSRECORD._serialized_end=1006
  _VALIDATORCURRENTREWARDSRECORD._serialized_start=1009
  _VALIDATORCURRENTREWARDSRECORD._serialized_end=1202
  _DELEGATORSTARTINGINFORECORD._serialized_start=1205
  _DELEGATORSTARTINGINFORECORD._serialized_end=1463
  _VALIDATORSLASHEVENTRECORD._serialized_start=1466
  _VALIDATORSLASHEVENTRECORD._serialized_end=1695
  _GENESISSTATE._serialized_start=1698
  _GENESISSTATE._serialized_end=2899
# @@protoc_insertion_point(module_scope)
