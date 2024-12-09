import yaml
from pathlib import Path

class ReaderConfig:
    def __init__(self, init_d):
        self.__dict__.update(init_d)
        for k, v in init_d.items():
            if isinstance(v, dict):
                self.__dict__[k] = ReaderConfig(v)

def load_config(Obj):
    path = Path(Path.cwd(), 'config', 'config.yaml')
    with open(path, 'r') as file:
        return Obj(yaml.safe_load(file))


config = load_config(ReaderConfig)