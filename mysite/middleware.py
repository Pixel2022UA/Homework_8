import time


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        execution_time = time.time() - start_time

        log_message = f"{request.method} request to {request.path} took {round(execution_time, 6)} seconds\n"

        with open("log_file.txt", "a") as log_file:
            log_file.write(log_message)

        return response
