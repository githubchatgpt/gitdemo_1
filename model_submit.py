import requests
from src.main.python.framework.utils.namer.namer import Namer
url="https://pre.modelscope.cn/api/v1/muse/train/submitTrainTask"
headers={
    "Cookie":"cna=I0pdIfdOgXQBASQBsYBnCEoZ; _ga=GA1.1.1784091972.1762761435; _gcl_au=1.1.153697319.1762761435; csrf_session=MTc2Mjc2MTQzOHxEWDhFQVFMX2dBQUJFQUVRQUFBeV80QUFBUVp6ZEhKcGJtY01DZ0FJWTNOeVpsTmhiSFFHYzNSeWFXNW5EQklBRURCSGNtUnhiMnRKYzJwdFprVkpRbVU9fEIKhUpoJq7HoHEBZk6aUfIB3vW-DfqLZG-5h_LX2cIu; csrf_token=5nNMLi2l82ZqvSpitka1R_sciw8%3D; xlly_s=1; _samesite_flag_=true; cookie2=1f4b6af046e72a25333593e4d5e643f2; t=f224389f4fd7dbebf58b899835d9044c; _tb_token_=3bbed56dee7b4; csg=ef4565f9; m_session_id=ade52a3f-a7a6-4888-9e9d-a8a01a0c0014; h_uid=2215631505627; acw_tc=0b62601617630015334188396e67c3632660a28c88aa23dfb9fb2921268029; modelscope_pre_version=9.9.1; _ga_K9CSTSKFC5=GS2.1.s1762999643$o11$g1$t1763002639$j39$l0$h0; ssxmod_itna=1-Yq0xcD2QitjOG0iLc2DUxWK0IPDKDXDUdqiQGgDYq7=GFKDCx7K7eD8bxrU9mZlKnuDxOenouGtDlhYoDZDGFdDqx0oi6jrYe_=HlmYxuxHFGDnDqkl0nI=9=o7kl_gEkkiIRnLkVzX80OTT32FYYx4D=xxDwxibDBKDnpxDjx_rDeWaDCeDQxirDD4DAmoD018pODDd_UgvwI7Kb4rp_4GWODO3ODGCV4GtXISf_IY4U4iaizREO0YDExGOrvr3_4GaVzbnDlKmDm_bCS6yDCI2rRYQp_ffOet89OqYhWDYK0mQYii1zYw=WNkQG1GDP0wS1igjqRWe1GKYK4DDptl0O9GZD2GR7givSGeM0nr3WorihDhQUiiDuKYiOnrb9rN/xOl04FEQR5PeB3=0DnYqeD; ssxmod_itna2=1-Yq0xcD2QitjOG0iLc2DUxWK0IPDKDXDUdqiQGgDYq7=GFKDCx7K7eD8bxrU9mZlKnuDxOenouDYDixfuD1zYQD03RKG7SIx9UYqDs6UQcTakGriIfjX6iYkfMRG6xH=M=asduCd4T5Y98uxvzlhpzjhPO447O/1Piz1uW6YuhIEGxW8wW0Z01Vap5v=FzzrF8kooCTOuKzZ9_srKFHj0fRU3F9GDxvF3xYAMWqZd6ltCrBIpOPoKXV6D8G=G5xbI=KCFNW8y989Iz8y516AEpG6h75zkddY9_HDKxmPFa4y9ma_yzG1rZ90khEzKAiGxo1MClxhaSijODWgPfOCimbYGsjg=6E3RL=BEbISPGdio4CKeaagF7L3qYO4qxGT==Tw30WRiQ6rhzhxWSC8q=1MzKLaIxpZL=/htRBa6htH8i5Sa5_pb8xOhf9GQF1EzOq/O4arkPlNfr7CSNY8vd3jb4dUL3QPIFeNO=1nQiKRqpTElo70hXEwUxRHabQKiEyhFH0NRA1=R=QzCYDd0nvvhtO=m7gCufWYOaGluDPEREIaRGR6P1DUG/I6fpZhbkYHGj=mlGRFWWwbkPs8m20t_yU9xf1UaEBu65b7cT=6nAXfz5bkcTCGUFSPFZnIFCSHsr6eC8_TGAYkx3QT=qFaTtZCWA/AtNAaFw7C_d0_FDoEkh/e0HDctiHFxCBxdcHnz47LiGaDYD4hDefqohDSqD2VltqGQlGkA=D4Nh5YDD; tfstk=g7CtEEMVay3OIqmZWi23notlpl4nhJbwJG7SinxihMIduZXMhNAMkjIFu1xMiPWpDMKeIVA1SStfuiCGIsQqME_f0P-07JbN7IRbqufYZN7N4Ib1_1psAv_ePfTbKd9DrZE4quVutcwDirrlSFBZtBT2AFTjGAapOFYyGEtX5yKBkUkjfiObJyLyyFGXfI9IRFxBcIOfcwapoHT6GIsfRyLq1ea9YVTtMO8kd_6ZJJcSN6L9BnhDvjIRtbvpVNKKG-1pW0-55HhjG3nFwIQfcohDNTSdMLsuMXRGy9OBW9Ujdh9RCGYFD7h6f6Q11hf_xfx1_w6liMajGnBCFLB55kDpJ9_G9pf72jpNdGWyHsq3aCXlrsJ515nyxL8A2C6LAfI54_1lwN_Iq3LmCyUK3xJ68Nz4zaEgW_DMJ346Cxk2ne8pqyES3xJLneKu5ekq3KYF.; isg=BEZGF4RJU0TFDgZjPPo6b4cmlzrIp4phGn60BzBulmlEM-JNmDdqcJyFC2__r4J5"
}
#   maxTrainEpochs轮数 。repeat重复次数
data={
  "checkpointId": 275167,
  "triggerWord": None,
  "urlList": [
    "https://muse-ai.oss-cn-hangzhou.aliyuncs.com/img/7aa4e833-083e-4222-9150-96a5d5e4d175.jpeg",
    "https://muse-ai.oss-cn-hangzhou.aliyuncs.com/img/b2911913-9086-4ce8-8b3d-6930fc8a3def.jpeg",
    "https://muse-ai.oss-cn-hangzhou.aliyuncs.com/img/d4f575a8-435e-45f8-a50c-9fe712e5f455.jpeg"
  ],
  "captionList": [
    "",
    "",
    ""
  ],
  "trainParam": {
    "outputName": Namer.named('lora-model'),
    "repeat": 0,
    "maxTrainEpochs": 0,
    "bucketNoUpscale": None,
    "bucketResoSteps": 64,
    "captionExtension": None,
    "clipSkip": 2,
    "enableBucket": True,
    "imageHeight": 1472,
    "imageWidth": 1104,
    "isModelscopePublic": True,
    "isRestart": False,
    "keepNToken": 0,
    "learningRate": 0.0001,
    "lrScheduler": "constant",
    "lrSchedulerNumCycles": 3,
    "lrWarmupSteps": 0,
    "maxBucketReso": 4096,
    "maxDataLoaderNWorkers": None,
    "maxTokenLength": 225,
    "maxTrainSteps": None,
    "minBucketReso": 128,
    "minSnrGamma": None,
    "mixedPrecision": "bf16",
    "modelChineseName": None,
    "modelTrainType": "flux",
    "multiresNoiseDiscount": 0,
    "multiresNoiseIterations": 0,
    "networkAlpha": 16,
    "networkArgs": None,
    "networkDim": 16,
    "networkModule": None,
    "noHalfVae": True,
    "noiseOffset": 0,
    "optimizerType": "AdamW",
    "pretrainedDitPath": None,
    "pretrainedModelNameOrPath": None,
    "pretrainedTextEncoder2Path": None,
    "pretrainedTextEncoderPath": None,
    "pretrainedVaePath": None,
    "remoteReportKey": None,
    "repoId": None,
    "resolution": None,
    "sampleImageHeight": 1472,
    "sampleImageWidth": 1104,
    "sampleLoraScale": None,
    "sampleNegativePrompts": "",
    "samplePrompts": None,
    "sampleSampler": "DPM++ 2M Karras",
    "sampleSeed": -1,
    "saveEveryNEpochs": 5,
    "saveModelAs": None,
    "savePrecision": "bf16",
    "seed": -1,
    "shuffleCaption": True,
    "textEncoderLr": 0.00001,
    "trainBatchSize": 1,
    "trainDataDir": None,
    "trainTextEncoderOnly": False,
    "trainUnetOnly": False,
    "unetLr": 0.0001,
    "weightedCaption": False,
    "xformers": False,
    "useLoraPlus": True
  },
  "taggerArgs": {},
  "advanced": False,
  "datasetTrainType": "IMAGE",
  "datasetOperation": "CREATE"
}

response=requests.post(url=url,headers=headers,json=data)
print(response.text)