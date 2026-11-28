"""# 学习日志 · Learning Journal

**日期 / Date:** 2026-11-28
**主题 / Theme:** 从 HTTP 到本地大模型——一条完整的本地 AI 应用链路
**Theme:** From HTTP to a Local LLM — Building an End-to-End Local AI Stack

---

## 一、今日主题 / Today's Topics

| # | 中文 | English |
|---|---|---|
| 1 | HTTP 协议基础 | The HTTP Protocol |
| 2 | Apifox 接口接入测试 | API Integration Testing with Apifox |
| 3 | 上下文会话记忆方案 | Context & Conversation Memory |
| 4 | 本地部署 DeepSeek | Running DeepSeek Locally |

**今天最大的收获 / Biggest takeaway**

这四件事不是四个孤立的知识点，而是同一个系统的四层。把它们串起来看，每一层都能解释下一层为什么长那样。

These four topics are not four isolated subjects — they are four layers of one system. Viewed together, each layer explains why the layer above it looks the way it does.

```
┌─ 业务层 / Application   会话记忆方案   Who remembers the previous turn
├─ 调试层 / Debugging     Apifox 接入测试 Is the request and response correct
├─ 协议层 / Protocol      HTTP           Verbs, JSON, status codes, streaming
└─ 推理层 / Inference     本地 DeepSeek   Ollama on 127.0.0.1:11434
```

---

## 二、逐项笔记 / Notes by Topic

### 1. HTTP 协议 / The HTTP Protocol

**中文**

HTTP 是"请求—响应"模型：客户端发一个请求，服务端回一个响应，然后连接结束。它本身**不保存任何状态**——这是理解后面"会话记忆"的关键前提。

四个要素要分清：

- **方法（Method）**：`GET` 取数据，`POST` 提交数据。调大模型接口基本都用 `POST`，因为要传 JSON body。
- **状态码（Status Code）**：`200` 成功、`400` 请求有问题、`401` 没鉴权、`404` 路径不对、`500` 服务端挂了。但要注意——**状态码 200 不代表业务成功**，有些 API 会把错误塞在 body 里。
- **头部（Headers）**：`Content-Type: application/json` 告诉服务端 body 是什么格式。
- **正文（Body）**：JSON 是最常见的格式。

还有一个容易忽略的点：**分块传输（chunked transfer）**。普通响应是"攒齐了再一次性发回"，而流式响应是"边算边发"，这就是大模型能一个字一个字往外蹦的原因。

**English**

HTTP is a request–response model: the client sends a request, the server sends back a response, and the connection is done. HTTP itself **stores no state** — which is the key premise for understanding conversation memory later.

Four things to keep straight:

- **Method**: `GET` to read, `POST` to submit. LLM APIs almost always use `POST` because they carry a JSON body.
- **Status code**: `200` OK, `400` bad request, `401` unauthenticated, `404` wrong path, `500` server error. But note — **a 200 does not mean business success**; some APIs put the error inside the body.
- **Headers**: `Content-Type: application/json` tells the server what the body is.
- **Body**: JSON is the common format.

One easily overlooked detail: **chunked transfer encoding**. A normal response is buffered and sent all at once; a streaming response is sent as it is computed. That is exactly why an LLM can emit one token at a time.

---

### 2. Apifox 接口接入测试 / API Integration Testing with Apifox

**中文**

Apifox 的价值不只是"发个请求看看返回"，而是把接口测试变成可重复的资产：

- **环境变量**：把 `{{baseUrl}}` 抽出来，本地、测试、线上切换环境时不用改请求。
- **断言（Assertions）**：不只看状态码，还要断言 body 里的字段。比如 `$.error` 不存在、`$.message.content` 非空。
- **前置/后置脚本**：可以在请求前生成参数、请求后把返回值存进变量，供下一个请求使用（接口串联）。
- **流式响应**：调流式接口时，Apifox 会把返回显示成多行 JSON，需要逐行看。

一个实践顺序建议：**先关掉流式（`stream: false`）把接口调通，再打开流式看真实效果**。混在一起调，出错了分不清是协议问题还是流式解析问题。

**English**

The value of Apifox is not merely "send a request and eyeball the response" — it turns API testing into a repeatable asset:

- **Environment variables**: extract `{{baseUrl}}` so switching between local, staging and production needs no edits to the request.
- **Assertions**: don't stop at the status code; assert on body fields too, e.g. `$.error` is absent and `$.message.content` is non-empty.
- **Pre-request / post-response scripts**: generate parameters before the call, and store returned values into variables for the next request (request chaining).
- **Streaming responses**: for streaming endpoints Apifox renders the response as multiple lines of JSON; you have to read them line by line.

A practical order I'd recommend: **turn streaming off (`stream: false`) and get the endpoint working first, then turn streaming on.** Debugging both at once makes it impossible to tell whether the problem is in the protocol or in the stream parsing.

---

### 3. 上下文会话记忆方案 / Context & Conversation Memory

**中文**

这是今天最颠覆认知的一点：**大模型接口本身没有记忆**。

所谓"它记得我"是一种错觉。真相是客户端每一轮都把**完整的对话历史**重新发一遍：

```json
"messages": [
  {"role": "system",    "content": "你是一个助手"},
  {"role": "user",      "content": "第一轮问题"},
  {"role": "assistant", "content": "第一轮回答"},
  {"role": "user",      "content": "第二轮问题"}
]
```

由此推出几个必然的工程问题：

- **上下文有上限**：模型有 `num_ctx`，历史无限堆积迟早溢出。必须有策略。
- **三种常见策略**：① 滑动窗口，只保留最近 N 轮；② 摘要压缩，把旧对话压缩成一段摘要；③ 向量记忆，把历史存进向量库，按需检索相关片段。
- **持久化**：要把对话存进数据库（SQLite 就够了），否则一关页面就全忘了。
- **Token 成本**：每多一轮历史，每次请求的输入 token 都在增长。这不是"免费的记忆"。

**English**

This was the most perspective-shifting point of the day: **the model API has no memory of its own.**

"It remembers me" is an illusion. In reality the client resends the **entire conversation history** on every turn:

```json
"messages": [
  {"role": "system",    "content": "You are an assistant"},
  {"role": "user",      "content": "First question"},
  {"role": "assistant", "content": "First answer"},
  {"role": "user",      "content": "Second question"}
]
```

Several engineering consequences follow:

- **Context is bounded**: the model has a `num_ctx` limit; unbounded history will eventually overflow. You need a strategy.
- **Three common strategies**: (1) sliding window — keep only the last N turns; (2) summarisation — compress older turns into a summary; (3) vector memory — store history in a vector store and retrieve relevant fragments on demand.
- **Persistence**: conversations must be written to a database (SQLite is enough), otherwise everything is lost when the page closes.
- **Token cost**: every extra turn grows the input tokens of every subsequent request. Memory is not free.

---

### 4. 本地部署 DeepSeek / Running DeepSeek Locally

**中文**

本地部署的核心矛盾只有一个：**参数量 vs 显存**。

- 模型要**全部加载进显存**才能全速运行；装不下就会溢出到内存，速度断崖式下跌。
- 量化（Quantisation）是主要手段：把权重从 16 位浮点压到 4 位，体积大约降到 1/4，精度损失在可接受范围内。`Q4_K_M` 是最常用的性价比档位。
- 粗略估算：**显存 ≈ 参数量 × 0.6~0.7 GB（4 位量化）**，再留 1~2 GB 给 KV 缓存和系统。

一个重要的认知：**"参数量越新越好"在本地不成立**。2026 年最新的 DeepSeek 旗舰是几百 B 的 MoE，消费级显卡根本放不下；反倒是小尺寸的蒸馏版才是本地可用解。选模型要看"能不能跑得动"，不是"是不是最新"。

**English**

Local deployment boils down to one trade-off: **parameter count vs VRAM**.

- The model must be **fully loaded into VRAM** to run at full speed; if it doesn't fit, it spills into system RAM and throughput collapses.
- Quantisation is the main tool: weights are compressed from 16-bit floats to 4-bit, roughly a quarter of the size, at an acceptable accuracy cost. `Q4_K_M` is the usual sweet spot.
- Rule of thumb: **VRAM ≈ parameter count × 0.6–0.7 GB (4-bit)**, plus 1–2 GB headroom for the KV cache and the OS.

An important realisation: **"newer and bigger is better" does not hold locally.** In 2026 the flagship DeepSeek models are several-hundred-billion-parameter MoE models that no consumer GPU can hold; the small distilled variants are what actually run. Choose a model by whether it runs, not by whether it is the newest.

---

## 三、今天的实践 / Hands-on Work

| 操作 / Action | 结果 / Result |
|---|---|
| 删除本地 `qwen3:8b` | 释放 5.2 GB / Freed 5.2 GB |
| 安装 `deepseek-r1:8b` | 5.2 GB，Q4_K_M，128K 上下文 / 5.2 GB, Q4_K_M, 128K context |
| 速度实测 / Benchmark | **61.9 tok/s，100% GPU**（8K 上下文） |
| 16K 上下文实测 | 7.8 GB，20% 回落到 CPU，明显变慢 / spills 20% to CPU, much slower |
| 安装嵌入模型 / Embedding model | `qwen3-embedding:0.6b`（639 MB） |
| 搭建本地 RAG / Built a local RAG tool | 纯标准库，零依赖 / stdlib only, zero dependencies |

**关于模型选型的发现 / A finding on model selection**

Ollama 上 `deepseek-r1:8b` 这个标签实际对应 **DeepSeek-R1-0528-Qwen3-8B**——2025 年 5 月的 0528 更新版，基于 Qwen3-8B 蒸馏，不是早期基于 Llama 3.1 的版本。查元信息可以确认：`architecture = qwen3`、`8.2B` 参数、支持 `tools` 和 `thinking`。

The `deepseek-r1:8b` tag on Ollama actually maps to **DeepSeek-R1-0528-Qwen3-8B** — the May 2025 0528 refresh, distilled onto Qwen3-8B rather than the earlier Llama 3.1 base. Confirmed by the model metadata: `architecture = qwen3`, 8.2B parameters, with `tools` and `thinking` capabilities.

---

## 四、踩过的坑 / Pitfalls Hit

**1. 状态码 200 不代表成功**
Ollama 出错时常常返回 200，错误信息放在 body 的 `error` 字段里。断言只看状态码会漏。

A `200` does not mean success. Ollama often returns 200 with the error inside the body's `error` field, so asserting on the status code alone misses failures.

**2. 流式是 NDJSON，不是 SSE**
`stream: true` 返回的是**每行一个独立 JSON**（NDJSON），不是 `data: ...` 格式的 Server-Sent Events。想用 `EventSource` 直接接是接不上的，得用 `fetch` + `ReadableStream` 自己按行解析。

Streaming returns **NDJSON** — one JSON object per line — not SSE. You cannot consume it with `EventSource`; you need `fetch` + `ReadableStream` and parse line by line.

**3. 思考型模型有隐藏字段**
`deepseek-r1` 流式返回时，思考过程在 `message.thinking` 里，正式答案在 `message.content` 里。只读 `content` 会看到几秒钟空白然后突然出字。

For reasoning models, the chain of thought streams in `message.thinking` while the answer streams in `message.content`. Reading only `content` shows several seconds of silence followed by a sudden burst.

**4. 上下文开大反而变慢**
从 8192 提到 16384，显存不够，20% 的计算回落到 CPU，速度掉一大截。「更大的上下文」不是免费的。

Raising context from 8192 to 16384 exceeded VRAM; 20% of the compute fell back to the CPU and throughput dropped sharply. A larger context is not free.

**5. 「更新知识库」不是 `ollama pull`**
模型权重是冻结的，`pull` 只是换模型文件。要让它懂你的资料，得靠 RAG（检索增强）或微调，前者成本低得多。

You cannot "update a model's knowledge" with `ollama pull` — weights are frozen. To make it know your documents you need RAG (much cheaper) or fine-tuning.

---

## 五、关键术语对照 / Glossary

| 中文 | English | 一句话解释 / One-liner |
|---|---|---|
| 请求 / 响应 | Request / Response | HTTP 的一问一答 / the question-and-answer of HTTP |
| 状态码 | Status code | 三位数字表示结果类别 / three digits describing the outcome |
| 分块传输 | Chunked transfer | 边算边发，流式的基础 / send as computed, the basis of streaming |
| 无状态 | Stateless | 服务端不记得上一次 / the server recalls nothing |
| 断言 | Assertion | 自动检查返回是否符合预期 / automatically check the response |
| 环境变量 | Environment variable | 把地址等配置抽出来复用 / extract config for reuse |
| 上下文窗口 | Context window | 模型一次能"看见"的 token 上限 / max tokens visible at once |
| 滑动窗口 | Sliding window | 只保留最近 N 轮对话 / keep the last N turns |
| 摘要压缩 | Summarisation | 把旧对话压成一段话 / compress old turns into a paragraph |
| 向量检索 | Vector retrieval | 按语义相似度找相关片段 / find fragments by semantic similarity |
| 量化 | Quantisation | 降低权重精度以减小体积 / lower weight precision to shrink size |
| 显存 | VRAM | 显卡上的内存，决定模型能否全速 / GPU memory, decides full speed |
| 蒸馏 | Distillation | 用小模型学大模型的推理模式 / small model learning a big one's reasoning |
| 检索增强生成 | RAG | 先查资料再回答 / retrieve first, then answer |

---

## 六、下一步 / Next Steps

- [ ] 在 Apifox 里把 Ollama 的 `/api/chat`、`/api/embed`、`/api/tags` 建成一个带环境变量和断言的集合
- [ ] 用 SQLite 实现真正的持久化会话记忆，加上摘要压缩
- [ ] 试试把 RAG 接到对话流程里，验证"多轮对话 + 知识库"能否协同工作
- [ ] 了解 MoE 架构和 CPU/GPU 混合推理，看能否让更大的模型在 8G 显存上"跑得动"

- [ ] Build an Apifox collection for Ollama's `/api/chat`, `/api/embed` and `/api/tags` with environment variables and assertions
- [ ] Implement real persistent memory with SQLite, including summarisation
- [ ] Wire RAG into the chat loop and check that multi-turn dialogue and the knowledge base work together
- [ ] Look into MoE architectures and hybrid CPU/GPU inference to see whether larger models can run on 8 GB of VRAM

---

## 七、一句话总结 / One-Sentence Summary

**中文**：HTTP 让请求能送到、Apifox 让请求可验证、会话记忆让请求有历史、本地模型让请求不必出网——四层拼起来，才是一个能用的本地 AI 应用。

**English**: HTTP gets the request there, Apifox makes it verifiable, conversation memory gives it history, and a local model keeps it off the internet — four layers, one usable local AI application."""