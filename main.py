from agents.agent_analytical import AnalyticalAgent
from agents.agent_concise import ConciseAgent
from agents.agent_detailed import DetailedAgent
from judge.judge_agent import JudgeAgent

def run_council(question):
    agent1 = AnalyticalAgent()
    agent2 = ConciseAgent()
    agent3 = DetailedAgent()
    judge = JudgeAgent()

    res1 = agent1.answer(question)
    res2 = agent2.answer(question)
    res3 = agent3.answer(question)

    final = judge.evaluate(question, [res1, res2, res3])
    return final


if __name__ == "__main__":
    question = input("Ask a question: ")
    answer = run_council(question)
    print("\nFinal Answer:\n", answer)