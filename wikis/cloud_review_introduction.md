# 云审查工具简介

## 这是什么？

这是一个以`Tieba-Manager`为基础，二次开发的自动扫描并处理首页违规信息的管理工具

**它可以极大节约吧务人工巡逻的时间成本**

## 扫描范围
在我给出的范例[`cloud_review_hanime.py`](https://github.com/Starry-OvO/Tieba-Manager/blob/master/cloud_review_hanime.py)中，每一轮扫描都会覆盖宫漫吧首页**按回复时间顺序**的前**30个**`主题帖`；以及这些`主题帖`中最新的**30条**`回复`；如果帖子被定义为`热门帖`，云审查还会检查`主题帖`的前**30条**`热门回复`；以及上述所有`回复`中点赞数最高的前**10条**`楼中楼`内容

云审查工具会检查以上内容中是否存在黑名单用户、违规图片、符合正则表达式规则的违规文字或小尾巴、违规链接

## 使用方法

参照我给出的例子自己编程修改[`cloud_review_hanime.py`](https://github.com/Starry-OvO/Tieba-Manager/blob/master/cloud_review_hanime.py)，这是被实际应用于[宫漫吧](https://tieba.baidu.com/f?ie=utf-8&kw=%E5%AE%AB%E6%BC%AB)的云审查工具。注释比较规范全面，请自行理解各api的功能

## 实战效果

以下是应用于[`孙笑川吧`](https://tieba.baidu.com/f?ie=utf-8&kw=%E5%AD%99%E7%AC%91%E5%B7%9D)的云审查工具的实战效果。

<img width="720" alt="test_1" src="https://user-images.githubusercontent.com/48282276/165777398-47e00f26-a46f-4b7c-a03e-03092e5d31ba.png">

<img width="720" alt="test_2" src="https://user-images.githubusercontent.com/48282276/165776593-ab5feec4-6529-4702-82e5-1904e9e8630f.png">

## 性能测试
**测试时间**: 2022.03.30<br>
**硬件条件**: **CPU** Intel Xeon Platinum 8163 2.50GHz / **带宽** 1Mbps<br>
**扫描间隔**: 10秒<br>
**吧活跃度**: 近29天日均新增回复15977条<br>
10次扫描平均耗时 **1.252秒**

<img width="483" alt="benchmark" src="https://user-images.githubusercontent.com/48282276/160804519-f71a1e8d-5d9a-49a1-aac8-7119b1af5105.png">