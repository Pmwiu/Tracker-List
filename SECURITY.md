# Security Policy（安全策略）

## 仓库性质

本仓库为**个人使用**的 BitTorrent Tracker 列表镜像与自动维护工具，仅包含：

- 公开 Tracker 地址的**纯文本数据**
- 用于下载、合并、去重、活性测试的 Python 脚本

脚本不收集、不上报任何个人数据，不包含任何可执行的第三方二进制程序。

## 凭证与权限

- 仓库**不包含、不存储**任何密码、令牌（Token）、API Key 等凭证
- 活性测试使用的 `info_hash`、`peer_id` 均在每次运行时**随机生成**，不关联任何真实种子或身份
- 自动维护通过 GitHub Actions 的临时 `GITHUB_TOKEN` 完成，权限最小化为 `contents: write`（仅用于推送更新），不授予 issues、packages、pull-requests 等其他权限

## 供应链与攻击面

- 工作流**仅由定时计划（schedule）和手动触发（workflow_dispatch）运行**，不监听 `pull_request` 事件，因此来自 Fork 的外部 Pull Request **无法触发**本仓库工作流
- 工作流设置了最大运行时长（`timeout-minutes: 15`），防止失控
- 第三方 Actions 固定使用官方主版本标签（`actions/checkout@v4`、`actions/setup-python@v5`）

## 功能收敛

为保持个人使用的纯净性，仓库已/将关闭 Issues、Projects、Wiki、Discussions 等非必要协作功能（仓库设置中操作）。

## 报告安全问题

本仓库为个人项目，**不接受外部贡献**。如确有安全问题需要反馈，请通过 GitHub 个人主页联系仓库所有者。

## 订阅安全建议

推荐订阅经过协议级活性测试的存活列表：

```
https://pmwiu.github.io/Tracker-List/s/alive
```
