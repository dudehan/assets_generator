#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自动生成 flutter 项目assets资源配置
"""

import os
import re
import sys
from functools import reduce


FIRST_NODE = ''
LAST_NODE = ''
#PATH ： 图片路径，例如：assets/images
PATH = sys.argv[1]
#R_PATH : 文件路径，例如：lib/image_r.dart
R_PATH = sys.argv[2]
#R_CLASS_NAME : 类的名称，例如：ImageR
R_CLASS_NAME = sys.argv[3]

if PATH == 'assets/images':
    FIRST_NODE = 'assets-images-generator-begin'
    LAST_NODE = 'assets-images-generator-end'
elif PATH == 'assets/files':
    FIRST_NODE = 'assets-files-generator-begin'
    LAST_NODE = 'assets-files-generator-end'
elif PATH == 'assets/local':
    FIRST_NODE = 'assets-local-generator-begin'
    LAST_NODE = 'assets-local-generator-end'

RE_ASSETS = re.compile(
    r'# {0}[\s\S]+# {1}'.format(FIRST_NODE, LAST_NODE))
RE_2_3X = re.compile(r'(2.x/)|(3.x/)')


# PATH = 'assets'

def replace_content(content):
    with open('pubspec.yaml', 'r') as fr:
        result = re.sub(RE_ASSETS, content, fr.read())
        with open('pubspec.yaml', 'w') as fw:
            fw.write(result)


def find_assets(path, list):
    if os.path.isfile(path):
        return path
    assets = os.listdir(path)
    for f in assets:
        value = find_assets('%s/%s' % (path, f), list)
        if value:
            list.append(value)
    return None


def formatter(origin):
    src = origin.replace('2.x/', '').replace('3.x/', '')

    arr = re.split(r'[/_.]', src[:src.rindex('.')])
    print(arr)
    res = ''
    for i in arr:
        if i is None or i == '' or i == 'assets':
            continue
        # res = res + '_' + i[0:]
        res = res + i[0].upper() + i[1:]
        print(res)
    res = res[0].lower() + res[1:]
    return [src, res, origin]


def get_non_repeat_list(data):
    return list(set(data))


if __name__ == '__main__':
    find_list = []
    find_assets(PATH, find_list)
    no2x3x_list = []
    for l in list(find_list):
        if l.find('.DS_Store') > -1:
            find_list.remove(l)
            continue
        nox = l
        if l.find('2.x/') > -1 or l.find('3.x/') > -1:
            nox = re.sub(RE_2_3X, '', l)
            if nox in find_list:
                find_list.remove(nox)
        no2x3x_list.append(nox)
    no2x3x_list = get_non_repeat_list(no2x3x_list)
    yaml_content = '# {0}\n    - %s\n  # {1}'.format(FIRST_NODE, LAST_NODE) % reduce(
        lambda x, y: x + '\n    - ' + y, sorted(no2x3x_list, key=str.lower))
    replace_content(yaml_content)

    class_list = map(formatter, sorted(
        no2x3x_list, key=lambda s: re.sub(RE_2_3X, '', s.lower())))
    print(class_list.__str__())
    class_r = 'class ' + R_CLASS_NAME + ' {\n%s}' % reduce(lambda x, y: x + y, map(
        lambda x: "  /// %s\n  static final String %s = '%s';\n" % (
            x[2], x[1], x[0]), class_list))

    # r = 'lib/r.dart'
    if os.path.exists(R_PATH):
        os.remove(R_PATH)
    with open(R_PATH, 'w') as fw:
        fw.write(class_r)
    # start_server()
