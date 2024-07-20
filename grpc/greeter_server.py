from concurrent import futures
import grpc
import generate_pb2
import generate_pb2_grpc


class summer(generate_pb2_grpc.summerServicer):
    def SumNum(self, request, context):
        return generate_pb2.SumRequest(request.x, request.y)

    # def FactNum(self, request, context):
    #     return generate_pb2.FactRequest(reply=f"Goodbye, {request.name}!")


def server():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    generate_pb2_grpc.add_summerServicer_to_server(summer(), server)
    server.add_insecure_port("0.0.0.0:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


server()
