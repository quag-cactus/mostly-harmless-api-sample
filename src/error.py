class ApiError(Exception):
    """ エラーの基底となるクラス """
    status_code: int = 400
    detail: str = 'API error'  # エラー概要

class IDNotFoundError(ApiError):
    status_code: int = 404
    detail: str = "該当するIDのQuaggyは存在しません"