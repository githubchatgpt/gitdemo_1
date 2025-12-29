import requests

url = "https://pre-1.modelscope.cn/api/v1/muse/predict/task/quickSubmit"
headers = {
    "Content-Type": "application/json",
    "Cookie": "cna=I0pdIfdOgXQBASQBsYBnCEoZ; _ga=GA1.1.1784091972.1762761435; _gcl_au=1.1.153697319.1762761435; csrf_session=MTc2Mjc2MTQzOHxEWDhFQVFMX2dBQUJFQUVRQUFBeV80QUFBUVp6ZEhKcGJtY01DZ0FJWTNOeVpsTmhiSFFHYzNSeWFXNW5EQklBRURCSGNtUnhiMnRKYzJwdFprVkpRbVU9fEIKhUpoJq7HoHEBZk6aUfIB3vW-DfqLZG-5h_LX2cIu; csrf_token=5nNMLi2l82ZqvSpitka1R_sciw8%3D; _samesite_flag_=true; cookie2=1f4b6af046e72a25333593e4d5e643f2; t=f224389f4fd7dbebf58b899835d9044c; _tb_token_=3bbed56dee7b4; xlly_s=1; modelscope_pre_version=9.9.9; csg=d918613b; m_session_id=1b81a719-fb8b-4050-81a0-6642a726ddde; h_uid=2215631505627; acw_tc=0b62601617635224877348033e677dea0537b817ce8adb99648d7f34fbd807; _ga_K9CSTSKFC5=GS2.1.s1763516505$o34$g1$t1763522774$j56$l0$h0; tfstk=gGsEYi_Ex3f_7Kc_A1Kr3xzFo4-dV3PXqgOWETXkdBAHVUiP711OVw1WOQ5Pes8lATtH4u5cwBYBA7nzUZB7p965RalyvG_IVBNp4TfX4SNbco6dpHKuGS6-F0kvvLon-ec7jcvy4pAUW7pRp3Ku1qg45IXdOFlkGexuQhvyLQxkrLcgQLJ2Z3AHrf0MnCAkq_AkICvpUpvHK22NICpkqQfk-R-M6LxkZ_xo1kfl9cRw-RGWj6tgYmtpi9AZqmkvLe4dE4iijGJe8tfe_d91bp8eiUDLSJSVn9jvUgemzQW5-69OaoPwjM5FxF-z4cKC3Nfe7wPrbFQGHgYNWSuAH9fFoEj3bRfPstQvxMV-ABQlIgA1x8iyiZ6vbdI76DAPSajBJ3h3TdSF3g7P49hJIWwN2wlozev9QIwaQW5XPAWcEbKjy4LaWdRbH-3-yefvQIwH-43J7JvwG-eA.; isg=BIyMGpRkCcLaqRx1yhgQkXnkXey-xTBvdPxO8eZJpzfIcSB7DtBH_DqHEXnJDWjH; ssxmod_itna=1-Yq0xcD2QitjOG0iLc2DUxWK0IPDKDXDUdqiQGgDYq7=GFKDCx7K7eD8bxrU9m=KK7wDxNR9DbFq1DBqhxiDnqD86DQeDvDcb7YekUBor_IqUjDxAxK9BEE=k6X6iKgP9Ftn=lpfOLX1s2OwTdcFYKe4D=xxDwxibDBKDnpxDjx4xGDiiHx0rD0eDPxDYDG_IDD5faIxDjQ3vGb8_OYoeat3DbpxmEmxDRxQDSDLfjt8_Yl3DaxgoAIxwDmKDIo1KEQ3DFxlobq0ki4i3dcgysq0O55ow078fLIhBE1HiGebxG7iTRGDx9am=7qi7wxjqeADzQiebGx1hRYwQhKOAwMx4DDptlD8iAP5nrQHSF5m85Inx1QWT3ebzYkFqxQqYShtBhND4r9Bqc5PeBqVhPOGDD; ssxmod_itna2=1-Yq0xcD2QitjOG0iLc2DUxWK0IPDKDXDUdqiQGgDYq7=GFKDCx7K7eD8bxrU9m=KK7wDxNR9DbFqiDG4m63SDSx03dm=7fQNzYYuKD/A942n=e4Npf6dAEUOuy2Tk6O34sY_L7zhjGsaHdKYws2Z0C1ppQ269C9WvQd9_Qe05ar_KhzhKONhIC5AyW7hg7mcRP3fy4laOEYeAxU/ytu15mbzyCki9LKBA=PzTXIOyDkZcDm=DmGZMdO=GAH49wu1rp9AlH0bBd3Np=d_G73WgxbTPa0R91Wxehx=mhEzrXgoBgxXgddVLN62tdYNfLi6iCTrFKl4E4xcSaMO4EbKjObaRDMdHEohbkNX7sKBda8bMqQzuYP_aT8_GgKlrTwTQQYCjxd60awurPbQOlTmOq6uFOomPlrCwimTac_a7S7KLiHji=ji7gbbwiH3maaak1To6H6edmb8xw7oM1Z8CcghbqYwRja4bvEbfoNNLm_er3cIUCTNMsd3ii3mv36s2kGldy=8soiTCrxMGP423aAzpNCPuHK8k_X4Tu0EGq3GFxQ_OF/mWIzt83miTiQUCqaWT89XIiN0vuUGRDsv_WhFA7lT72KziykY1kndGADyB49i5LqYPVq9gKdGkmrxUZoWhDOVLq0daOxi8G6kMwN7WAtGvkTyEd0B92q7iMKT/nVq5I3uyaovsCxhySBqE4PeQl0lhsyxKWzoYClaBralqH5xnbkyeUDaBP7DGDYe4hYYnqSDNBqDxrBxM0DD_6A4AqYDY3DD"

}
data = {
    "predictType": "TXT_2_IMG",
    "description": "4567",
    "imageInputFrontArgsList": [],
    "quickDiffusionArgs": {
        "imageRatio": "1:1",
        "numImagesPerPrompt": 1
    },
    "styleType": "QWEN_IMAGE",
    "addWaterMark": False
}

response = requests.post(url, json=data, headers=headers)
print(response.text)

res_quota=requests.get(url="https://pre.modelscope.cn/api/v1/muse/predict/queryAIGCTicketAndQuotaNum",headers=headers)
quota=res_quota.json()['Data']['data']['quotaRemaining']
print(quota)