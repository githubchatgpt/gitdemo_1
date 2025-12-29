import requests
import json
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# ================== 可配置区域（你可以修改这些）==================

# 🌐 接口地址
API_URL = "https://pre-1.modelscope.cn/api/v1/console/message/task/send"

# 📧 接收者列表（可多个）
RECEIVERS = "maastest0018,Thailand01"  # 替换为你想发给的用户 ID 列表

# 🔐 Cookie（从浏览器获取，保持登录态）
COOKIE = ("cna=dgZ+IejFnCEBASQBsYDnhSHO; _ga=GA1.1.856294341.1761024119; _gcl_au=1.1.498138405.1761024119; t=100a692957fa887b56539d7a257a2390; csrf_session=MTc2MTUzMjU2OXxEWDhFQVFMX2dBQUJFQUVRQUFBeV80QUFBUVp6ZEhKcGJtY01DZ0FJWTNOeVpsTmhiSFFHYzNSeWFXNW5EQklBRUcxR1VFTjBaVE5FWVdneWEwcG5lbWs9fE4PFMg_x9RWSD3SJ_iAQHPdWGXL9zICB1hiJR4vgLlz; csrf_token=hKGsCALtwPNOy3VGbmySNkbRSr0%3D; _c_WBKFRo=UAHZUgmFBeUpFqBJw9XhjUjHLjic3nieQuaK2fvA; xlly_s=1; _samesite_flag_=true; cookie2=119dabc03debf4e51ec20d462c92fa13; _tb_token_=f73e3f681b6e3; csg=50e7a41f; m_session_id=1644ba3a-ebca-4a39-bd00-223588e16ae9; h_uid=2214908846141; _ga_K9CSTSKFC5=GS2.1.s1762325475$o36$g1$t1762327289$j59$l0$h0; tfstk=gOmihQYdFW1S-MS1SKq6SqnJhHTK5lZbgjIYMoF28WPQM-psQkun9XixWjFTijDjZrotHlWmiXhoir9_MSPmMxu9p3K-CAZb0jAJ23L66gcjo-yN0KyUUo2a1gr1ZAZb0BQRreFrCfE9v4E40pqUnR2a0-l4YJy0TGyVb-5eK-NU0-PV79rUh82a3GlqLp20TSr47jzeK-NUgorq6f_awmurYIi10PBYqLnbIPVrQ5ktQDJ8RNMbt0mj2RmgaA7f0io3IPme2TgioouZBX4-SQjg2AuSG8lN_C2njYmmzX-djoDEzmqEYBWL_4MnmlnwHhrEjfma-jWc-PuS64znvCjQa2knHy0BhNFxP-lbPmd5f5kqF0g8qnX0K4DUxg5d8a-BaiweHD7flPyQK7EUC3OXAabWWpvhyxaad8NJKpbXMPyQQ3pHKad47Jw7w; isg=BDw8Re7_ecXpL0xk3tUqIQGsDdzuNeBf0-7Acxa-RycK4ddrPESy750XwQmZnRi3; ssxmod_itna=1-iqGx9DgDuiwSG0D2GGDOWDCDcDYqYF5iODzxCvB50C1DLxn_PGd3Rbq1mbDy7GO6ubIhOKiRRIQSD0vm=mDA5Dnzx7YDtrScGQenO75h=tpneY4o5y7GiuxPF_CwpI39jOOIRyGwm6M/FL=ojqhp8ud4oxGIGDG2DYoDCqDSexD9YroD4S3Dt4DIDAYDDxDW9eDBbZbrDGPbMQnbHWe3hBbbxi3rmCeDmTmsxiv7H6abHW47xA3oaoarCeGnD0jEPEqbx03haO8DzTbDbOoNx5CDtqgo1WITaparKVAx_uYXe_elYW_QiAD30DKODFG5bi4DOG5xxMix/kQ=i5m0YE2dDD31iGnGi3bro7DbCtc2togt=EoqCAaFKXAGG0Icmh1GGNfwzlw1Q5qjIvjxeGGxKmgi_lhDxD; ssxmod_itna2=1-iqGx9DgDuiwSG0D2GGDOWDCDcDYqYF5iODzxCvB50C1DLxn_PGd3Rbq1mbDy7GO6ubIhOKiRRIQmDDpU1YCRD03/mYc4iqMmDGX7Km/b2KENl_0SL6p5Bc4xehpiirOPzvT/cIS3UVb4onuD0QMPqKYj4ju6ew24KxW2YLMpe=n2BQjR1m8DeB_DgjRQrNQbLe1DqRYWEe1q4CpnVba3oRBtrPcikZqXHdkqHa6ao63F_Zn7LY17ro6=AXSyEd=Bs61AhpQro7Ad23w9um8qRxe8=cZ9k=LUdXLOKycCOwqbu92MtuKyRF5HAGARiV8u=fq4Un0RiCYWOjDH0RaBcsGW//TC_IHSWPxI5LyI4qKxImUIAYmepuatvexwB/cWBcxu5eZb1j_xmPGR0alntsq98TQlFmjD7lYGCnKPvoVT1QDto0K_BCSq5QHUlRi4wtpRiK8GbuD_yObuq7uOCn_/czzEP3L7SOQBpxCwzjDE45PIn=DaYaDAz2C1IH_cYdniy2Caih_YrolV8jkemCRkO794jja3GHFmpQYzzEsbL7Kk_1uCOk6GeGnniLeOQWLq=GzoOVfGvT7Fu7B77I_4zjw3eyfemnbor6EYae=a/m93XFQAvnwzy9hR4exY2t9D8nruYDF5B6YGj9ZCzR6iD7/FxPABHNPDuieYnI8VY0PhuxPsb3qS0lf3AhaG3hw3lUBMFQifDxd4U73mDehQ_3Cb40_YjOAi5l4NYrxoSEx0G9xnu34rNETUh1Ge9NhihjLD2DzKCO4PY4heQ4UwMKDo0olxhuMtf=7KkrwQinh1WDD")

