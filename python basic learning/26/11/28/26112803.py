"""

# 学习日志 · Learning Journal（补充篇）

**日期 / Date:** 2026-11-28
**主题 / Theme:** 用 Python 代码调用模型——本地与云端
**Theme:** Calling Models from Python — Local and Cloud

---

## 一、本次目标 / The Goal

前面一直是用现成工具去用模型，今天想更进一层：**不点鼠标，用代码去调它**。而且不只调本地的，云端的一起调通。

So far I had been using the model through an existing tool. Today I wanted one level deeper: **call it from code instead of clicking buttons** — and not only the local model, but a cloud model as well.

---

## 二、过程记录 / What Actually Happened

**中文**

1. **动手写代码，准备调用本地模型。**
   想法很直接：既然是本地服务，写段 Python 发个请求应该就行。

2. **卡住了：代码里要 `import openai`。**
   编辑器里一写这个引用就报错——这个库本机根本没有，也不是 Python 自带的。

3. **查明白了：要从 PyPI 下载，用 pip 安装。**
   原来 Python 只自带标准库，第三方库都得自己去"应用商店"取。商店叫 **PyPI**，取货的工具叫 **pip**。

4. **装完之后，本地模型跑通了。**
   用 Python 代码配合自己的 API，成功调起了本地 DeepSeek，拿到了返回结果。

5. **接着又调通了云端大模型。**
   同样是 Python 代码加自己的 API，这次请求发到云端，也成功拿到了结果。

**English**

1. **Started writing code to call the local model.**
   The plan seemed obvious: it's a local service, so a short Python script sending a request should do it.

2. **Got stuck: the code needed `import openai`.**
   The editor errored on that import — the library simply wasn't on this machine, and it isn't part of Python itself.

3. **Worked out why: it has to come from PyPI, installed with pip.**
   Python ships only its standard library; any third-party package must be fetched from a repository. That repository is **PyPI**, and the tool that fetches from it is **pip**.

4. **Once installed, the local model worked.**
   Python code plus my own API successfully called the local DeepSeek and returned a result.

5. **Then the cloud model worked too.**
   Again Python code plus my own API — this time the request went out to a cloud model, and it returned a result as well.

---

## 三、这次真正学到的 / What I Actually Learned

**中文**

**① "调用模型"不只有一种姿势。**
之前以为只能靠工具界面，或者手写 HTTP 请求。这次发现还有第三条路：用别人封装好的**客户端库**，几行代码搞定，协议细节被库包掉了。

**② 库不是凭空存在的，得自己装。**
`import` 只是"声明我要用"，不代表"它已经在这"。今天最实在的一课——报错不是因为代码写错，而是**依赖没装**。以后看到"模块找不到"这类错误，第一反应应该是"缺依赖"，而不是"我写错了"。

**③ PyPI 和 pip 是两个东西。**
一个是**仓库**（存放包的地方），一个是**工具**（把包拿下来装好）。类比：PyPI 是应用商店，pip 是安装器。

**④ 本地和云端，居然用的是同一套代码。**
这是今天最有意思的发现。换的只是两样东西：**API 地址**（请求发给谁）和 **API 密钥**（凭谁的身份）。其余代码几乎不用动。也就是说，只要接口"长得一样"，本地和云端在代码眼里没有区别。

**⑤ 但两者的代价完全不同。**
云端模型**不需要本地显卡**，算力在别人机器上，按用量付费；本地模型**不花钱**，但受自己的显存限制。同一行代码，背后是两种完全不同的成本结构。

**English**

**① There is more than one way to call a model.**
I had assumed it was either a GUI tool or hand-written HTTP. Today I found a third route: a **client library** — a few lines of code, with the protocol details hidden inside it.

**② Libraries don't appear by themselves.**
`import` only declares "I want to use this"; it does not mean "it is already here". The most concrete lesson of the day: the error was not bad code, it was a **missing dependency**. From now on, a "module not found" error should say "dependency missing" before it says "I typed something wrong".

**③ PyPI and pip are two different things.**
One is a **repository** (where packages live), the other a **tool** (which fetches and installs them). Analogy: PyPI is the app store, pip is the installer.

**④ Local and cloud turned out to use the same code.**
The most interesting discovery of the day. Only two things change: the **API endpoint** (who receives the request) and the **API key** (whose identity it carries). Almost nothing else moves. As long as the interface "looks the same", the code cannot tell local from cloud.

**⑤ But the two cost very different things.**
A cloud model needs **no local GPU** — the compute happens on someone else's machine and is paid for by usage. A local model **costs nothing to run** but is limited by my own VRAM. The same line of code sits on top of two completely different cost structures.

---

## 四、本地 vs 云端 / Local vs Cloud

| 维度 / Aspect | 本地模型 / Local | 云端模型 / Cloud |
|---|---|---|
| 代码写法 / How you call it | 用库，几乎一样 / a library, nearly identical | 用库，几乎一样 / a library, nearly identical |
| 要改什么 / What you change | API 地址指向本地 / point the endpoint at localhost | API 地址指向云端 / point the endpoint at the cloud |
| 算力在哪 / Where compute runs | 自己的显卡 / my own GPU | 服务商的机器 / the provider's machines |
| 显存要求 / VRAM needed | 有，且是硬约束 / yes, a hard limit | 没有 / none |
| 费用 / Cost | 电费，几乎为零 / electricity, near zero | 按用量计费 / billed by usage |
| 速度 / Speed | 受硬件影响 / limited by my hardware | 受网络和配额影响 / limited by network and quota |
| 隐私 / Privacy | 数据不出本机 / data never leaves the machine | 数据要发出去 / data leaves the machine |
| 能力上限 / Capability ceiling | 受显存限制 / capped by VRAM | 可以用很大的模型 / can use much larger models |

---

## 五、卡点与解法 / Blocks and Fixes

| 卡点 / Block | 原因 / Cause | 解法 / Fix |
|---|---|---|
| 代码里 `import openai` 报错 | 第三方库没安装 / package not installed | 用 pip 从 PyPI 安装 / install with pip from PyPI |
| 不清楚库从哪来 | Python 只带标准库 / Python ships only stdlib | 认准 PyPI + pip 这套机制 / use the PyPI + pip mechanism |
| 不知道调用要填什么 | 习惯了自己写 HTTP / used to raw HTTP | 库已封装，只需地址、密钥、模型名 / supply endpoint, key, model name |
| 本地能调，云端怎么调 | 以为两套完全不同的东西 / assumed two separate things | 换掉地址和密钥即可 / swap endpoint and key |

---

## 六、术语对照 / Glossary

| 中文 | English | 一句话解释 / One-liner |
|---|---|---|
| 第三方库 | Third-party library | 不是 Python 自带的包 / a package not bundled with Python |
| 依赖 | Dependency | 代码运行前必须先装好的东西 / must be installed before the code runs |
| 包管理 | Package management | 安装、升级、卸载库的机制 / installing, upgrading, removing libraries |
| 仓库 | Repository / Package index | 存放包的地方，PyPI 就是 / where packages live; PyPI is one |
| 引入 / 导入 | Import | 在代码里声明要用某个库 / declare a library is to be used |
| API 地址 | API endpoint / base URL | 请求发往的地址 / where requests are sent |
| API 密钥 | API key | 调用方的身份凭证 / the caller's credential |
| 本地模型 | Local model | 跑在自己机器上的模型 / a model running on your own machine |
| 云端模型 | Cloud model | 通过接口调用、跑在服务商机器上的模型 / a model reached over the network |
| 推理 | Inference | 模型生成回答的过程 / the process of generating a response |
| 按用量计费 | Usage-based billing | 用多少付多少 / pay for what you use |
| 编辑器 / IDE | Editor / IDE | 写代码的软件，如 VS Code、PyCharm / software for writing code |

> 小订正 / Small correction：写代码的软件叫**编辑器**或 **IDE**，不叫"编译器"。编译器负责把代码翻译成机器指令，是另一回事。
>
> The software you write code in is an **editor / IDE**, not a "compiler". A compiler translates code into machine instructions — a different thing entirely.

---

## 七、还没弄清、想验证的问题 / Open Questions

**中文**

1. **pip 把包装到哪儿了？** 全局 Python，还是项目自己的虚拟环境？装到全局，不同项目之间会不会互相干扰？
2. **API 地址为什么能指向本地？** 那个字段到底填的是什么，为什么本地服务也能像远程服务一样被调用？
3. **本地为什么也非填 API 密钥不可？** 是真在校验，还是纯粹为了让库不报错？云端那把密钥显然不是摆设。
4. **库到底帮我做了什么？** 手写 HTTP 请求能不能达到同样效果？差别在哪？
5. **云端那把密钥怎么保管？** 直接写在代码里显然不行——应该怎么放？
6. **两边的模型名能混用吗？** 本地叫这个名字，云端也叫这个名字，会不会串？

**English**

1. **Where did pip install it?** Global Python, or a project-specific virtual environment? If global, do different projects interfere?
2. **Why can the API endpoint point at localhost?** What exactly goes in that field, and why can a local service be called like a remote one?
3. **Why is an API key required locally too?** Is it validated, or just there to stop the library complaining? The cloud key is obviously not decorative.
4. **What is the library doing for me?** Would a hand-written HTTP request give the same result? Where's the difference?
5. **How should the cloud key be stored?** Clearly not hard-coded in the script — so where?
6. **Can model names be mixed up?** The same name exists locally and in the cloud — can I accidentally hit the wrong one?

---

## 八、下一步 / Next Steps

- [ ] 搞清楚 pip 的安装位置，学会用虚拟环境隔离项目依赖
- [ ] 对比"用库调用"和"手写 HTTP 调用"，看清库到底封装了什么
- [ ] 把本地和云端的调用整理成同一份可复用脚本，只靠切换配置来换目标
- [ ] 学会不把密钥写进代码（改用环境变量或配置文件）
- [ ] 对比同一个问题在本地和云端的回答质量差异

- [ ] Find out where pip installs, and learn to isolate project dependencies with virtual environments
- [ ] Compare "library call" against "hand-written HTTP call" to see what the library wraps
- [ ] Turn local and cloud calls into one reusable script that switches target by config alone
- [ ] Stop hard-coding keys — move them into environment variables or a config file
- [ ] Compare answer quality for the same question, local versus cloud

---

## 九、一句话总结 / One-Sentence Summary

**中文**：以为要写的是一段"调用模型的代码"，结果先学了一堂"Python 依赖管理课"；而更有意思的是，本地和云端在代码里几乎一模一样——换掉的只是地址和钥匙。

**English**: I thought I was about to write "code that calls a model"; what I actually got was a lesson in **Python dependency management**. And more interesting still: local and cloud are nearly identical in code — only the address and the key change.
"""