# NLP / LLM 完整学习计划

> 目标：从 Python 基础到能独立开发 LLM 应用，预计 6-9 个月

---

## 总览时间线

| 阶段 | 内容 | 时间 | 难度 |
|------|------|------|------|
| 阶段一 | Python 进阶 + 数学基础 | 3-4 周 | ⭐ |
| 阶段二 | 机器学习入门 | 3-4 周 | ⭐⭐ |
| 阶段三 | 深度学习 + PyTorch | 4-6 周 | ⭐⭐⭐ |
| 阶段四 | NLP 经典方法 | 4-6 周 | ⭐⭐⭐ |
| 阶段五 | Transformer + 预训练模型 | 6-8 周 | ⭐⭐⭐⭐ |
| 阶段六 | LLM 深入 + RAG + 微调 | 6-8 周 | ⭐⭐⭐⭐⭐ |
| 阶段七 | AI Agent + 工程化实战 | 4-6 周 | ⭐⭐⭐⭐⭐ |

---

## 阶段一：Python 进阶 + 数学基础（3-4 周）

### 1.1 Python 数据科学生态

**学习内容：**
- NumPy：数组创建、索引切片、广播机制、矩阵运算、线性代数函数
- Pandas：DataFrame 操作、数据读取（CSV/Excel/JSON）、数据清洗、分组聚合、缺失值处理
- Matplotlib / Seaborn：折线图、柱状图、散点图、热力图、子图布局
- 常用标准库：json、os、re、collections、itertools

**B站视频：**
- 【Python 数据分析必备教程】搜索关键词：`NumPy Pandas 入门` — 推荐频道：`莫烦Python`（基础简短易懂）
- 【Python 科学计算 NumPy 完整教程】搜索关键词：`NumPy 完整教程 数据科学`
- 【Pandas 从入门到实战】搜索关键词：`Pandas 数据分析 实战`

