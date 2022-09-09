# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from evmospy.evmosproto.evmos.feesplit.v1 import tx_pb2 as evmos_dot_feesplit_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the fees Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterFeeSplit = channel.unary_unary(
                '/evmos.feesplit.v1.Msg/RegisterFeeSplit',
                request_serializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgRegisterFeeSplit.SerializeToString,
                response_deserializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgRegisterFeeSplitResponse.FromString,
                )
        self.UpdateFeeSplit = channel.unary_unary(
                '/evmos.feesplit.v1.Msg/UpdateFeeSplit',
                request_serializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgUpdateFeeSplit.SerializeToString,
                response_deserializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgUpdateFeeSplitResponse.FromString,
                )
        self.CancelFeeSplit = channel.unary_unary(
                '/evmos.feesplit.v1.Msg/CancelFeeSplit',
                request_serializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgCancelFeeSplit.SerializeToString,
                response_deserializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgCancelFeeSplitResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the fees Msg service.
    """

    def RegisterFeeSplit(self, request, context):
        """RegisterFeeSplit registers a new contract for receiving transaction fees
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFeeSplit(self, request, context):
        """UpdateFeeSplit updates the withdrawer address of a fee split
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelFeeSplit(self, request, context):
        """CancelFeeSplit cancels a contract's fee registration and further receival
        of transaction fees
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterFeeSplit': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterFeeSplit,
                    request_deserializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgRegisterFeeSplit.FromString,
                    response_serializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgRegisterFeeSplitResponse.SerializeToString,
            ),
            'UpdateFeeSplit': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFeeSplit,
                    request_deserializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgUpdateFeeSplit.FromString,
                    response_serializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgUpdateFeeSplitResponse.SerializeToString,
            ),
            'CancelFeeSplit': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelFeeSplit,
                    request_deserializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgCancelFeeSplit.FromString,
                    response_serializer=evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgCancelFeeSplitResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'evmos.feesplit.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the fees Msg service.
    """

    @staticmethod
    def RegisterFeeSplit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.feesplit.v1.Msg/RegisterFeeSplit',
            evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgRegisterFeeSplit.SerializeToString,
            evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgRegisterFeeSplitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFeeSplit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.feesplit.v1.Msg/UpdateFeeSplit',
            evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgUpdateFeeSplit.SerializeToString,
            evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgUpdateFeeSplitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelFeeSplit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.feesplit.v1.Msg/CancelFeeSplit',
            evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgCancelFeeSplit.SerializeToString,
            evmos_dot_feesplit_dot_v1_dot_tx__pb2.MsgCancelFeeSplitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)