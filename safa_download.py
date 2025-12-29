from requests import request, Response

import modelscope
def main_entrance():
    response: Response = request(
        method='get',
        url='https://pre.modelscope.cn/models/autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime/resolve/master/workflow.json',
        headers={
            'user-agent': '',
            'referer': '',
            'range': 'bytes=5-7',
            'Cookie': 'cna=I0pdIfdOgXQBASQBsYBnCEoZ; _ga=GA1.1.1784091972.1762761435; _gcl_au=1.1.153697319.1762761435; t=f224389f4fd7dbebf58b899835d9044c; _c_WBKFRo=ZZUFV5aG5SRoh2x3mlVWj3h6B6rFr6VL7zY6gkIT; m_session_id=589bf48a-ef3f-4d8f-8512-ca3ee6cfd3fe; h_uid=2215631505627; xlly_s=1; _ga_K9CSTSKFC5=GS2.1.s1763978704$o54$g1$t1763978714$j50$l0$h0; ssxmod_itna=1-Yq0xcD2QitjOG0iLc2DUxWK0IPDKDXDUdqiQGgDYq7=GFKDCx7K7eD8bxrU9mHB=iGbq1YQ7T5D/Q44GzDiLPGhDBeAF9Ye42Idzbm7gGddiD8Gh=zF8u9SkRQjWK44_5091bnfuXIVknOy8k6DYDneeDQKDoxGkDiHKD0KYeD4DxrPD5xDTDWeDGDD374DCItOKD0bA8SEA5IxmiQOADYaKtIbKDYvXDAwLAf8A5_iLDWpwv78K34i8D7KnOmbAD7pXvD=DXgYDEmnI1y=Dvalw34qEvI8KGsI=MhWYPD_CYYB4UouKYOwxjqeADzGe4bDkjw2YwdOIxjPie4DDptlGOYAexh4yDYYygbvwFvpjnPb4hFRoxhQU0DWT8YDOFOOnxNlxxBRPwgD05P/Hd=DN6y4eD; ssxmod_itna2=1-Yq0xcD2QitjOG0iLc2DUxWK0IPDKDXDUdqiQGgDYq7=GFKDCx7K7eD8bxrU9mHB=iGbq1YQ7qeDAD6DxYKzDj4xOk_80wvxzjhDDsT_3a9HkbsPcIQ0H__FI50qCddfjxz=BKrnkel3c7pg9C97q7_p94DUv12=Hdcou8vcFHY3YwbE9hx8yhl2vN7IFvobKwlOYEyEOWH7GL9ekAt3dAvKvvT_AfWIdL22y7B=yIVtI0DkC828q06c_ALavnEPvaeq9OPzYuDgP8XZadrL5f67ad9WB8ETy2hqE=e7kmU62CReLBmOy8Ndbb8rd0=PCDq01i_NlizDM1O87rODTiO_Sdc8qS3rx2hb_CyBa9uYr23lSP623ubzcTamT=TQ=kizNMO0oChWsBoburaMCd=8pAoTFT3QAHErKGb_A8qQPNMGNFkpYDxfuI4wzeftL8drTwHOrax7SrvkdIjwWWpL9EQPnmL2NTnbB2QrEG64X=ua6b3f3tcEz6_mWnFhomyCHBgQ/WFn3A28H2rNFqaPjC94bsevoffd8HI8THGua/4GiKe7dYEfoa3H0qxKfK=mkGDFxx5YUlh_uE9yKcvcDgMaj9fWiyHOBHGcHi9ZODlAmkA=YDci=Wiy3k7Sya7/1DkiNe0qPnDaDtdfBGX=eDxbhDV2ZNVcHEZZos9YZ7v/xoWz0oGiYYGvFTAqlGNnz8eUcCx7qtDK0TYqxADD; isg=BDIyEC2qj2mhFrKncF7W4_N6g34UwzZdLlIgQ_wAQeXQj8uJ5Fdwb32tfysz_671; tfstk=goYoPJmY1tw65Qz7qXbSqffU0rix8a_B8pUdpwBE0tWfp6hWTevHCdbLyY_JTyXDdMBywaC3-KOCUb1Rpp2eBdcCUga8-HXvrghWybT0ld9uJgSFaIuVHHJhAb6dL9vpT3hxWVdWNw_eKA3tWF0-zH9haMzygX5Oa_lA4FMYZh7EBA3YDSSSewRJ8uol0IWft6yU4p7431BVTu7eLtSV_1eP8wJEii5Os9zUz6R4g_BVLw7eLIlc9t5P8wJegjfI6NEPBe-wuvMVXrVJeVNVNgXwat4MGEfrW631_yzeo_AcQQr_8y8cZgYqHB2gnw-ywKj9qA4lWQ-6d1JzUYfDrCYHbKuYrwA2beb2uxPAUhOD-aLr9472rLYPmpP3mg-6ehSDkY4fQnRD9ixjOuBpf6JCfeH_PTRe1FtOS2VhihAVoguQ0lujQy1q9ErQAg5fiOFWH-jMxLvQRjc0XBsPG16tijqBmg5faVhmil3l4s11B'
        }
    )

    if response.status_code != 200:
        print(response.text)
        return

    print(response.text)

    pass


# def test():
#     pass


if __name__ == '__main__':
    main_entrance()
    # test()
    pass

