class BatchInfo:
    """
    バッチのソースコードに関する情報
    """
    id: str     # バッチID
    summary: str    # 概要
    description: str    # 概要
    timing: str     # 実行タイミング
    remark: str     # 備考

    def __init__(self):
        """
        初期化
        """
        self.id = ''
        self.summary = ''
        self.description = ''
        self.timing = ''
        self.remark = ''
