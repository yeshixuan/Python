# pygame
#文件起名不应该以test开头
# 飞机大战
-

# v1
- 主要作为技术验证
- 画出一个舞台，包括背景，包括一个小飞机

# v2
- 小蜜蜂会动，从上往下慢慢地飞
- 能控制小蜜蜂左右移动
- 入场算法
   - y轴要求是负数，这样会形成慢慢入场的效果，y = 0 - 蜜蜂的高度
   - x轴要求是由一定的富裕，即要求密封等移动五品不能贴边来，比如富裕50
        基本上x轴的值应该是50起，最右边的计算方式应该是world的宽度减去蜜蜂的宽度减去富裕值50
- 移动速度问题
    - 包含x、y值
    - 绝大多数值考虑y值
    - 但是蜜蜂和英雄是特例
    - 蜜蜂从上往下走时也会左右移动
    - 英雄的移动是由上下左右键盘控制
    - 速度应该是一个tuple=（x,y）
- 方向问题
    - 具体移动方向有x,y控制
    - 值只能是-1,0,1三个就好
    - 应该是一个tuple
    - 例如(-1,0)表示水平向左移动
    - （0,1）表明向下垂直移动
    
# v3
- 重构代码，使用opp方法
   - 世界的构成
        - 小飞机
        - 大飞机
        - 小蜜蜂
        - 子弹
        - 英雄机
        - 天空
   - 配置文件
        - 可以通过一次性配置来让程序正确运行
        - 降低了代码软件工程方面的成本
        - python的配置文件包：configparser
            - 以前就叫ConfigParser
            - 配置文件一般以cfg或者ini结尾，window用cfg，linux用ini
            - 语法：
                - 中括号：表示的是section
                - 每个ssection下是键值对
                - 键值对等号或者冒号连接
            - get(section_name,key_name),返回相应的值
            - getint（section_name,key_name),返回相应的整数值
            
- 在ooop的基础上创建小飞机，蜜蜂，相对简单很多
- 程序可以正常产生飞行物，包括英雄机，子弹，云层
# v4 - 实现碰撞检测
- 碰撞检测算法是游戏通用算法，必须掌握
- 一旦判断发生碰撞
    - 生命值会发生改变
    - 生命状态发生改变
        - LIFT_STATUS_LIVE
        - LIFT_STATUS_DEAD:已经发生碰撞，播放死亡动画
        - LIFT_STATUS_REMOVABLE:可以移除
    - 如果生命状态DEAD，则播放死亡动画
    
- 在处理小飞机的时候：
    - 初始化的时候吧五张图片全部初始化完毕，放入list中
    - 考虑到资源消耗，图片保存成类变量（所谓静态变量）
    - 正常播放的是第一张图片，一旦中弹，则连续播放其余四张图片

- 游戏状态
    - READY:游戏没有开始，显示一张准备图片
    - RUNNING：正常游戏运行
    - DONE：gameover，显示借宿图片，注意游戏停止循环运行
    
- 游戏分数：
    - 一个变量，每次碰撞后检测对方身份，如果是子弹撞击对方，则直接根据敌人类型更改分数
    - 把分数提示显示在屏幕上