import grpc
import generate_pb2
import generate_pb2_grpc

print("Will try to greet world ...")

with grpc.insecure_channel("localhost:50051") as channel:
    stub = generate_pb2_grpc.summerStub(channel)
    response = stub.SumNum(generate_pb2.SumRequest(x=5, y=10))
    # response2 = stub.SayGoodbye(generate_pb2.GreetRequest(name="Bob"))
    # response3 = stub.
# print("Greeter client received: " + response.reply)
# print("Greeter client received: " + response2.reply)
