# 起名不应该以test开头
import configparser

# 第一步生成相应的ConfigParser的实例
cfg = configparser.ConfigParser()

# 生成实例后需要输入相应的配置文件
cfg.read("text_cfg.cfg", encoding="utf-8")

sp_name = cfg.get("SmallPlane", "name")
print(sp_name)

sp_width = cfg.getint("SmallPlane", "width")
print(sp_width)