from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc
import time
import logging
import sys

logger = logging.getLogger(__name__)


def run(grpcserver):
  channel = grpc.insecure_channel(grpcserver)
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  while True:
    try:
      response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
      logger.error("Greeter client received: " + response.message)
      time.sleep(3)
    except Exception as e:
      logger.error('Could not connect load-balancer. error {}'.format(e))
      time.sleep(3)

if __name__ == '__main__':
  run(sys.argv[1])
