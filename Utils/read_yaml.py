import os

import yaml

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ReadFileData:

    @staticmethod
    def load_data(file_path):
        try:
            data_file_path = os.path.join(root_path, "ApiData", file_path)
            with open(data_file_path, encoding='utf-8') as f:
                data_content = yaml.safe_load(f)
        except Exception as ex:
            print(ex)
        else:
            return data_content


read_data = ReadFileData()
