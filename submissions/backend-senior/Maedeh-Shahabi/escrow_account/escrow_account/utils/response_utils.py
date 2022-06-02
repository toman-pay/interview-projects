from typing import Optional, Dict, Any

from escrow_account.base_constants import BaseConstants


class ResponseUtils:

    @staticmethod
    def get_create_response_data(success: bool, id_: Optional[str], data: dict) -> Dict[str, Any]:
        return {
            BaseConstants.success: success,
            BaseConstants.id_: id_,
            BaseConstants.data: data,
        }
