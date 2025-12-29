import requests
from concurrent.futures import ThreadPoolExecutor


url = "https://pre.modelscope.ai/api/v1/muse/predict/task/quickSubmit"
headers = {
    "Content-Type": "application/json",
    "Cookie":"cna=KRubIQdBGBICAQAAAADVgJcT; _ga=GA1.1.5769076.1762929961; _gcl_au=1.1.1346739235.1762929961; csrf_session=MTc2MjkyOTk2NHxEWDhFQVFMX2dBQUJFQUVRQUFBeV80QUFBUVp6ZEhKcGJtY01DZ0FJWTNOeVpsTmhiSFFHYzNSeWFXNW5EQklBRUhwVWVVRTRSMmhsVkcxMlFXZGpNSFE9fJ2k-ONiJ7xHCOwkBffFhRj8iWaMatAg1YPX-r4QqqKm; csrf_token=FAQKrSIBn3-5wV2Q4o6xtIze-h0%3D; xlly_s=1; modelscope_pre_version=9.9.1; m_session_id=e3f15bb9-5e71-4f4b-b63a-487a43cb3403; h_uid=27456655466496; acw_tc=0bc1a14217645732737508382e7cb39b0dfda08ad44039bd37ed1e39bd3bb9; _ga_K9CSTSKFC5=GS2.1.s1764565736$o8$g1$t1764574488$j29$l0$h0; ssxmod_itna=1-QqjxBDyDcDnQiQDOWG0zGCAY4GQDQeeDp=DBP01_D_xQ5508D6exBRDZqqHguKw44KVi7GG5zxgxGX533xiNDAPq0iDCfWQKKt/GD4N38/GOeeHzW8_rI4ZnUHgdQ74E1rpLsvw2kZ0aiEytRoD8_4DKqGmD0=DATeD7Leq3xGGj4GwDGoD34DiDDPdxDtbwWeD7gTQgen4P2r3_lTDmbeKgieDmwHDnhaTrZu4s7aDf_rFYaeexY=DQuOrBBTDj_HFCKGy7eGWW3u6yKGuKUreErnbNaeXawUY7Amw_ARDsD4qIuw4IvhYnw5Yxs0w57DKnquQG3pIUiXbDDABh5buDaurbYx3hB3yg7WSAepYGG3oOtRDiieQ_4t0OeONY0ieRP3ieYnPUGQaE4_Dew0PeD; ssxmod_itna2=1-QqjxBDyDcDnQiQDOWG0zGCAY4GQDQeeDp=DBP01_D_xQ5508D6exBRDZqqHguKw44KVi7GG5zxdxDfbrtSB4GaKW7f5fYD0yQProec2FKN_/0uWPkwYc0WKkuP=Rnx0rW9=CRm5ltFMuA3LuYwx60DNxXGhAIOUxQYL5tAr4Bd_jIA67UA=YmQ_X_hxESTbi8Q_5LqxR_hXyz0jKpS5iXMaK5B_jK7UCwRDiGkGM77acWALeRkIwdMfIaprOrtypdcNuF9TV7BdPRzdYDTlObjttv4=ZlfgUBTLuz=fPD=cbTd4KwhAE0eHf_tOfr12WuqOvhiNAtmhiMki=4FrmQ3GDrQiRd3xftebt4ddz8t98HiuTco4KwNl_Cq0GAnT6hxzYdbr4qCDxdNv2GXgQ1qtckGZTtlg_2YvZAOo6W1jQKQbvgd4SQN3=zlGBrxNG_=uhTg_zCb8lbxZQQYfkeQt1N9_zxSff1bEZr/WtMW6TddxQNMLry2WQQvYP0Xo4RfrKYv48=qIhPFbYBHbtNgi3YaCUlXqWhq6d27fEoKsz28kzT=1FjbzcqYej9hs4nWVhs2riXRqV3pVTQU_hjqE/z2EuXBKBi32q=4qKcwkzu892OnDyobnAkOTSbn/K8HG530DZG5mhDsLzQ_D53iFSlsOsrYbYUDmoYsElvRd4udMo5ie25ifYqqGHIppL=D4E74eeeuDw4eQ7WN0StUDwAQFmKRAI0Rd3UDQOFYGoDQ/=OOImeRde5wC8q3xNDqlp03ZmeGibtIxgxjYog/82_GKZopo/QqUS39fx2x_P4AhIDkWRQ2o2KOYNeo620o5=GbAD3xKG53xLj53NGiYUG40o72RmD3xPG5eD; tfstk=gdPI2vTumuFNZdexdb7whIA2yRlWON5qeUg8ozdeyXhLyYEqbvoFqwbS2uEi4JzRK_Z_2k9z8DyUV8iTAv73TwxMNlZjzwmzLuwSt5yeaDSnNzEqNiSVgsz3-XcR0i-zFcXrMquJp3o-6chrPMWOfOa3-bYM3E6ZXyfSbS6IybE-6A3Eyb3-pYQs6q3mwBHJ9dKtj4h-wYh8WA3oy0KppYQ_Wc0ow0E-pNGtj4h-2uh-6itsz9g8RZDp1qZvzgzEfQd81VIouyskG2PnR1i4-csAD5OmdmUKfQIQdx3jXqNOqHou1PFKrlCwObatPoGLCGdQVye0qqEd1H3QpraqC7jvNV2TxAuQCaptvrnK9cNlrQmLLzFrFWIvzDF3Y5M0ZHsZ4-za9AZAbCZoFJex97sf6g8ygmiFPLTsnQgs0N_6EL2NYqxYOsJBav3iJs715h9opV01cN_630MKS2I55Nt6E; isg=BCQkgMVEEbr_zGXPwxk-vKKz9SQWvUgnTHTWqT5HPu-y6cKzdM9ptscPqUFxMYB_"
}
data = {
    "predictType": "TXT_2_IMG",
    "description": "456",
    "imageInputFrontArgsList": [],
    "quickDiffusionArgs": {
        "imageRatio": "1:1",
        "numImagesPerPrompt": 1
    },
    "styleType": "QWEN_IMAGE",
    "addWaterMark": False
}


with ThreadPoolExecutor() as executor:
    futures = [executor.submit(requests.post, url, json=data, headers=headers) for _ in range(10)]
    for future in futures:
        print(future.result().text)
