import streamlit as st
from agents.agent_analytical import AnalyticalAgent
from agents.agent_concise import ConciseAgent
from agents.agent_detailed import DetailedAgent
from judge.judge_agent import JudgeAgent

# Page config
st.set_page_config(page_title="LLM Council", page_icon="🧠")

# Title
st.title("🧠 LLM Council")
st.caption("Multi-Agent AI System with Judge Evaluation")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input (chat style)
question = st.chat_input("Ask your question...")

if question:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    # Initialize agents
    agent1 = AnalyticalAgent()
    agent2 = ConciseAgent()
    agent3 = DetailedAgent()
    judge = JudgeAgent()

    # Generate responses
    with st.spinner("Agents are thinking... 🤖"):
        res1 = agent1.answer(question)
        res2 = agent2.answer(question)
        res3 = agent3.answer(question)

        final = judge.evaluate(question, [res1, res2, res3])

    # Show final answer
    with st.chat_message("assistant"):
        st.subheader("🏆 Final Answer")
        st.write(final)

        # Optional: show agent responses
        with st.expander("🧠 See how agents responded"):
            st.markdown("**Analytical Agent**")
            st.write(res1)

            st.markdown("**Concise Agent**")
            st.write(res2)

            st.markdown("**Detailed Agent**")
            st.write(res3)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": final})