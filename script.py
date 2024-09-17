from transformers import pipeline

summarizer = pipeline("summarization")

long_text = """
OpenAI is an AI research and deployment company. Our mission is to ensure that artificial general intelligence 
(AGI)—highly autonomous systems that outperform humans at most economically valuable work—benefits all of humanity. 
OpenAI will build safe and beneficial AGI or help others achieve this outcome. In addition to our research, 
OpenAI has commercialized and deployed AI technology, collaborating with various industries to implement 
cutting-edge solutions.
"""

summary = summarizer(long_text, max_length=50, min_length=25, do_sample=False)
print(summary[0]['summary_text'])

