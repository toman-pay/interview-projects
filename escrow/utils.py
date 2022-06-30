from typing import Optional, Dict, Any


def create_response_data(success: bool, id: Optional[str], data: dict) -> Dict[str, Any]:
    return dict(success=success, data=data, id=id)
