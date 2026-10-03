# AI 智能伴侣（AI Partner）

一个基于 **Streamlit** 和 **DeepSeek 大模型** 的 AI 聊天助手 Web 应用。通过 OpenAI 兼容接口调用 DeepSeek 的 `deepseek-flash` 模型，实现了带「思考模式」的对话机器人。

> 本项目用于演示如何快速搭建一个接入大语言模型的应用。

## 🖼️ 界面预览

![AI 智能伴侣界面](resources/screenshot.png)

## ✨ 功能特点

- 🖥️ **Streamlit 网页界面**：简洁的聊天窗口，实时交互
- 🤖 **DeepSeek 大模型**：通过 OpenAI 兼容 SDK 调用 `deepseek-flash` 模型
- 🧠 **思考模式（Thinking）**：开启模型的推理过程，回答更严谨
- 🎭 **个性化人设**：通过系统提示词设定助手角色（幽默的「小丑」）
- 🔐 **安全的密钥管理**：API Key 通过环境变量读取，不硬编码在代码中

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

在环境变量中设置 DeepSeek 的 API Key（变量名为 `aipy_DEEPSEEK_API_KEY`）：

- **Windows（PowerShell）**

  ```powershell
  $env:aipy_DEEPSEEK_API_KEY = "你的密钥"
  ```

- **Linux / macOS**

  ```bash
  export aipy_DEEPSEEK_API_KEY="你的密钥"
  ```

> 申请 API Key 请前往 [DeepSeek 开放平台](https://platform.deepseek.com/)。

### 3. 启动应用

```bash
streamlit run ai_partner.py
```

浏览器会自动打开页面，输入问题即可与 AI 对话。

## 📁 项目结构

```
ai助手创建/
├── ai_partner.py          # 主应用：Streamlit 聊天界面 + 调用 DeepSeek
├── DeepSeek调用测试.py     # DeepSeek API 调用测试脚本
├── requirements.txt       # 依赖清单
└── resources/
    ├── logo.jpg           # 应用 Logo
    └── screenshot.png     # 界面截图
```

## 🔧 技术要点

- **OpenAI 兼容接口**：使用 `openai` SDK，将 `base_url` 指向 `https://api.deepseek.com`，无需额外安装 DeepSeek 专用 SDK。
- **思考模式**：通过 `extra_body={"thinking": {"type": "enabled"}}` 开启 DeepSeek 的思考过程。
- **响应方式**：当前使用非流式（`stream=False`）一次性返回结果。

## 📄 许可证

本项目仅用于学习与演示。
