# codemind

**Code intelligence engine. Understand, analyze, and transform codebases with AI-powered insights.**

## 描述

codemind 通过静态分析和 AI 增强，提供代码库级别的智能理解和重构能力。

## 功能特性

- **代码理解**：深度语义分析代码结构
- **影响分析**：变更影响范围预测
- **重构建议**：智能重构机会识别
- **架构可视化**：自动生成架构图谱

## 安装

```bash
pip install codemind
```

## 使用

```bash
# 分析代码库
codemind analyze ./src --output report.json

# 查找重构机会
codemind refactor --target ./src --type extract-method

# 生成架构图
codemind graph --format mermaid --output arch.mmd
```

## 许可证

MIT