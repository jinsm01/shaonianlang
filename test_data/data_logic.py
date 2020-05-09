import yaml


class Yaml_data:
    def __init__(self, yaml_data_path):
        self.data = yaml.safe_load(open(yaml_data_path))

    def case_name(self, name):
        return self.data[name]
