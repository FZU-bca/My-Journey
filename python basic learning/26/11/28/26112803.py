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

**⑤ 
"""