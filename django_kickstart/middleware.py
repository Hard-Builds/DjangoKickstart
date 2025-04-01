import time


class PerformanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        response = self.get_response(*args, **kwargs)
        time_taken = time.time() - start_time
        time_taken = round(time_taken, 4)

        response.headers["time_taken"] = time_taken

        return response
