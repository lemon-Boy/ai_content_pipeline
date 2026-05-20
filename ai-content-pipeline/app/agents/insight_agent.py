from app.services.llm_service import chat


class InsightAgent:

    def run(self, trend_data):

        prompt = f'''
你是一个行业分析 Agent。

请分析以下内容：

{trend_data}

输出：
1. 热点总结
2. 用户情绪
3. 内容方向
4. 爆款选题
'''

        result = chat(prompt)

        return result