import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class PerformanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()
        response = self.get_response(request)
        time_taken = time.time() - start_time
        time_taken = round(time_taken, 4)

        response.headers["time-taken"] = time_taken

        logger.info(
            f"API Path: {request.path_info}, method:"
            f" {request.method}, user: {request.user.pk}, time_taken: {time_taken}"
        )
        return response