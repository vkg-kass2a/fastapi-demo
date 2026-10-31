from fastapi import FastAPI
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

app = FastAPI()

# ========== 准备阶段 ==========

# 1. 输出的形状（从 demo5.py 抄过来）
class ResumeInfo(BaseModel):
    name: str = Field(description="姓名")
    school: str = Field(description="毕业院校")
    major: str = Field(description="专业")
    years: int = Field(description="工作年限，没有就填 0")
    skills: list[str] = Field(description="掌握的技能列表")

# 2. 输入的形状（这是新的，你自己想）
class ResumeRequest(BaseModel):
    resume_text: str

# 3. 建 LLM（从 demo5.py 抄，注意这里要写 llm = ChatOpenAI(...)）
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
)

# 4. 搭链
structured_llm = llm.with_structured_output(ResumeInfo, method="function_calling")
prompt = ChatPromptTemplate.from_template("请提取这份简历的信息：{resume}")
chain = prompt | structured_llm

# ========== 请求阶段 ==========

@app.post("/extract")
def extract_resume(request: ResumeRequest):
    result = chain.invoke({"resume": request.resume_text})   # ← 应该是请求发来的
    return result
