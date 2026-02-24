# Decepticon修改版
原项目地址：https://github.com/PurpleAILAB/Decepticon
修改内容：支持国内大模型

# 安装与使用
```sh
git clone https://github.com/z1sec/Decepticon.git
cd Decepticon

uv venv
uv pip install -e .

# 并且记得在里面填好你需要使用模型平台的API
cp .env.example .env 

# 构建下kali和必要系统（网络好的情况下20分钟以内可构建完成）
docker-compose up -d 

# 启动必要的mcp
uv run python src/tools/mcp/Initial_Access.py
uv run python src/tools/mcp/Reconnaissance.py

# 启动web页面
uv run python -m streamlit run frontend/streamlit_app.py
```
![web页面1](/assets/image1.png)

![web页面2](/assets/image2.png)

# 自添加模型
可自行修改：src/utils/llm/custom_config.json
添加你需要的模型提供商，只要是支持openai的即可。