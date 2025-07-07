
import streamlit as st
import json
import openai
from openai import OpenAI

# 加载 Prompt 模板
def load_prompts():
    with open("prompt_templates.json", "r") as f:
        return json.load(f)

def extract_text_from_file(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        import fitz  # PyMuPDF
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc)
    elif file.name.endswith(".docx"):
        import docx
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return "Unsupported file format"

st.set_page_config(page_title="AI PRD Analyzer", layout="centered")

st.markdown("""
# 🤖 AI PRD 分析平台

欢迎来到 AI 驱动的产品文档分析工具 🪄  
本平台支持上传 PRD / 技术文档，并智能识别：
- 🧩 关键变更点
- ⚠️ 注意事项与潜在风险
- ✨ 创新亮点
- ✅ 自动测试用例建议

请上传文档，选择分析任务，并输入 OpenAI API Key 开始体验！
""")

api_key = st.text_input("🔑 请输入你的 OpenAI API Key", type="password")
client = None
if api_key:
    client = OpenAI(api_key=api_key)

uploaded_file = st.file_uploader("📄 上传 PRD/TD 文档", type=["pdf", "docx", "txt"])
document_text = ""
if uploaded_file:
    document_text = extract_text_from_file(uploaded_file)
    st.success(f"✅ 已上传文件：{uploaded_file.name}")

prompts = load_prompts()
prompt_options = {v["name"]: k for k, v in prompts.items()}
selected_prompt_name = st.selectbox("🎯 选择分析任务", list(prompt_options.keys()))

if selected_prompt_name:
    key = prompt_options[selected_prompt_name]
    st.subheader("🔍 分析任务说明")
    st.write(prompts[key]["description"])

    full_prompt = prompts[key]["prompt"]

    if uploaded_file and document_text and client:
        if st.button("🚀 执行分析"):
            with st.spinner("模型正在努力分析中...请稍候..."):
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are an expert product analyst."},
                        {"role": "user", "content": full_prompt + "\n\n" + document_text}
                    ],
                    temperature=0.3
                )
                result = response.choices[0].message.content
                st.subheader("📘 分析结果")
                st.markdown(result, unsafe_allow_html=False)
    else:
        st.info("请确保已上传文档并填写了 API Key。")
