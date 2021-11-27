"""
__author__ = 'hogwarts_xixi'
"""
# pip install pyyaml
import yaml


def test_yaml():
    # f = open("./datas/data.yml")
    # result = yaml.safe_load(f)
    # print(result)
    # f.close()
    with open("./datas/data.yml") as f:
        result = yaml.safe_load(f)

    print(result.get("add_normal"))


def test_save():
    a = [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]]
    with open("a.yml", mode="w") as f:
        yaml.safe_dump(a, f)
