class ParameterConfig:
    """
    コマンドで受け取ったパラメータの設定
    """
    input_files_path: str  # 取り込むファイルのパス
    output_dir_path: str  # 書き出すフォルダの名称
    project_type: str  # 作成するバッチのソースコードの種類
    document_type: str  # 読み込むドキュメントの種類

    def __init__(self):
        self.input_files_path = ''  # 取り込むファイルのパス
        self.output_dir_path = ''  # 書き出すフォルダの名称
        self.project_type = ''  # 作成するバッチのソースコードの種類
        self.document_type = 'excel'  # 読み込むドキュメントの種類
