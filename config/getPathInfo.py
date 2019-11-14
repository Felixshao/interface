import os


def get_path():
    """
    :return:path;项目的绝对路径
    """
    path = os.path.split(os.path.realpath(__file__))[0]
    project_path = os.path.abspath(os.path.dirname(path) + os.path.sep + '.')

    return project_path


if __name__ == '__main__':
    print(get_path())