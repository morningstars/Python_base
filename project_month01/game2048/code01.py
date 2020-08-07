"""

    2048游戏规则：
        游戏运行 在4*4方格中随机出现两个随机数
        产生随机数的策略：10%是4  90%是2
        用户移动方格（wsad） 方格内的数字按照规则合并
        如果地图有变化(数字移动/数字合并) 随机产生一个随机数
        游戏结束：数字不能合并也没有空白位置
    架构：
        逻辑处理模块
        界面视图模块
        数据模型模块
        程序入口模块

    步骤：
        1.逻辑处理模块
            创建游戏核心类  GameCoreController
            1.核心代码的参数换成成员变量
            2.生成新数字
                --计算所有空白位置（数字为0）
                --随机选择一个位置
                --根据概率生成随机数存入对应位置

        2.页面视图类模块
            创建游戏核心类
            调用方法生成数字


"""

from game2048.controller import GameCoreController


controller = GameCoreController()
controller.print_map()

print("-----------------")

controller.generate_new_num()
controller.print_map()
