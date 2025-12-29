import requests
from json import loads

url="https://pre.modelscope.cn/models/autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime/resolve/master/Qwen-Image-Edit-2509-Photo-to-Anime_000001000.safetensors"
params={
    "Cookie":"cna=I0pdIfdOgXQBASQBsYBnCEoZ; _ga=GA1.1.1784091972.1762761435; _gcl_au=1.1.153697319.1762761435; t=f224389f4fd7dbebf58b899835d9044c; _c_WBKFRo=ZZUFV5aG5SRoh2x3mlVWj3h6B6rFr6VL7zY6gkIT; m_session_id=589bf48a-ef3f-4d8f-8512-ca3ee6cfd3fe; h_uid=2215631505627; xlly_s=1; _ga_K9CSTSKFC5=GS2.1.s1763978704$o54$g1$t1763978714$j50$l0$h0; isg=BIqKFjVy1-EG1Fq_GBY-e2uy23Ysew7VRmqIuxTKMF1oxz2B_A-i50t11zMbN4Zt; tfstk=gzIEP4_Ex3f6-WG_A1Kr3VYkIjtdn3PbZgOWETXkdBAHVUiP711OVw1WOQ5Pes8lATth4_5Ag3iBxynkE1XARwaJxhGlG1Thp9aKa0R10g6BN9YijLpe-QIPe0JlE_epNJU1p9KJqSNf4o6dp5TebDIy-FcM3O0orD46jxQnMXFbco63-pK5IS_QaVVDULxkKUmujRJWH2xkrpXgQLvSt4mhZO2w6Lgn-3AosVvJKvxkq_XgQLdMK3YhZO2weCAo6V5l9cRw-RiwWtP7-zU2G9AZq0j32eRqCdp9tGJe8IYM_0vCbp8ei9j2lM1HUZj2JsVsRBbVPsJfOlmFg9fFoEjns5-RCZ5y3M2muQ5dIMTGx8gvB3QhoHjzgXXMuGjBvNPqcIbOEg8GpSuvCaXfAa5Q60ACuOfwlGGschjFTMYwmgyjwdVQQgQEZ48HBdRbQRPFGUMNnTcJc43J7PpwG-exy4Lh0dRbKe0-yF8eQIwYH; ssxmod_itna=1-Yq0xcD2QitjOG0iLc2DUxWK0IPDKDXDUdqiQGgDYq7=GFKDCx7K7eD8bxrU9mHB=iGbqidmhi5D/i7DeDZDGFdDqx0oi6jrYe_=HlmY2RxHFGCGh=zF8u9SkRQjlYh2q7Mto8cBHXV=1o6KHdD4D=xxDwxibDBKDnpxDjx4xGDiiax0rD0eDPxDYDGRpDDHEbIxDjD8I1KfhOlYeb43DbprwEmxDRcdDSnSEE4fhY03DacBopIr_DmKDIZCKED3DFcMoNq0k=4i3oEoyCq0OeM7_0QfEAI2yGQG=SOqYhWDYRhD1dBIQkWNkQG1GDP0wSai47w1iKO7omnP17NiDDAnh5GYb424yDYKvgiHwWHpfnPenorGGDhQU0DWT8YiO_HVnxNl2Ff0Plr5=DPD7d=0DIYqeD; ssxmod_itna2=1-Yq0xcD2QitjOG0iLc2DUxWK0IPDKDXDUdqiQGgDYq7=GFKDCx7K7eD8bxrU9mHB=iGbqidmhDeDA3_ex4NzDj_Nkr62AvQqDBMaWeTZna9yEqS4Il2Uav7PryPToeUMpAqUdMCdqsad9deYc=qec4Yj2FtrFdZYaFkow5RO0zrOiP1QI5K3wQklp5HYqxbKP1Y7G=APadGOqH6iHdaZOHh/fWo0ILS6iHqWcLExvU=fGajSA=RoCAee6mYn7EKUr4HjpWboQsGoczxqIHxh9DbcvOwrk8RQFw/PM9r6MycNpjGNcMX_V8CTWXdG_d1Ex7xCzKC30OhT_zhTQdWxx8sWAhVwaGOwHDtHBtnhWdS4KbNCgYebNXLWnrzvO5Rr1NnbURNNjWUf7A2GQ03kir6idU8xhRKDpFHS3wCAThamOaRra28OYGDg8qn25xuqmM49fsQ77QR3Zki/R3RRNkCxR_tb2AwhCokzXSfQe=/2rAP_sxU/dCKM4oWF10aD8v6d=l2KyEF3kr/2i065K/2oRi6it_qdvp2kOD/73FrQALQLOFBwxxL38tiHLtMY3SxtWldPP7txQbInETt0cGhk2gl64XPy2KZLLLdAUf3zIgzxg6Rsvzs3pGoNvFgQtewxsS0_MBLxl6DXksybzy6vsS=kgx/msG08z0KSiyqDQkB4RE5dfkGbWGamr7h=d_UPGqAj2PNxOoP4KOQYWDq4dT_jgxrBdc=yGD8as2xCzSFRGah4c73=AxjxpmT7kWiY_ofAj2_mnVZPgrAlTyho/bkn=3GMyhe4GiYimGi7EqlGNYheDEiWqgT48KgDQm4D",
    "Range":"bytes=8-234216"
}
response=requests.get(url=url,headers=params,stream=True)
print(response.status_code)
chunk = next(response.iter_content(chunk_size=512))
print(chunk.hex(' ', 1),"\n",chunk)

if isinstance(chunk, bytes):
    print(chunk.decode())
    # target: dict = loads(chunk.decode())
    # print(target)
    pass

with open('example.txt','w') as file:
    file.write('abc')



