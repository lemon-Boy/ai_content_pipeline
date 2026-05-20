from app.agents.trend_agent import TrendAgent
from app.agents.insight_agent import InsightAgent
from app.agents.copy_agent import CopyAgent


class ContentWorkflow:

    def __init__(self):
        self.trend_agent = TrendAgent()
        self.insight_agent = InsightAgent()
        self.copy_agent = CopyAgent()

    def run(self, keyword="AI"):

        print("\n=== STEP 1: 抓取热点 ===")

        trends = self.trend_agent.run(keyword)

        print(trends)

        print("\n=== STEP 2: 提炼观点 ===")

        insights = self.insight_agent.run(trends)

        print(insights)

        print("\n=== STEP 3: 生成小红书 ===")

        xhs = self.copy_agent.generate_xiaohongshu(insights)

        print("\n=== STEP 4: 生成公众号 ===")

        wechat = self.copy_agent.generate_wechat(insights)

        print("\n=== STEP 5: 生成 LinkedIn ===")

        linkedin = self.copy_agent.generate_linkedin(insights)

        return {
            "insights": insights,
            "xiaohongshu": xhs,
            "wechat": wechat,
            "linkedin": linkedin
        }