<!-- markdownlint-disable-next-line MD041 -->
<p align="center">
  <a href="https://nonebot.dev/"><img src="https://raw.githubusercontent.com/nonebot/adapter-github/master/assets/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# NoneBot-Adapter-GitHub

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD036 -->

_✨ GitHub 协议适配 ✨_

<!-- markdownlint-restore -->

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/nonebot/adapter-github/master/LICENSE">
    <img src="https://img.shields.io/github/license/nonebot/adapter-github" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-adapter-github">
    <img src="https://img.shields.io/pypi/v/nonebot-adapter-github" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue" alt="python">
  <a href="https://results.pre-commit.ci/latest/github/nonebot/adapter-github/master">
    <img src="https://results.pre-commit.ci/badge/github/nonebot/adapter-github/master.svg" />
  </a>
  <br />
  <a href="https://jq.qq.com/?_wv=1027&k=5OFifDh">
    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-768887710-orange?style=flat-square" alt="QQ Chat Group">
  </a>
  <a href="https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&appChannel=share&inviteCode=7b4a3&appChannel=share&businessType=9&from=246610&biz=ka">
    <img src="https://img.shields.io/badge/QQ%E9%A2%91%E9%81%93-NoneBot-5492ff?style=flat-square" alt="QQ Channel">
  </a>
  <a href="https://t.me/botuniverse">
    <img src="https://img.shields.io/badge/telegram-botuniverse-blue?style=flat-square" alt="Telegram Channel">
  </a>
  <a href="https://discord.gg/VKtE6Gdc4h">
    <img src="https://discordapp.com/api/guilds/847819937858584596/widget.png?style=shield" alt="Discord Server">
  </a>
</p>

## 安装

```bash
poetry add nonebot-adapter-github
# 或者
pip install nonebot-adapter-github
```

## 加载适配器

```python
import nonebot
from nonebot.adapters.github import Adapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(Adapter)
```

## 配置

### 配置 APP

```dotenv
GITHUB_APPS='
[
  {
    "app_id": "123456",  # GitHub App ID 必填
    "private_key": [
      "-----BEGIN RSA PRIVATE KEY-----",
      "...",  # 将私钥按行输入
      "...",
      "...",
      "-----END RSA PRIVATE KEY-----"
    ],  # GitHub App 私钥必填
    "client_id": "123456",  # OAuth App Client ID 必填，GitHub App 可选
    "client_secret": "xxxxxx",  # OAuth App Client Secret 必填，GitHub App 可选
    "webhook_secret": "xxxxxx"  # 可选
  }
]'
```

### 其他配置

```dotenv
GITHUB_BASE_URL=https://api.github.com
GITHUB_ACCEPT_FORMAT=full+json
GITHUB_PREVIEWS=["starfox"]
```

## 使用

### WebHook

URL: `/github/webhooks/<app_id>` (GitHub APP) / `/github/webhooks/<client_id>` (OAuth APP)

事件格式:

```python
class Event(BaseModel):
    id: str  # 事件 ID
    name: str  # 事件名称
    payload: Dict[str, Any]  # 事件内容

    to_me: bool = False  # 是否 @ 了机器人或机器人昵称
```

具体事件类型及内容请参考 [GitHub Developer](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads)

### 调用 API

可以直接通过 bot 调用 API，但是请注意 **只能使用异步接口，参数必须是 keyword args**。具体使用方法参考 [githubkit](https://github.com/yanyongyu/githubkit)。

```python
async with bot.as_installation(installation_id=1):
    resp = await bot.rest.issues.async_get(owner="owner", repo="repo", issue_number=1)
    issue = resp.parsed_data

    resp = await bot.async_graphql(query=query)

    async for issue in bot.github.paginate(bot.rest.issues.async_list_for_repo, owner="owner", repo="repo"):
        print(issue)
```

也可以直接使用 `githubkit`，但是将绕过 NoneBot 的 `call api hook`。

```python
github = bot.github
```

## 开发

生成事件列表：

```bash
python -m codegen && ruff check --fix -e . && isort . && black .
```
