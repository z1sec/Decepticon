# 自定义模型配置指南

## 支持的国内模型平台

Decepticon 现在支持多种国内 AI 模型平台，包括：

### 阿里云百炼 (DashScope)
- Qwen Turbo/Plus/Max 系列
- Qwen3 全系列 (72B, 32B, 14B, 7B, 4B, 1.8B, 0.5B)

### 零一万物 (01.AI)
- Yi-34B-Chat, Yi-34B, Yi-6B-Chat

### 智谱AI (Zhipu AI)
- GLM-4 系列 (Flash, Plus, Air, Long, FlashX, AllTools, Plus-Premier)
- CogView-3-Plus

### 月之暗面 (Moonshot AI)
- Kimi Chat 系列 (8K, 32K, 128K)

### 百川智能 (Baichuan)
- Baichuan4
- Baichuan3-Turbo 系列

### 讯飞星火 (iFlytek)
- Spark Pro, Max, Lite

### 腾讯混元 (HunYuan)
- HunYuan Lite, Standard, Standard-256K, Pro

## 配置方法

### 1. 环境变量设置
在 `.env` 文件中添加相应的 API 密钥：

```bash
# 阿里云百炼
DASHSCOPE_API_KEY=your-dashscope-api-key

# 零一万物
LINGYI_API_KEY=your-lingyi-api-key

# 智谱AI
ZHIPUAI_API_KEY=your-zhipuai-api-key

# 月之暗面
MOONSHOT_API_KEY=your-moonshot-api-key

# 百川智能
BAICHUAN_API_KEY=your-baichuan-api-key

# 讯飞星火
XFYUN_API_KEY=your-xfyun-api-key

# 腾讯混元
HUNYUAN_API_KEY=your-hunyuan-api-key
```

### 2. 使用自定义模型
启动 Decepticon 后，在模型选择界面中可以看到所有可用的模型。已配置 API 密钥的模型会显示为可用状态。

## 添加新的自定义模型

如果你想添加其他兼容 OpenAI API 的模型，可以编辑 `src/utils/llm/custom_config.json` 文件：

```json
{
  "display_name": "模型显示名称",
  "model_name": "模型API名称",
  "provider": "custom",
  "api_base": "https://your-api-endpoint.com/v1",
  "api_key_env": "YOUR_API_KEY_ENVIRONMENT_VARIABLE",
  "model_type": "openai_compatible"
}
```

### 配置参数说明：
- `display_name`: 在界面中显示的模型名称
- `model_name`: 调用 API 时使用的模型名称
- `provider`: 必须设置为 "custom"
- `api_base`: API 基础 URL
- `api_key_env`: 存储 API 密钥的环境变量名称
- `model_type`: 模型类型（目前只支持 openai_compatible）

## 测试模型连接

启动后可以通过 CLI 或 Web 界面查看模型状态，已正确配置的模型会显示为可用状态。

## 注意事项

1. 确保网络可以访问对应的 API 服务
2. 检查 API 密钥是否正确且有足够额度
3. 部分模型可能需要特定的区域访问权限
4. 建议先使用免费额度或测试模型进行验证