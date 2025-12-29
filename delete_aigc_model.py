import requests


headers={
    "Cookie":"csrf_session=MTc2MTUzMDI4OXxEWDhFQVFMX2dBQUJFQUVRQUFBeV80QUFBUVp6ZEhKcGJtY01DZ0FJWTNOeVpsTmhiSFFHYzNSeWFXNW5EQklBRUc1SU1IRTFkbUpTUjNsU2RXMUNOREU9fJr2jaxtfcZ6b2ooUikPuqvvDB-K-7AOrwf3r-M0X02C; csrf_token=JWNTbNAVB1MfrqahuWjbMcTcgt8%3D; cna=I0pdIfdOgXQBASQBsYBnCEoZ; _ga=GA1.1.1784091972.1762761435; _gcl_au=1.1.153697319.1762761435; t=f224389f4fd7dbebf58b899835d9044c; _c_WBKFRo=ZZUFV5aG5SRoh2x3mlVWj3h6B6rFr6VL7zY6gkIT; xlly_s=1; csg=3d4453e9; m_session_id=589bf48a-ef3f-4d8f-8512-ca3ee6cfd3fe; h_uid=2215631505627; acw_tc=0b62601a17637208462797814e75e465e6970345b6ddcef405e1268d0323cf; _ga_K9CSTSKFC5=GS2.1.s1763721991$o50$g1$t1763721995$j56$l0$h0; ssxmod_itna=1-WqAx9GGQoeqxh2DgYxBQfDuD0BD_xBP01DpgxQ5DODLxnb4GdDuDMm4RDCwhCtwjmeKloqHN4BD05wxGDA5Dn8x7YDtxfPh3k0=CuDIQFIYveKGbQ00IpeY0I2S3wyYoOS9HULKUk9EHkoOmh64xODUDAE5D7QDb4DyDGtbDG=ifDeD4f3Dt4DIDAYDDxDWneDBi6bbDGprgeWbTmeosARrxi3bGQPbDitGxi57apcrTmhHxA3YNxab7eGnRi8bbOWDj4BTmKGyGeGWbfTXZKGuttbKh2nWHpm0rwGMi_LeRCDxOA4ozTKqGe4nDs0DReiC0N4AqRYwQ1KmCKUDDA0r5bYtbDYFAxDrgivSGeM0eInHhb_hShi/_xfiO9Yh02tWgemGx_qHKDP47tbwKXveeD; ssxmod_itna2=1-WqAx9GGQoeqxh2DgYxBQfDuD0BD_xBP01DpgxQ5DODLxnb4GdDuDMm4RDCwhCtwjmeKloqHN4GDDPYGQMD7PKQbljRKqQ9eeDsgz3goh=k=lmfQOkylC6nCkkg6P7OqGdk1dlh5y_hgv0kdKK0dOYY02eSNKfY0nYivDdwGe94N5TGU2ABoV033hjlpdllj/mE_RzO=4bLp4Q=QM_dfeaw6ASO0VA_D4KQyxmDyVelPkphxBiCGkcd3ePeQs6dhlCWi4ZjjqyRrmPMRCcKrAc9Lcikdf8TaBAR7qGkffmoQGZwf3RzWeTi8gud83iek=L2DZhrx3sdBoWRsdlHygzfkWelQX4QbghdMGro5DMwOx7Vr1znTV2Dgumag=wW4EgwY7Qdj4duOyTiAoQlOiEMFV3px8OeSN6iQBkie0O0_tdTYgod6Rtx2T5ShgqrWpzG2dr4zMMOo0dcTKwbOIxraStphjx8WOOsWSaaDQqAkjnxN3QdktWgCZoIEn7ARCOuXDFv3RTGO_lnNg72Xr4IM8N251rtCQajwCRQHMY7fkQtSmdpCclwq0bseYnMzgnXkLQP_OodUyuH8=HU_zIu7u9cwfQ6bmg8xDuHNEDHb81w7TgNbD_q36/DUkr4gjkEr52IbdkYrwAjuO/S=cb8kD5WB3gD5LxXtddkC7clNuN38xuudd7zqFdfoD6et35400DQUEdE=CDvEiAXDCqjwZY5fDEraSNjDXKwZ0DR0SuQ0w_8=fGC7Gz0dYS/qTePOU37iFw6k=RhuB42XX7DArfY5KDi7qWKqGjQYIS=m_Kr=feVT4Kw=Gj3E6T=nxAjIbGSi=WI_b33_EB5ZbHhZnxzAKvDfwxbYXmZ0diAD/rxD; tfstk=grHIbysoo4HNRNcYO8-NGhOknd2WgvOw3GsSmmUPL_eK5YgtkXyz8e0S2qzZL7yptL_SyPVU8UxHVloSPDPrT075xAgfU98Ht0B7U8L2uKJqxM2ueEublkmltkrbyLWLwJ297qVRfKJqxDIUvno93Xo_SRqzy8FLwdeTSu7Lv4FRBcUgquQL29KsXP4OpTULvcnTDuW8v4eJfcUg28EKyWKsXPq8ezhTRNZyOunBmq_MHnOy9IUNeTH_A5dZbPezg3y7OrnLWBxICOVQkDU1eednZXaTcALl8zDsXvEoWdWQFcESlJh6W9gSvj0uD2p1JkGKcmPsEEB7jf33_kG621UKDyeL5YxlEyhE2YPSpEIzJv0ECSDlRFzrgckL1qLNC4VS9jeKFE9O4cB4ly-5NGNcFla2fh1lZf8UmZExuiHY9lqp3ht15_VLjlZMfh147WEgvSK6fN1l.; isg=BOfmNDg6Qt5GfMek9aGrEH5ddh2xbLtOU9U1ALleQXarqD9qxz_9nm3myqg2QJPG"

}

response_list=requests.get(url="https://pre.modelscope.cn/api/v1/muse/train/list?pageNumber=1&pageSize=30",headers=headers)
print(response_list.text)
for i in range(0,1,1):
    # if response_list.json()['Data']['data']['records'][i]['trainStatus']=='CANCELED' or response_list.json()['Data']['data']['records'][i]['trainStatus']=='FAILED' or response_list.json()['Data']['data']['records'][i]['trainStatus']=='TIMEOUT':

        TaskId=response_list.json()['Data']['data']['records'][i]['id']
        name=response_list.json()['Data']['data']['records'][i]['taskName']
        stau=response_list.json()['Data']['data']['records'][i]['trainStatus']
        url = "https://pre.modelscope.cn/api/v1/muse/train/delete?taskId={taskId}".format(taskId=TaskId)
        response = requests.delete(url=url, headers=headers)
        print(TaskId,name,stau,response.text)



