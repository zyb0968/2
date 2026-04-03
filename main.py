title = input("请输入论文标题: ")
summary = input("请输入论文摘要: ")

note = f"""# 文献阅读笔记

## 标题
{title}

## 摘要
{summary}

## 研究问题


## 核心方法


## 主要结果


## 优点


## 不足


## 和我的课题关系


## 我的疑问
"""

with open("paper_note.md", "w", encoding="utf-8") as f:
    f.write(note)

print("已生成 paper_note.md")
