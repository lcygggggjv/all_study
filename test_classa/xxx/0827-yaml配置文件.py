


import yaml  #导入yaml文件
import pprint  #美观打印


def read_yaml(filename,encoding='UTF-8'):
    with open(filename,encoding=encoding) as f:
        content=yaml.safe_load(f)
    return content

pprint.pprint(read_yaml("py.yaml"))


