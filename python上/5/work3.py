import re
from collections import Counter

# 读取政府工作报告
def read_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# 统计关键词频率和句子
def count_keywords(text, keywords):
    keyword_set = set(keywords)  # 使用集合提高查找速度
    word_count = Counter()
    sentences = re.split(r'[。；]', text)  # 按句子分隔符分割文本

    # 遍历每个句子
    extracted_sentences = []
    for sentence in sentences:
        # 检查当前句子是否包含关键词
        found_keywords = [word for word in keyword_set if word in sentence]
        for word in found_keywords:
            word_count[word] += 1
        if found_keywords:  # 如果找到关键词，保存句子
            extracted_sentences.append(sentence.strip())

    return word_count, extracted_sentences

# 将句子写入新文件
def write_sentences(sentences, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for sentence in sentences:
            f.write(sentence + '\n')

# 主函数
def main():
    report_file = 'report.txt'
    output_file = 'extracted_sentences.txt'
    keywords = ['就业', '消费', '减税降费', '住房', '教育', '生态']

    # 读取报告内容
    report_text = read_report(report_file)

    # 统计关键词频率和句子
    keyword_counts, sentences = count_keywords(report_text, keywords)

    # 输出词频
    print("关键词频率统计：")
    for word, count in keyword_counts.items():
        print(f"{word}: {count}")

    # 写入包含关键词的句子
    write_sentences(sentences, output_file)
    print(f"包含关键词的句子已保存到 {output_file}")

if __name__ == '__main__':
    main()
