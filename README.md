<p align="center">
  <img alt="logo" src="https://cdn.jsdelivr.net/gh/midoks/mdserver-web@latest/route/static/logo.png" height="140" />
  <h3 align="center">mdserver-web</h3>
  <p align="center">一款简单Linux面板服务</p>
  <p align="center">强烈推荐系统:debian</p>
</p>

### 简介

简单的Linux面板,感谢BT.CN写出如此好的web管理软件。我一看到，就知道这是我一直想要的页面化管理方式。
复制了后台管理界面，按照自己想要的方式写了一版。


![Debian](https://img.shields.io/badge/LINUX-Debian-blue?style=for-the-badge&logo=Debian)
![Ubuntu](https://img.shields.io/badge/LINUX-Ubuntu-blue?style=for-the-badge&logo=Ubuntu)
![Fedora](https://img.shields.io/badge/LINUX-Fedora-blue?style=for-the-badge&logo=Fedora)
![CentOS](https://img.shields.io/badge/LINUX-CentOS-blue?style=for-the-badge&logo=CentOS)


[![Wiki](https://img.shields.io/badge/MW-Wiki-red?style=for-the-badge&logo=wiki)](https://github.com/midoks/mdserver-web/wiki)
[![](https://data.jsdelivr.com/v1/package/gh/midoks/mdserver-web/badge?style=for-the-badge)](https://www.jsdelivr.com/package/gh/midoks/mdserver-web)

* SSH终端工具
* 面板收藏功能
* 网站子目录绑定
* 网站备份功能
* 插件方式管理

基本上可以使用,后续会继续优化!欢迎提供意见！

- 吹水组 - https://t.me/mdserver_web
- 交流论坛 - https://bbs.midoks.me

```
如果出现问题，最好私给我面板信息。不要让我猜。如果不提供，不要提出问题，自行解决。  — 座右铭
Talk is cheap, show me the code.  -- linus
```

- [兼容性测试报告](/compatibility.md)
- [常用命令说明](/cmd.md)

### 主要插件介绍

* OpenResty - 轻量级，占有内存少，并发能力强。
* PHP[53-82] - PHP是世界上最好的编程语言。
* MySQL - 一种关系数据库管理系统。
* MariaDB - 是MySQL的一个重要分支。
* MySQL[APT/YUM] - 一种关系数据库管理系统。
* MongoDB - 一种非关系NOSQL数据库管理系统。
* phpMyAdmin - 著名Web端MySQL管理工具。
* Memcached - 一个高性能的分布式内存对象缓存系统。
* Redis - 一个高性能的KV数据库。
* PureFtpd - 一款专注于程序健壮和软件安全的免费FTP服务器软件。
* Gogs - 一款极易搭建的自助Git服务。
* Rsyncd - 通用同步服务。


### 插件开发相关

```
插件文档还不完善，如果有不明白的地方提Issue! 我会尽力完善。
如果你自己写了插件，想分享出来，也可以提Issue。
```

- 简单例子 - https://github.com/mw-plugin/simple-plugin 
- 插件地址 - https://github.com/mw-plugin
- 开发文档 - https://github.com/midoks/mdserver-web/wiki/插件开发


# Note

```
phpMyAdmin[4.4.15]支持MySQL[5.5-5.7]
phpMyAdmin[5.2.0]支持MySQL[8.0]

PHP[53-72]支持phpMyAdmin[4.4.15]
PHP[72-82]支持phpMyAdmin[5.2.0]
```

# 特别赞助

- [找资源 - 阿里云盘资源搜索引擎](https://zhaoziyuan.pw/)

# AD - VPS推荐 - 🙏

- [ZZZ评测](https://www.zzzvps.com/)

| 服务商			| 	LOGO   |  推广地址  | 优惠码 |
| ------------- |----------|-----------|-------|
| digitalvirt	|[![digitalvirt](https://digitalvirt.com/templates/BlueWhite/img/logo-dark.svg)](https://digitalvirt.com/aff.php?aff=154) | https://digitalvirt.com/aff.php?aff=154 | mdserver-web |
| mvirtua |[![mvirtua](https://mvirtua.com/upload/logo-black.png)](https://mvirtua.com/aff/FUSKXVDH) | https://mvirtua.com/aff/FUSKXVDH | mdserver-web (全场8折)|

# Docker

- 由[DDSRem](https://github.com/DDSRem)开发维护。
- https://hub.docker.com/r/ddsderek/mw

```
docker run -itd --name mw-server --privileged=true -p 7200:7200 -p 80:80 -p 443:443 -p 888:888 ddsderek/mw-server:latest
```


### 版本更新 0.15.1

* 升级功能优化。
* 域名伪静态保存优化。
* 自动同步gitee。
* nezha保存优化。
* OP防火墙优化(站点配置-状态关闭后,不再防御)-已安装的,需要重载。
* 修复子目录绑定-伪静态问题。
* [插件]docker - 添加IP地址池。
* PHP下载中国优化。
* 监控页面-自定义时间优化。

### JSDelivr安装地址

- 初始安装

```
curl --insecure -fsSL https://cdn.jsdelivr.net/gh/midoks/mdserver-web@latest/scripts/install.sh | bash
```

- 直接更新

```
curl --insecure -fsSL https://cdn.jsdelivr.net/gh/midoks/mdserver-web@latest/scripts/update.sh | bash
```

- 卸载脚本

```
wget --no-check-certificate -O uninstall.sh https://cdn.jsdelivr.net/gh/midoks/mdserver-web@latest/scripts/uninstall.sh && bash uninstall.sh
```

### 备用地址

- 初始安装

```
curl --insecure -fsSL https://raw.githubusercontent.com/midoks/mdserver-web/master/scripts/install.sh | bash
curl --insecure -fsSL https://code.midoks.me/midoks/mdserver-web/raw/branch/master/scripts/install.sh | bash
```

- 直接更新

```
curl --insecure -fsSL https://raw.githubusercontent.com/midoks/mdserver-web/master/scripts/update.sh | bash
```

- 卸载脚本

```
wget --no-check-certificate -O uninstall.sh https://raw.githubusercontent.com/midoks/mdserver-web/master/scripts/uninstall.sh && bash uninstall.sh
```


### 通用软件安装[命令行安装]

- 需已经安装mdserver-web

```
curl --insecure -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/quick/app.sh | bash
```


### DEV使用

```
curl --insecure -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/install_dev.sh | bash
curl --insecure -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/update_dev.sh | bash

wget --no-check-certificate -O uninstall.sh https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/uninstall.sh && bash uninstall.sh

curl --insecure -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/quick/debug.sh | bash

curl --insecure -fsSL https://code.midoks.me/midoks/mdserver-web/raw/branch/dev/scripts/install_dev.sh | bash
curl --insecure -fsSL https://code.midoks.me/midoks/mdserver-web/raw/branch/dev/scripts/update_dev.sh | bash
```

### 捐赠地址 USDT（TRC20）

TVbNgrpeGBGZVm5gTLa21ADP7RpnPFhjya

日行一善，以后必定大富大贵


### 微信赞助

[![截图](https://cdn.jsdelivr.net/gh/midoks/mdserver-web@latest/route/static/img/weixin_zz.jpg)](https://cdn.jsdelivr.net/gh/midoks/mdserver-web@latest/route/static/img/weixin_zz.jpg)


### 无图不真相

[![截图](https://cdn.jsdelivr.net/gh/midoks/mdserver-web@latest/route/static/mdw.jpg)](https://cdn.jsdelivr.net/gh/midoks/mdserver-web@latest/route/static/mdw.jpg)


### Stargazers over time

[![Stargazers over time](https://starchart.cc/midoks/mdserver-web.svg)](https://starchart.cc/midoks/mdserver-web)


### 感谢开发赞助

[![digitalvirt](https://digitalvirt.com/templates/BlueWhite/img/logo-dark.svg)](https://digitalvirt.com/aff.php?aff=154)

### 授权许可

本项目采用 Apache 开源授权许可证，完整的授权说明已放置在 [LICENSE](https://github.com/midoks/mdserver-web/blob/master/LICENSE) 文件中。

