import openpyxl
from openpyxl import Workbook

from models.parameter_config import ParameterConfig
from models.source_info import SourceInfo
from models.batch_info import BatchInfo


class ImportExcel(SourceInfo):
    """
    エクセルのインポート処理
    """

    def __init__(self, parameter_config: ParameterConfig):
        """
        初期化処理
        :param parameter_config:
        """
        # 基底クラスの初期化
        super().__init__()

        # エクセル情報の取り込み
        _exel_info: Workbook = openpyxl.load_workbook(parameter_config.input_files_path)

        # 「全ての属性」からテーブル情報を取得する
        sheet = _exel_info['Batch']
        if sheet is None:
            return

        # すべてのセルを読み込む(ヘッダーと説明部は読み込まないため2から開始する)
        for row_num in range(3, sheet.max_row + 1):
            # バッチ情報を初期化する
            batch_info = BatchInfo()

            # エクセルから読み取った情報
            batch_info.id = sheet['A' + str(row_num)].value  # バッチID
            if batch_info.id is None:
                print('ID required be set\nRow number:' + str(row_num))
                continue
            batch_info.summary = sheet['B' + str(row_num)].value  # 概要
            if batch_info.summary is None:
                print('Summary required be set.\nRow number:' + str(row_num))
                continue
            batch_info.description = sheet['C' + str(row_num)].value  # 説明
            if batch_info.description is None:
                print('Description required be set.\nRow number:' + str(row_num))
                continue
            batch_info.timing = sheet['D' + str(row_num)].value  # 実行時間
            batch_info.remark = sheet['E' + str(row_num)].value  # 備考

            # バッチ情報を追加する
            self.batch_items.append(batch_info)
