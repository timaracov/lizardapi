class JsonResponse:
    def __init__(self, data: dict | list, status: int = 200) -> None:
        self.data = data
        self.status = status