**GitHub 教程：**
- [numpy-100](https://github.com/rougier/numpy-100) — 100 道 NumPy 练习题，从简单到进阶
- [pandas_exercises](https://github.com/guipsamora/pandas_exercises) — Pandas 练习题集
- [matplotlib-cheatsheet](https://github.com/matplotlib/cheatsheets) — Matplotlib 官方速查表

**阶段目标：**
- [ ] 能用 NumPy 实现矩阵乘法、转置、求逆
- [ ] 能用 Pandas 读取 CSV 并做数据清洗和统计
- [ ] 能用 Matplotlib 画出基本图表

---

### 1.2 数学基础（够用即可）

**学习内容：**
- 线性代数：向量、矩阵运算、特征值分解、SVD
- 概率统计：贝叶斯定理、概率分布、期望方差、最大似然估计
- 微积分：导数、偏导数、链式法则、梯度

**B站视频：**
- 【3Blue1Brown 线性代数的本质】搜索关键词：`3Blue1Brown 线性代数的本质` — 可视化讲解，强烈推荐
- https://www.bilibili.com/video/BV1XxEL6LESR/?spm_id_from=333.337.search-card.all.click
- 【3Blue1Brown 微积分的本质】搜索关键词：`3Blue1Brown 微积分的本质`
- https://www.bilibili.com/video/BV1qW411N7FU/?spm_id_from=333.337.search-card.all.click
- 【概率论速成】搜索关键词：`概率论 速成 数据科学`

**GitHub 教程：**
- [mathematics-for-machine-learning](https://github.com/mjwen/mathematics-for-machine-learning) — 机器学习数学基础笔记
- [ML-Math](https://github.com/TomHAnderson/ML-Math) — ML 所需数学知识汇总

**阶段目标：**
- [ ] 理解矩阵乘法在神经网络中的作用
- [ ] 理解梯度下降的数学原理
- [ ] 理解贝叶斯定理

---

## 阶段二：机器学习入门（3-4 周）

### 2.1 经典机器学习算法

**学习内容：**
- 监督学习：线性回归、逻辑回归、决策树、随机森林、SVM、KNN
- 无监督学习：K-Means 聚类、PCA 降维
- 模型评估：交叉验证、过拟合/欠拟合、精确率/召回率/F1、ROC/AUC
- 特征工程：标准化、归一化、特征选择

**B站视频：**
- 【吴恩达机器学习】搜索关键词：`吴恩达 机器学习 2022` — 经典中的经典，有中文版
- https://www.bilibili.com/video/BV1owrpYKEtP/?spm_id_from=333.337.search-card.all.click
- 【李宏毅机器学习】搜索关键词：`李宏毅 机器学习 2024` — 中文讲解，通俗易懂，更新到最新
- https://www.bilibili.com/video/BV1ruqABeEFX/?spm_id_from=333.337.search-card.all.click
- 【机器学习速成课程】搜索关键词：`Google 机器学习速成` — Google 官方出品，快速入门
- https://www.bilibili.com/video/BV1dW411s7KS/?spm_id_from=333.337.search-card.all.click

**GitHub 教程：**
- [machine-learning-course](https://github.com/ageron/handson-ml3) — 《动手学机器学习》配套代码（sklearn 实战）
- [mlcourse.ai](https://github.com/mlcourse/mlcourse.ai) — 开源机器学习课程，含练习
- [scikit-learn 官方教程](https://scikit-learn.org/stable/tutorial/) — sklearn 官方教程

**实战项目：**
- 房价预测（回归）
- 鸢尾花分类（分类）
- 客户分群（聚类）

**阶段目标：**
- [ ] 能用 sklearn 训练和评估模型
- [ ] 理解偏差-方差权衡
- [ ] 完成 2-3 个小项目

---

## 阶段三：深度学习 + PyTorch（4-6 周）

### 3.1 神经网络基础

**学习内容：**
- 感知机、多层感知机（MLP）
- 激活函数：ReLU、Sigmoid、Tanh、Softmax
- 反向传播、梯度下降、学习率
- 正则化：Dropout、BatchNorm、权重衰减
- 优化器：SGD、Adam、AdamW

### 3.2 PyTorch 框架

**学习内容：**
- Tensor 操作、自动求导（autograd）
- nn.Module、数据加载（Dataset/DataLoader）
- 模型训练循环：前向传播 → 计算损失 → 反向传播 → 更新参数
- 模型保存与加载
- GPU 加速训练

**B站视频：**
- 【刘二大人 PyTorch 教程】搜索关键词：`刘二大人 PyTorch` — 中文 PyTorch 入门最佳
- https://www.bilibili.com/video/BV1Y7411d7Ys/?spm_id_from=333.337.search-card.all.click
- 【小土堆 PyTorch 教程】搜索关键词：`小土堆 PyTorch` — 保姆级教程，非常细致
- https://www.bilibili.com/video/BV1QpsXzyEAK/?spm_id_from=333.337.search-card.all.click
- 【吴恩达深度学习】搜索关键词：`吴恩达 深度学习` — 理论基础，配合 PyTorch 实践
- https://www.bilibili.com/video/BV12urfB1E7s/?spm_id_from=333.337.search-card.all.click

**GitHub 教程：**
- [pytorch-tutorial](https://github.com/yunjey/pytorch-tutorial) — PyTorch 从入门到进阶，代码简洁
- [d2l-pytorch](https://github.com/d2l-ai/d2l-pytorch) — 《动手学深度学习》PyTorch 版
- [pytorch-deep-learning](https://github.com/mrdbourke/pytorch-deep-learning) — PyTorch 深度学习完整教程

**实战项目：**
- MNIST 手写数字识别
- CIFAR-10 图像分类
- 自定义数据集训练

**阶段目标：**
- [ ] 能独立用 PyTorch 搭建和训练神经网络
- [ ] 理解反向传播的完整流程
- [ ] 能使用 GPU 加速训练

---

## 阶段四：NLP 经典方法（4-6 周）

### 4.1 NLP 基础

**学习内容：**
- 文本预处理：分词（jieba）、停用词、词干化
- 文本表示：One-Hot、TF-IDF、词袋模型
- 词向量：Word2Vec（CBOW / Skip-gram）、GloVe
- 中文 NLP 特点：分词、编码（UTF-8）

### 4.2 序列模型

**学习内容：**
- RNN 原理：隐藏状态、序列建模
- 梯度消失/爆炸问题
- LSTM：遗忘门、输入门、输出门
- GRU：简化版门控单元
- 双向 RNN、Seq2Seq 架构
- Attention 机制（重点理解！Transformer 的前身）

**B站视频：**
- 【斯坦福 CS224N NLP 深度学习】搜索关键词：`CS224N 自然语言处理` — NLP 最权威课程
- https://www.bilibili.com/video/BV1vQMBz6EvP/?spm_id_from=333.337.search-card.all.click
- 【李宏毅 NLP 相关章节】搜索关键词：`李宏毅 自然语言处理 Transformer`
- https://www.bilibili.com/video/BV1hM4y157xX/?spm_id_from=333.337.search-card.all.click
- 【Seq2Seq + Attention 讲解】搜索关键词：`Seq2Seq Attention机制 图解`
- https://www.bilibili.com/video/BV19u4m1T7JR/?spm_id_from=333.337.search-card.all.click

**GitHub 教程：**
- [nlp-tutorial](https://github.com/graykode/nlp-tutorial) — NLP 经典模型 PyTorch 实现（RNN/LSTM/Seq2Seq/Attention）
- [ChineseNlpCorpus](https://github.com/fighting41love/ChineseNlpCorpus) — 中文 NLP 数据集集合
- [jieba](https://github.com/fxsjy/jieba) — 中文分词工具

**实战项目：**
- 中文文本情感分类（LSTM）
- 中文分词对比实验
- 文本相似度计算

**阶段目标：**
- [ ] 理解 RNN → LSTM → Attention 的演进逻辑
- [ ] 能用 PyTorch 实现 LSTM 文本分类
- [ ] 理解 Attention 机制的原理

---

## 阶段五：Transformer + 预训练模型（6-8 周）⭐核心阶段

### 5.1 Transformer 架构

**学习内容：**
- Self-Attention 计算过程（Q/K/V）
- Multi-Head Attention
- 位置编码（Positional Encoding）
- Feed-Forward Network
- 残差连接 + Layer Normalization
- Encoder-Decoder 结构

### 5.2 预训练语言模型

**学习内容：**
- BERT：掩码语言模型（MLM）、下一句预测（NSP）、微调方法
- GPT 系列：自回归生成、因果语言模型
- Tokenizer：BPE、WordPiece、SentencePiece、tiktoken
- 模型微调：全参数微调、冻结层微调

### 5.3 Hugging Face 生态

**学习内容：**
- `transformers` 库：Pipeline、AutoModel、AutoTokenizer
- `datasets` 库：数据加载与处理
- `evaluate` 库：模型评估
- 模型下载与使用、模型上传与分享

**B站视频：**
- 【Transformer 原理讲解】搜索关键词：`Transformer 原理 图解 详解` — 推荐找有动画演示的
- https://www.bilibili.com/video/BV1fj6vBfEnu/?spm_id_from=333.337.search-card.all.click
- 【手写 Transformer】搜索关键词：`手写 Transformer 从零实现 PyTorch`
- https://www.bilibili.com/video/BV1cCw9zrEjP/?spm_id_from=333.337.search-card.all.click
- 【Andrej Karpathy Let's build GPT】搜索关键词：`Karpathy 从零构建 GPT` — 从零手写 GPT，必看
- https://www.bilibili.com/video/BV1mqrTBvEaf/?spm_id_from=333.337.search-card.all.click
- 【Hugging Face 教程】搜索关键词：`Hugging Face Transformers 教程 中文`
- https://www.bilibili.com/video/BV1aNZ1BfEkY/?spm_id_from=333.337.search-card.all.click

**GitHub 教程：**
- [minGPT](https://github.com/karpathy/minGPT) — Karpathy 的极简 GPT 实现，代码仅 300 行
- [nanoGPT](https://github.com/karpathy/nanoGPT) — Karpathy 的 GPT 训练框架
- [transformers-tutorials](https://github.com/huggingface/transformers) — Hugging Face 官方仓库
- [annotated-transformer](https://github.com/harvardnlp/annotated-transformer) — 带注释的 Transformer 实现
- [The Annotated Transformer (中文)](https://github.com/AaronChuang/annotated_transformer_zh) — 中文注释版
- [transformer-explainer](https://github.com/hila-chefer/Transformer-Explainability) — Transformer 可解释性

**推荐论文（必读）：**
- Attention Is All You Need（Transformer 原始论文）
- BERT: Pre-training of Deep Bidirectional Transformers
- Language Models are Unsupervised Multitask Learners（GPT-2）
- Language Models are Few-Shot Learners（GPT-3）

**实战项目：**
- 用 BERT 做中文情感分析
- 用 GPT-2 做中文文本生成
- Fine-tune BERT 做命名实体识别（NER）

**阶段目标：**
- [ ] 能手写 Self-Attention 的计算过程
- [ ] 熟练使用 Hugging Face Transformers
- [ ] 完成 BERT 微调项目

---

## 阶段六：LLM 深入 + RAG + 微调（6-8 周）🔥重点阶段

### 6.1 Prompt Engineering

**学习内容：**
- Zero-shot、Few-shot、Chain-of-Thought（CoT）
- Prompt 模板设计、系统提示词
- 结构化输出（JSON mode）
- Prompt 注入防御

### 6.2 RAG（检索增强生成）

**学习内容：**
- RAG 架构：检索 → 增强 → 生成
- 文档加载与分割（Chunking 策略）
- Embedding 模型：text-embedding-ada-002、BGE、M3E
- 向量数据库：FAISS、ChromaDB、Milvus、Weaviate
- 检索策略：相似度搜索、混合检索、重排序
- RAG 评估：忠实度、相关性

### 6.3 模型微调

**学习内容：**
- 全参数微调 vs 参数高效微调（PEFT）
- LoRA / QLoRA 原理与实践
- SFT（监督微调）数据准备
- RLHF / DPO 对齐方法概述
- 评估微调效果

### 6.4 LLM 应用开发

**学习内容：**
- OpenAI API 调用、流式输出
- LangChain 核心概念：Chain、Agent、Memory、Tool
- LlamaIndex 文档问答框架
- 本地模型部署：Ollama、vLLM

**B站视频：**
- 【LangChain 教程】搜索关键词：`LangChain 教程 中文 2024`
- https://www.bilibili.com/video/BV178w1z7EHQ/?spm_id_from=333.337.search-card.all.click
- 【RAG 检索增强生成】搜索关键词：`RAG 检索增强生成 教程 实战`
- https://www.bilibili.com/video/BV1eecUz7ExG/?spm_id_from=333.337.search-card.all.click
- 【LoRA 微调实战】搜索关键词：`LoRA 微调 大模型 实战`
- https://www.bilibili.com/video/BV1DRqbBZEBY/?spm_id_from=333.337.search-card.all.click
- 【大模型应用开发】搜索关键词：`大模型应用开发 LLM API`
- https://www.bilibili.com/video/BV16aDpB4Er6/?spm_id_from=333.337.search-card.all.click

**GitHub 教程：**
- [langchain](https://github.com/langchain-ai/langchain) — LangChain 官方仓库
- [llama_index](https://github.com/run-llama/llama_index) — LlamaIndex 官方仓库
- [RAGFlow](https://github.com/infiniflow/ragflow) — 开源 RAG 引擎
- [FastChat](https://github.com/lm-sys/FastChat) — 开源 LLM 训练与部署平台
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) — 一站式 LLM 微调框架（支持中文，强烈推荐）
- [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) — 清华开源中文大模型
- [Qwen](https://github.com/QwenLM/Qwen) — 阿里通义千问开源模型
- [DeepSeek](https://github.com/deepseek-ai/DeepSeek-V3) — DeepSeek 开源模型
- [openai-cookbook](https://github.com/openai/openai-cookbook) — OpenAI 官方示例代码
- [prompt-engineering-guide](https://github.com/dair-ai/Prompt-Engineering-Guide) — 提示工程完整指南

**实战项目：**
- 搭建一个 PDF 文档问答系统（RAG）
- 用 LoRA 微调一个中文对话模型
- 开发一个基于 LangChain 的聊天机器人

**阶段目标：**
- [ ] 能独立搭建 RAG 应用
- [ ] 能用 LLaMA-Factory 微调开源模型
- [ ] 熟练使用 OpenAI API 或本地模型 API

---

## 阶段七：AI Agent + 工程化实战（4-6 周）🚀前沿方向

### 7.1 AI Agent

**学习内容：**
- Agent 架构：感知 → 规划 → 行动 → 反思
- ReAct 框架（推理 + 行动）
- Function Calling / Tool Use
- 多 Agent 协作系统
- Memory 系统：短期记忆、长期记忆、向量记忆

### 7.2 工程化

**学习内容：**
- API 服务化：FastAPI、Gradio、Streamlit
- 容器化：Docker 基础
- 模型量化：GPTQ、AWQ、GGUF
- 部署方案：Ollama（本地）、vLLM（服务器）、Serverless

**B站视频：**
- 【AI Agent 开发】搜索关键词：`AI Agent 开发 教程 LangChain Agent`
- https://www.bilibili.com/video/BV1wVEQ6cE85/?spm_id_from=333.337.search-card.all.click
- 【FastAPI 教程】搜索关键词：`FastAPI 教程 Python`
- https://www.bilibili.com/video/BV1SY7C6nETx/?spm_id_from=333.337.search-card.all.click
- 【Docker 入门】搜索关键词：`Docker 入门教程 2024`
- https://www.bilibili.com/video/BV1CJ411T7BK/?spm_id_from=333.337.search-card.all.click

**GitHub 教程：**
- [autogen](https://github.com/microsoft/autogen) — 微软多 Agent 框架
- [crewAI](https://github.com/crewAIInc/crewAI) — 多 Agent 协作框架
- [Dify](https://github.com/langgenius/dify) — 开源 LLM 应用开发平台（中文友好）
- [OpenDevin](https://github.com/OpenDevin/OpenDevin) — AI 软件开发 Agent
- [MetaGPT](https://github.com/geekan/MetaGPT) — 多 Agent 框架（中国团队）
- [ollama](https://github.com/ollama/ollama) — 本地运行大模型
- [open-webui](https://github.com/open-webui/open-webui) — Ollama 的 Web UI

**综合实战项目：**
- 开发一个能搜索网页 + 查询数据库的 Agent
- 搭建一个完整的 AI 应用（前后端 + 模型服务）
- 参与一个开源 AI 项目的贡献

---

## 持续学习资源

### 必关注的 GitHub 仓库
- [llm-course](https://github.com/mlabonne/llm-course) — LLM 学习路线图（持续更新）
- [LLM101n](https://github.com/karpathy/llm101n) — Karpathy 的 LLM 课程（建设中）
- [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) — 提示词集合
- [transformers](https://github.com/huggingface/transformers) — Hugging Face 主仓库

### 必关注的 B站频道/UP主
- 李宏毅（机器学习/深度学习/LLM 最新课程）
- 刘二大人（PyTorch 教程）
- 莫烦Python（基础教程，简短易懂）
- 小土堆（PyTorch 保姆级教程）

### 论文阅读建议
- 不要一开始就读论文，阶段五之后再开始
- 优先读综述类论文，建立全局认知
- 用 [Connected Papers](https://www.connectedpapers.com/) 找相关论文
- 中文论文解读：搜索 `XXX 论文解读` 有很多优质博客

### 社区与资讯
- Hugging Face 社区：模型、数据集、Space
- 知乎 AI/NLP 话题
- 机器之心、量子位（公众号/网站）
- arXiv 每日论文推送（后期）

---

## 每日学习建议

| 时间段 | 活动 |
|--------|------|
| 1-2 小时 | 看视频课程，理解概念 |
| 1-2 小时 | 写代码实践，跑实验 |
| 30 分钟 | 整理笔记，记录疑问 |
| 周末 | 做项目，复习本周内容 |

---

## 学习心态建议

1. **不要追求全部看完** — 视频看 60% 理解了就动手写代码
2. **遇到不懂的先跳过** — 很多概念学完后面回头看就懂了
3. **代码一定要自己敲** — 复制粘贴学不会任何东西
4. **记录学习笔记** — 用自己的话总结，比看十遍视频有效
5. **找学习伙伴或社区** — 独学而无友则孤陋而寡闻
6. **保持耐心** — 这是一个长期过程，每天进步一点点

---
