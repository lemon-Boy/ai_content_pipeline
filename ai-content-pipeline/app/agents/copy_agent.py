from app.services.llm_service import chat


class CopyAgent:

    def generate_xiaohongshu(self, insights):

        prompt = f'''
你是小红书百万粉丝博主。

根据以下观点：

{insights}

生成：
1. 爆款标题
2. 正文
3. emoji
4. hashtags

风格：
- 强情绪
- 强观点
- 口语化
- 年轻化
'''

        return chat(prompt)

    def generate_wechat(self, insights):

        prompt = f'''
你是公众号深度作者。

根据以下观点：

{insights}

生成公众号文章：

要求：
- 有逻辑
- 有案例
- 有观点
- 有结论
- 1500 字左右
'''

        return chat(prompt)

    def generate_linkedin(self, insights):

        prompt = f'''
你是 LinkedIn 科技 KOL。

根据以下内容：

{insights}

生成专业风格帖子。

要求：
- 英文
- 专业
- 有洞察
- 适合海外科技圈
'''

        return chat(prompt)