from datetime import datetime

class HistoryRepository:
    """Small persistence abstraction; production deployments can replace this with SQLAlchemy models."""

    def __init__(self):
        self.items = []

    def save(self, operation: str, payload: str, result: str):
        item = {"operation": operation, "payload": payload, "result": result, "created_at": datetime.utcnow().isoformat()}
        self.items.append(item)
        return item
