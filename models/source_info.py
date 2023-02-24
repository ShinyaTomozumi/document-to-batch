from typing import List
from models.batch_info import BatchInfo


class SourceInfo:
    """
    ソースコードの情報
    """
    project_name: str   # プロジェクト名
    author_name: str    # ソース作成者
    copy_right: str   # ソースのコピーライト
    version: str    # ドキュメントのバージョン
    batch_items: List[BatchInfo]    # バッチ情報

    def __init__(self):
        """
        初期化
        """
        self.project_name = ''
        self.author_name = ''
        self.copy_right = ''
        self.version = ''
        self.batch_items = []
