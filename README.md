# langchain-learning

**建设中**

本仓库记录了一些个人学习Langchain过程中的经验

## 执行Notebook的准备工作

touch a `.env` file and add environment variables before you run the notebook:

**azure config**
```
OPENAI_API_TYPE=azure
OPENAI_API_VERSION=2023-05-15
OPENAI_API_BASE=https://`YOUR_AZURE_OPENAI_ENDPOINT`.openai.azure.com/
OPENAI_API_KEY=`YOUR_AZURE_OPENAI_KEY`
OPENAI_DEPLOYMENT_ID=`YOUR_AZURE_OPENAI_DEPLOYMENT_ID`
OPENAI_MODEL=gpt-3.5-turbo  # gpt-3.5-turbo or gpt-4 or gpt-4-32k
```

**openai config**
```
OPENAI_API_KEY=`YOUR_OPENAI_KEY`
OPENAI_MODEL=gpt-3.5-turbo  # gpt-3.5-turbo or gpt-4 or gpt-4-32k
```

**代理**
```
OPENAI_PROXY=`YOUR_HTTP_PROXY`
```
