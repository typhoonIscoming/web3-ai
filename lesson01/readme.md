# 第 1 课：AI 开发提效全景与工具对比

> 课程视频回放：[点击观看](https://appibxs98ig9955.h5.xet.pomoho.com/p/course/video/v_6a1c554ce4b0694c5bcdda9c?product_id=course_2xArq45EVWERVb4oHPYEmCLzHG5&course_id=course_2xArq45EVWERVb4oHPYEmCLzHG5&sub_course_id=subcourse_3EUmreviThPpAUC2IJ1NTqoDbk5)

---

## 一、环境准备

### Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version                            # 验证安装
claude                                      # 首次运行会引导登录
```

### Cursor

1. 从 <https://cursor.com> 下载安装
2. 登录后可直接使用，有 VS Code 配置的直接导入

### 验证

```bash
claude --version
```

---

## 二、AI 开发的三种模式

| 模式 | 代表工具 | 特点 |
| ------ | ---------- | ------ |
| **聊天式** | ChatGPT / Claude.ai | 复制粘贴，人工搬运代码 |
| **IDE 内嵌** | Cursor | 在编辑器里直接补全或对话，上下文自动注入 |
| **命令式（Agent）** | Claude Code / Codex | 在终端中执行，能读写文件、跑命令、自主决策 |

**关键认知**：从左到右，AI 的自主性递增，人的干预递减。

选型不是"哪个最好"，而是**不同任务用不同模式**：

- 探索性问题 → 聊天式
- 日常编码 → IDE 内嵌
- 多文件重构、自动化任务 → 命令式 Agent

---

## 三、三大工具速览

### Claude Code

- 终端 Agent，能读写文件、执行命令、自主推进
- 支持 MCP 接入外部资源、Skill 能力沉淀、Hooks 自动化
- 适合：复杂任务、多文件操作、工作流自动化

### Cursor

- VS Code 深度 fork，AI 原生 IDE
- Tab 补全 + 内联编辑 + 聊天面板 + Agent 模式
- 适合：日常编码、快速迭代、可视化 diff

### Codex

- OpenAI 出品，有两种形态：Codex CLI（本地终端 Agent，类似 Claude Code）和 Codex Cloud（云端沙箱异步执行）
- CLI 开源免费，Cloud 适合批量任务分发
- 适合：本地快速编辑（CLI）、并行处理多个独立任务（Cloud）

> 本课程以 **Claude Code + Cursor** 为主线，Codex 作为对照参考。

### 工具对比矩阵

| 维度 | Claude Code | Cursor | Codex |
| ------ | ------------ | -------- | ------- |
| **交互模式** | 终端 Agent | AI IDE | 云端 Agent |
| **自主性** | 高（自主读写文件、执行命令） | 中（IDE 内操作，需确认） | 高（沙箱异步执行） |
| **上下文能力** | 全项目 + MCP 外部资源 | 当前项目文件 | 任务描述 + 仓库快照 |
| **扩展性** | MCP / Skill / Hooks / Rules | Rules（.cursor/rules/）/ MCP | 有限 |
| **适用场景** | 多文件重构、自动化、工作流 | 日常编码、快速迭代 | 批量异步任务 |
| **学习曲线** | 中（需熟悉终端） | 低（VS Code 用户无缝上手） | 中 |
| **价格** | Pro $20/月，Max $100 或 $200/月 | Pro $20/月（credit 制） | CLI 免费，需 ChatGPT 订阅（$20/月起）或 API key |

> 没有"最好的工具"，只有最适合当前任务的工具。实际工作中通常组合使用。

### 社区增强生态

AI 开发工具的能力不止于官方，社区生态正在快速扩展：

- **Everything Claude Code (ECC)**：为 Claude Code 提供 agent 配置优化、专用 skill、代码审查流程等增强能力
- **Superpowers**：AI agent 开发方法论框架，提供标准化的 skill 设计与执行模式

这些生态在后续课程中会逐步接触，本节只需知道它们的定位。

---

## 四、Cursor 与 Claude Code 基础技巧

以下都是**第一天就能用**的基础操作，每款工具各 10 条。Hooks、Skills、MCP、多 Agent 等进阶能力放到后续课程讲。

### Cursor 基础技巧

1. **Tab 链式补全**：在行尾按 Tab 接受整段补全，再按 Tab 可跳到下一个建议点。配合写个变量名或注释，AI 常能自动补完整函数。

2. **Ctrl+K 行内改写**：选中代码 → `Ctrl+K` → 用自然语言描述改动，直接在原位置出 diff。适合重命名、改样式、调参数。

3. **Ctrl+I 打开 Composer/Agent**：选中代码 + `Ctrl+I` 把代码作为上下文开 Agent 对话，用于跨文件重构或写新模块。

4. **终端里的 Ctrl+K**：在 Cursor 集成终端里按 `Ctrl+K`，用中文描述就能生成 shell 命令（如"列出最近 5 个 git 分支"），不用再查参数。

5. **Ctrl+L 打开 Chat**：`Ctrl+L` 召唤侧边聊天窗口，问代码、找 bug、学库用法都走这里，最轻量的入口。

6. **`@` 引用文件 / 符号**：输入 `@` 可选择文件、文件夹、函数、Git 改动，让 AI 精准看到你指的东西，比贴代码快。

7. **`@docs` 拉官方文档**：`@docs` 选框架文档（内置 30+ 主流库），避免 AI 用过时 API。

8. **`.cursorrules` 项目规则**：项目根目录放一个 `.cursorrules`，写上技术栈、代码风格、禁用项，每次对话自动注入——让 AI 输出风格稳定的第一招。

9. **源代码管理里的 ✨ 生成 commit**：左侧源代码管理面板点魔法棒图标，自动根据 diff 生成 commit message，不满意手动改即可。

10. **模型切换按需选**：日常用 Sonnet 便宜快；遇到难题（大重构、架构决策、疑难 bug）手动切 Opus 或 GPT 系列，对话框底部下拉直接切。

### Claude Code 基础技巧

1. **`/init` 生成 CLAUDE.md**：进到一个新项目先跑 `/init`，它会扫代码库生成一份记忆文件基座，后续 AI 每次都会自动读这个文件。

2. **`@` 引用文件**：对话里输入 `@src/auth/login.ts`，Claude 会直接读这个文件，不用你贴代码或描述路径。

3. **拖图 / 粘截图**：错误截图、UI 设计稿、日志图直接粘进终端，Claude 能看懂（视觉多模态）。

4. **Plan Mode（Shift+Tab）**：按 `Shift+Tab` 进入计划模式，Claude 只读代码、答问题、出方案，不动文件。确认方案后再切回普通模式执行。

5. **`/clear` 清上下文**：换任务一定要 `/clear`。上下文越满 AI 越笨，这是保持效果最简单的一招。

6. **`Esc` 打断 / `Esc+Esc` 回滚**：发现 AI 跑偏按一下 `Esc` 立刻停；双击 `Esc` 打开检查点菜单，可以把对话或代码回到任一历史节点。

7. **`claude --continue` 续上次会话**：终端关了重开也能用 `claude --continue` 接着昨天的对话，上下文不丢。

8. **管道输入日志**：`cat error.log | claude "分析这个错误"`，直接把原始输出灌给 AI，比转述精确 10 倍。

9. **让 AI 验证自己**：请求里带一句"写完跑一下测试 / build / lint，有错就修"，AI 会自己闭环，不需要你来回传错误。

10. **具体而不是模糊**："给 foo.py 补测试" ❌ / "给 foo.py 补一个『用户已登出』的边界测试，参考 tests/ 下现有写法，不要用 mock" ✅。越具体，返工越少。

### 两款通用的心法

- **描述越具体，返工越少**：告诉 AI 改哪里、参考什么样例、怎样算做完。
- **让 AI 自检**：给一个可验证信号（测试、lint、build、截图），比你手动审省力。
- **两次纠错就重来**：同一个问题改两次还不对，上下文已经乱了，清空重开比继续拉锯快。

### 延伸阅读

- Claude 官方：[Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices)
- Cursor 官方：[Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

---

## 五、现场演示：Claude Code vs Cursor

同一个任务，同一句 Prompt，两种工具并排演示。

**任务**：从零编写一个 Python 脚本，获取最近一个月的比特币行情数据并绘制 K 线图。

**Prompt**（两边用同样的话）：

```
帮我在[claude-demo/cursor-demo]文件夹中，写一个python脚本，来实现一下比特币行情数据的获取，获取最近一个月的比特币的行情数据，并且在本地绘制K线图
```

| 环节 | Claude Code | Cursor |
| ------ | ------------ | -------- |
| **启动** | 终端输入 `claude`，粘贴 Prompt | 打开项目，Agent 模式粘贴 Prompt |
| **创建文件** | 自动创建 `claude-demo/btc_kline.py` | 自动创建 `cursor-demo/btc_kline.py` |
| **安装依赖** | 自主执行 `pip install` 安装所需库 | 自主执行 `pip install` 安装所需库 |
| **运行验证** | 自主执行脚本，确认数据获取与图片生成 | 自主执行脚本，确认数据获取与图片生成 |
| **整体体验** | 纯终端，适合无 IDE 场景 | 可视化 diff，改动一目了然 |

现场重点观察：

- 两边生成的代码在**结构、风格、注释**上有什么差异
- 从输入 Prompt 到脚本成功运行并输出 K 线图，各自花了多少**轮次**

---

## 六、作业

分别用 Claude Code 和 Cursor 完成以下任务，提交代码和对比报告。

### 任务：写一个加密货币行情监控脚本

用 Python 实现一个命令行工具，功能要求：

1. **行情获取**：从 Binance 或 CoinGecko API 获取指定币种（至少支持 BTC、ETH）的实时价格
2. **价格预警**：用户可设定价格阈值，价格突破时在终端输出告警信息
3. **数据持久化**：将每次查询的价格记录存入本地 SQLite 数据库
4. **统计查询**：支持查询某币种过去 N 条记录的最高价、最低价、均价
5. **命令行交互**：用 `argparse` 或 `click` 实现子命令（如 `watch`、`alert`、`stats`）

### 提交内容

1. 两份代码（Claude Code 生成的和 Cursor 生成的）
2. 对比报告：

| 维度 | Claude Code | Cursor |
| ------ | ------------ | -------- |
| 交互轮次（从开始到功能完整可运行） | | |
| 代码结构（文件拆分、模块划分是否合理） | | |
| 错误处理（网络超时、无效输入等是否覆盖） | | |
| 是否主动补写了测试 | | |
| 主观体验评分（1-5） | | |

1. 结论：你后续会优先使用哪个工具，为什么。
