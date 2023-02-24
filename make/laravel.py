import datetime
import os
import shutil

from models.parameter_config import ParameterConfig
from models.source_info import SourceInfo


class Laravel:
    """
    Laravelのバッチ処理ソースコードを作成する
    """
    _parameter_config: ParameterConfig
    _source_info: SourceInfo
    _template_dir: str
    _SOURCE_TYPE = 'laravel'

    def __init__(self, parameter_config: ParameterConfig, source_info: SourceInfo):
        """
        クラスの初期化
        :param parameter_config:
        :param source_info:
        """
        # 変数の設定
        # 出力先のフォルダの初期化設定
        self._parameter_config = parameter_config
        if self._parameter_config.output_dir_path == '':
            self._parameter_config.output_dir_path = 'output_batch_' + self._SOURCE_TYPE
        # テンプレートソースのフォルダを指定する
        self._template_dir = os.path.dirname(__file__) + '/../template/' + self._SOURCE_TYPE
        # ソースコード情報を定義する
        self._source_info = source_info

    def make(self):
        """
        ソースコードを作成する
        :return:
        """
        # 既に作成したフォルダがあれば削除する
        if os.path.isdir(self._parameter_config.output_dir_path):
            shutil.rmtree(self._parameter_config.output_dir_path)

        # 「batch」情報が無ければ、エラーメッセージを表示してエラーを返却する。
        if len(self._source_info.batch_items) == 0:
            print('There was no "batch" in the loaded document.')
            return

        # 各バッチコマンドソースコードを作成する
        self._make_command()

        # 「Kernel.php」のソースコードを作成する
        self._make_kernel()

    def _make_command(self):
        """
        各バッチコマンドソースコードを作成する
        :return:
        """
        # 保存先のフォルダを作成する
        output_dirs = self._parameter_config.output_dir_path + '/app/Console/Commands'
        os.makedirs(output_dirs, exist_ok=True)

        # バッチごとにphpファイルを作成する
        for batch_item in self._source_info.batch_items:

            # ファイル名を設定する
            batch_class_name = batch_item.id

            # 各種バッチファイルの初期化
            source_file = open(output_dirs + '/' + batch_class_name + '.php', 'w')

            # バッチのテンプレートソースコードを読み込む
            template_file = open(self._template_dir + '/commands.php', 'r')
            template_source = template_file.read()

            # バージョンに現在時刻を設定する
            current_time = datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
            template_source = template_source.replace('__version__', current_time)

            # クラス名を設定する
            template_source = template_source.replace('__class_name__', batch_class_name)

            # 概要を設定する
            summary = batch_item.summary.replace('\n', ' ')
            template_source = template_source.replace('__summary__', summary)

            # 説明を設定する
            comment = batch_item.description.replace('\n', '\n     * ')
            template_source = template_source.replace('__comment__', comment)

            # 実行タイミングが記載されていた場合は、タイミングを記載する
            if batch_item.timing is not None:
                timing = batch_item.timing.replace('\n', '\n     * ')
                template_source = template_source.replace('__timing__', '\n     * バッチ実行時間: ' + timing)
            else:
                template_source = template_source.replace('__timing__', '')

            # 備考が記載されたいた場合に、備考コメントを記載する
            if batch_item.remark is not None:
                remark = batch_item.remark.replace('\n', '\n     * ')
                template_source = template_source.replace('__remark__', '\n     * 備考: ' + remark)
            else:
                template_source = template_source.replace('__remark__', '')

            # Commands.phpファイルにソースコードを書き込む
            source_file.write(template_source)
            source_file.close()

    def _make_kernel(self):
        """
        「Kernel.php」を作成する
        :return:
        """
        # ファイルの出力先
        output_dirs = self._parameter_config.output_dir_path + '/app/Console'

        # 「Kernel.php」に追記するコードを記載
        commands = []
        batches = []

        # ViewごとにControllerファイルを作成する
        for batch_item in self._source_info.batch_items:

            # クラスメイを作成する
            batch_class_name = batch_item.id

            # 概要を設定する
            summary = batch_item.summary.replace('\n', ' ')

            # 「Kernel.php」に記載するソースコードを構築する
            source_commands = '         \\App\\Console\\Commands\\' + batch_class_name + '::class,'
            commands.append(source_commands)

            # タイミングが設定されていた場合は、実行処理のコードを設定する
            if batch_item.timing is not None:
                source_batches = '        // TODO: ' + summary + '\n'
                source_batches += '        // ' + batch_item.timing.replace('\n', ' ') + '\n'
                source_batches += '        $schedule->command("' + batch_class_name + '")->daily();\n'
                batches.append(source_batches)

        # 「Kernel.php」のソースコードを作成
        # 保存先のフォルダを作成する
        source_file_kernel = open(output_dirs + '/Kernel.php', 'w')

        # 「Kernel.php」のテンプレートソースコードを読み込む
        template_file_kernel = open(self._template_dir + '/Kernel.php', 'r')
        template_source_kernel = template_file_kernel.read()

        # 記述するソースコードを作成する
        join_commands = '\n'.join(commands)
        if join_commands.endswith(","):
            join_commands = join_commands[:-1]
        template_source_kernel = template_source_kernel.replace('__commands__', join_commands)
        template_source_kernel = template_source_kernel.replace('__batches__', '\n'.join(batches))

        # 「Kernel.php」ファイルにソースコードを書き込む
        source_file_kernel.write(template_source_kernel)
        source_file_kernel.close()
