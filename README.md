<p align="center">

<img src="https://raw.githubusercontent.com/Starry-OvO/aiotieba/master/docs/img/aiotieba.svg">

</p>

<div align="center">
<p>
<a href="https://github.com/Starry-OvO/aiotieba/actions">
    <img src="https://img.shields.io/github/workflow/status/Starry-OvO/aiotieba/CI?label=CI&logo=github" alt="GitHub Workflow Status">
</a>
<a href="https://pypi.org/project/aiotieba">
    <img src="https://badge.fury.io/py/aiotieba.svg" alt="PyPI version">
</a>
<a href="https://pypi.org/project/aiotieba">
    <img src="https://img.shields.io/pypi/pyversions/aiotieba" alt="PyPI - Python Version">
</a>
</p>
</div>

---

## 简介

**aiotieba**使用[**asyncio**](https://tutorial.python.org/zh-cn/3/library/asyncio.html)和[**aiohttp**](https://github.com/aio-libs/aiohttp)封装了大量操作[百度贴吧核心API](https://github.com/Starry-OvO/aiotieba/blob/master/aiotieba/client.py)的简便方法，并为吧务管理设计了一套[内容审查脚手架](https://github.com/Starry-OvO/aiotieba/blob/master/aiotieba/reviewer.py)

本框架以提高二次开发速度为首要设计目标。规范且符合直觉的命名规律、全覆盖的类型注解和文档注释让你体验飞一般的开发体验

<details>

<summary>贴吧接口列表</summary>

+ 按回复时间/发布时间/热门序获取贴吧主题帖/精华帖列表。支持获取带转发/投票/转发嵌套投票/各种卡片的主题帖信息
+ 获取带图片链接/小尾巴内容/点赞情况/用户信息（[用户名](https://starry-ovo.github.io/aiotieba/tutorial/quickstart#user_name)/[portrait](https://starry-ovo.github.io/aiotieba/tutorial/quickstart#portrait)/[user_id](https://starry-ovo.github.io/aiotieba/tutorial/quickstart#user_id)/等级/性别/是否锁回复）/每条回复的前排楼中楼（支持按或不按点赞数排序）的楼层列表
+ 获取带所有前述用户信息的楼中楼列表
+ 根据[用户名](https://starry-ovo.github.io/aiotieba/tutorial/quickstart#user_name)/[portrait](https://starry-ovo.github.io/aiotieba/tutorial/quickstart#portrait)/[user_id](https://starry-ovo.github.io/aiotieba/tutorial/quickstart#user_id)中的任一项反查其他用户信息，或通过用户主页的[tieba_uid](https://starry-ovo.github.io/aiotieba/tutorial/quickstart#tieba_uid)反查其他用户信息
+ 使用小吧主、语音小编的账号删帖/屏蔽/封禁。支持删除视频帖/批量删帖/多于1天的封禁
+ 使用已被大吧主分配解封/恢复/处理申诉权限的吧务账号解封/恢复/处理申诉
+ 使用大吧主账号推荐帖子到首页/移动帖子到指定分区/加精/撤精/置顶/撤置顶/添加黑名单/查看黑名单/取消黑名单
+ 获取其他用户的主页信息/关注贴吧列表/关注用户列表/粉丝列表/发布的主题帖列表
+ 使用当前账号关注贴吧/取关贴吧/关注用户/取关用户/移除粉丝/获取屏蔽贴吧列表/屏蔽贴吧/取消屏蔽贴吧/点赞点踩/取消点赞点踩/签到/水帖/发送私信/获取回复历史
+ 获取一个贴吧的最新关注用户列表/等级排行榜/吧务列表/吧详情

</details>

<details>

<summary>额外的审查功能列表</summary>

+ 数据库功能：缓存贴吧常量（如贴吧名到fid的映射关系、用户基本信息等）/为用户添加标记/为帖子或回复添加标记/为图像hash添加标记
+ 图像处理功能：图像解码/二维码解析/图像hash计算

</details>

## 安装并使用

+ 检查Python版本 (**>=3.9**)

+ 安装

```shell
pip install aiotieba[img]
```

+ 体验一下

```python
import asyncio

import aiotieba


async def main():
    async with aiotieba.Client() as client:
        print(await client.get_threads("天堂鸡汤"))


asyncio.run(main())
```

+ 继续阅读[**入门教程**](https://starry-ovo.github.io/aiotieba/tutorial/quickstart)

## 友情链接

+ [另一个仍在活跃更新的贴吧管理器（有用户界面）](https://github.com/dog194/TiebaManager)
+ [用户反馈（我的个人吧）](https://tieba.baidu.com/starry)

## 客户名单

<details><summary>2022.09.24更新</summary>

|      吧名      | 关注用户数 | 最近29天日均访问量 | 日均主题帖数 | 日均回复数 |
| :------------: | :--------: | :----------------: | :----------: | :--------: |
|    抗压背锅    | 4,089,017  |      748,250       |    3,388     |   99,433   |
|     孙笑川     | 2,535,489  |      581,786       |    7,732     |  223,174   |
|    lol半价     | 1,961,420  |      103,427       |     405      |   5,606    |
|      宫漫      | 1,336,129  |       47,481       |     224      |   3,284    |
|    逆水寒ol    |  714,852   |       36,864       |     111      |   2,568    |
|    新孙笑川    |  355,569   |       59,189       |     463      |   20,332   |
|     vtuber     |  214,423   |       11,816       |      72      |    898     |
|     asoul      |  157,639   |       13,373       |      97      |    581     |
|      嘉然      |   57,072   |       12,429       |     105      |   1,461    |
|      向晚      |   29,964   |       13,004       |     103      |   1,399    |
|      贝拉      |   21,641   |       8,849        |      44      |    768     |
|      乃琳      |   17,117   |       3,853        |      22      |    278     |
| vtuber自由讨论 |   16,803   |       4,257        |      3       |     68     |
| asoul一个魂儿  |   14,538   |        996         |      6       |     43     |
|     贝贝珈     |   1,617    |        691         |      2       |     17     |

</details>