#  消息模板
PAYLOAD_TEMPLATE = {
    "Title": "自动化测试消息",
    "Receivers": RECEIVERS,
    "Content": r"""["root",{},["p",{},["span",{"data-type":"text"},["span",{"data-type":"leaf"},"这是一条自动发送的消息"]]]]"""
}

# ⚙ 控制参数
TOTAL_MESSAGES =3
DELAY_BETWEEN_REQUESTS = 0.1   # 每次请求间隔（秒），防止过快被封；设为 0 可加速
MAX_WORKERS = 1                # 并发线程数（控制并发压力）
OUTPUT_LOG = True               # 是否打印日志

# 设置请求头
def get_headers(cookie):
    return {
        "Content-Type": "application/json",
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

# 发送单条消息
def send_single_message(msg_id, payload, url, headers):
    try:
        # 把 Receivers 转成字符串数组（确保 JSON 序列化正确）
        payload = payload.copy()
        payload["Receivers"] = RECEIVERS  # 确保每次使用外部变量
        payload["Title"] = f"{PAYLOAD_TEMPLATE['Title']} #{msg_id}"

        resp = requests.post(
            url=url,
            data=json.dumps(payload, ensure_ascii=False),
            headers=headers,
            timeout=10
        )

        if resp.status_code == 200:
            try:
                result = resp.json()
                success = result.get("code") == 0 or result.get("success", False)
                msg = result.get("msg", "ok")
                return msg_id, True, msg
            except json.JSONDecodeError:
                return msg_id, True, "200 OK (non-JSON response)"
        else:
            return msg_id, False, f"HTTP {resp.status_code}: {resp.text[:100]}"
    except Exception as e:
        return msg_id, False, str(e)

# 批量发送
def send_bulk_messages():
    print(f" 开始发送 {TOTAL_MESSAGES} 条消息...")
    print(f" 目标接口: {API_URL}")
    print(f" 接收者: {RECEIVERS}")
    print("-" * 60)

    headers = get_headers(COOKIE)
    success_count = 0
    fail_count = 0
    results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = []
        for i in range(1, TOTAL_MESSAGES + 1):
            # 提交任务（可加入随机延迟等）
            future = executor.submit(send_single_message, i, PAYLOAD_TEMPLATE, API_URL, headers)
            futures.append(future)
            # time.sleep(DELAY_BETWEEN_REQUESTS)  # 控制节奏

        # 收集结果
        for future in as_completed(futures):
            msg_id, ok, msg = future.result()
            if ok:
                success_count += 1
                if OUTPUT_LOG:
                    print(f" [ID:{msg_id}] 成功 | {msg}")
            else:
                fail_count += 1
                print(f" [ID:{msg_id}] 失败 | {msg}")
            results.append((msg_id, ok, msg))

    # 最终统计
    print("-" * 60)
    print(f" 发送完成！总计: {TOTAL_MESSAGES}")
    print(f" 成功: {success_count}")
    print(f" 失败: {fail_count}")

    return results


if __name__ == "__main__":

    if COOKIE == "your_cookie_here":
        print(" 错误：请先在代码中设置有效的 Cookie！")
    else:
        send_bulk_messages()
