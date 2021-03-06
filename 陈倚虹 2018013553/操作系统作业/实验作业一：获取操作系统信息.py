# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    Author: YH.Chen
    Purpose: Use platform to get the information of OperaSystem.
    Created: 24/6/2020
"""

import platform


def get_platform():
    # 获取操作系统的名称及版本号
    return platform.platform()


def get_version():
    # 获取操作系统版本号
    return platform.version()


def get_architecture():
    # 获取操作系统的位数
    return platform.architecture()


def get_machine():
    # 计算机类型
    return platform.machine()


def get_node():
    # 计算机的网络名称'''
    return platform.node()


def get_processor():
    # 计算机处理器信息
    return platform.processor()


def get_system():
    # 获取操作系统类型
    return platform.system()


def get_info():
    # 汇总信息
    return platform.uname()


def show_os_all_info():
    # 打印操作系统的全部信息
    print('获取操作系统名称及版本号：[{}]'.format(get_platform()))
    print('获取操作系统版本号：[{}]'.format(get_version()))
    print('获取操作系统的位数：[{}]'.format(get_architecture()))
    print('计算机类型：[{}]'.format(get_machine()))
    print('计算机的网络名称：[{}]'.format(get_node()))
    print('计算机处理器信息：[{}]'.format(get_processor()))
    print('获取操作系统类型：[{}]'.format(get_system()))
    print('汇总信息：[{}]'.format(get_info()))


def test():
    print("操作系统信息：")
    show_os_all_info()


def main():
    test()
    print('-' * 20 + ' 打印完毕 ' + '-' * 20)


if __name__ == '__main__':
    main()
