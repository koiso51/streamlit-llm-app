# from langchain.chat_models import ChatOpenAI
# import streamlit as st

# from dotenv import load_dotenv
# load_dotenv()
# # from langchain.chat_models import ChatOpenAI
# # llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
# from openai import OpenAI
# llm = ChatOpenAI(
#     model_name="gpt-4o-mini",
#     temperature=0.5
# )

# 各種ライブラリの読み込み
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数の読み込み
load_dotenv()

# モデルのオブジェクトを用意(ChatOpenAI)
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

st.title("サンプルアプリ: 専門家アドバイザーアプリ")

st.write("##### 質問に対する適切な専門家からのアドバイス")
st.write("質問したい領域と相談内容を入力することで、適切な専門家からのアドバイスを受けることができます。")

selected_item = st.radio(
    "領域を選択してください。",
    ["健康に関するアドバイス", "仕事に関するアドバイス"]
)


# ChatOpenAIを使用するので不要
# # OpenAIクライアントの初期化
# client = OpenAI()

st.divider()
if selected_item == "健康に関するアドバイス":
    input_message = st.text_input(label="相談内容を入力してください。")
    text_count = len(input_message)

if selected_item == "仕事に関するアドバイス":
    input_message = st.text_input(label="相談内容を入力してください。")
    text_count = len(input_message)

if st.button("実行"):
    st.divider()

    if selected_item == "健康に関するアドバイス":
        # first_completion = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {
        #             "role": "system",
        #             "content": "あなたは優秀な医者です。"
        #         },
        #         {
        #             "role": "user",
        #             "content": input_message
        #         }
        #     ],
        #     temperature=0.5
        # )

        system_message = "あなたは優秀な医者です。"

        # メッセージリストの用意
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=input_message)
        ]
        # LLMからの回答取得
        response = llm(messages)

        st.write("### 回答")
        st.write(response.content)


    if selected_item == "仕事に関するアドバイス":
        # first_completion = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {
        #             "role": "system",
        #             "content": "あなたは優秀なキャリアコンサルタントです。"
        #         },
        #         {
        #             "role": "user",
        #             "content": input_message
        #         }
        #     ],
        #     temperature=0.5
        # )
        system_message = "あなたは優秀なキャリアコンサルタントです。"

        # メッセージリストの用意
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=input_message)
        ]
        # LLMからの回答取得
        response = llm(messages)

        st.write("### 回答")
        st.write(response.content)