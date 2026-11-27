"""

**学习日志｜2026-11-27**

因为要学习大模型的调用，我还学习了网络工程的基础知识，重点是 IP、域名、端口和 HTTP/HTTPS：

- **IP**：一台设备在网络中的地址，负责定位"是哪台机器"
- **域名**：给人看的名字，通过 DNS 解析成 IP
- **端口**：同一台机器上不同服务的编号，`IP + 端口` 才能定位到具体服务
- **HTTP**：应用层协议，规定了请求和响应的格式——请求方法、路径、请求头、请求体、状态码
- **HTTPS**：HTTP 加上 TLS 加密，保证传输过程不被窃听和篡改，默认端口也从 80 变成 443

把这几个概念串起来，调用大模型就不再抽象了：本质上是向某个域名（解析成 IP）的某个端口，发送一次带请求头和 JSON 请求体的 HTTPS 请求，再解析返回的 JSON。本地部署时访问 `127.0.0.1:端口号`，就是这套规则最直观的例子。

---

**Learning Log | Nov 27, 2026**

Because I need to learn how to call large models, I also studied networking fundamentals, focusing on IP addresses, domain names, ports, and HTTP/HTTPS:

- **IP**: a device's address on the network — it identifies *which machine*
- **Domain name**: a human-friendly name that DNS resolves to an IP
- **Port**: a number that distinguishes services on the same machine; `IP + port` locates a specific service
- **HTTP**: the application-layer protocol that defines the format of requests and responses — method, path, headers, body, status codes
- **HTTPS**: HTTP secured with TLS, protecting traffic from eavesdropping and tampering, with the default port changing from 80 to 443

Putting these together makes calling an LLM concrete: it is simply sending an HTTPS request — with headers and a JSON body — to a port on some domain (which resolves to an IP), then parsing the returned JSON. Accessing `127.0.0.1:<port>` for a local deployment is the clearest example of these rules in action.
"""