from openai import OpenAI

client = OpenAI(
    base_url='http://1942976517990068.cn-hangzhou.pai-eas.aliyuncs.com/api/predict/ms_eas_a39aaa47_df67_489c_834d_18d7/v1',
    api_key='ZjRmMDg3ZWI3YTM5ZjRmOGNmOTg4MThhY2M3MjUzODU5MTk2ODFiZA==', # ModelScope Token
)

response = client.embeddings.create(
    model='Qwen/Qwen3-Embedding-8B', # ModelScope Model-Id, required
    input='你好',
    encoding_format="float"
)

print(response)