#!/usr/bin/env python3
"""
ModelScope 多模态功能演示代码
展示文本、图像、语音等主流AI任务
"""

import torch
import numpy as np
from PIL import Image
import soundfile as sf
import matplotlib.pyplot as plt
from modelscope import snapshot_download
from modelscope.pipelines import pipeline
from modelscope.models import Model
from modelscope.preprocessors import Preprocessor
from modelscope.msdatasets import MsDataset
from modelscope.trainers import build_trainer
from modelscope.outputs import OutputKeys
import warnings

warnings.filterwarnings('ignore')


def setup_environment():
    """设置环境"""
    print("=" * 60)
    print("ModelScope 功能演示")
    print(f"PyTorch版本: {torch.__version__}")
    print(f"CUDA可用: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    print("=" * 60 + "\n")


def download_model_example():
    """示例1：下载模型"""
    print("📥 1. 下载预训练模型")

    model_id = 'damo/nlp_structbert_sentence-similarity_chinese-base'
    try:
        model_dir = snapshot_download(
            model_id=model_id,
            cache_dir='./models',  # 指定缓存目录
            revision='v1.0.0'  # 指定版本
        )
        print(f"✅ 模型下载完成: {model_dir}")
        return model_dir
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        return None


def nlp_text_classification():
    """示例2：NLP文本分类"""
    print("\n📝 2. NLP文本分类")

    # 创建文本分类pipeline
    classifier = pipeline(
        task='text-classification',
        model='damo/nlp_structbert_classification_chinese-base'
    )

    texts = [
        "这部电影真是太精彩了，演员演技在线！",
        "服务态度很差，产品质量也有问题。",
        "今天天气不错，适合出去散步。"
    ]

    for text in texts:
        result = classifier(text)
        print(f"\n文本: {text[:30]}...")
        print(f"情感: {result['label']} (置信度: {result['score']:.3f})")

    return classifier


def nlp_sentence_similarity():
    """示例3：句子相似度计算"""
    print("\n🔗 3. 句子相似度计算")

    sim_pipeline = pipeline(
        task='sentence-similarity',
        model='damo/nlp_structbert_sentence-similarity_chinese-base'
    )

    sentences = [
        "我喜欢吃苹果",
        "苹果是一种水果",
        "我正在使用苹果手机",
        "香蕉是黄色的水果"
    ]

    # 计算相似度矩阵
    results = sim_pipeline(input=(sentences, sentences))

    print("\n句子相似度矩阵:")
    for i, sent1 in enumerate(sentences):
        similarities = []
        for j, sent2 in enumerate(sentences):
            similarity = results[i][j]
            similarities.append(f"{similarity:.3f}")
        print(f"{sent1[:15]:<15} | {' '.join(similarities)}")


def computer_vision_segmentation():
    """示例4：计算机视觉 - 图像分割"""
    print("\n🖼️  4. 图像分割 (人像抠图)")

    try:
        # 创建图像分割pipeline
        segmenter = pipeline(
            task='image-matting',
            model='damo/cv_unet_image-matting'
        )

        # 示例：如果没有实际图片，创建一个虚拟图片
        print("⚠️  由于没有真实图片，这里展示调用方式")
        print("实际使用时，传入图片路径即可:")
        print("result = segmenter('path/to/your/image.jpg')")
        print(f"输出包含: {OutputKeys.OUTPUT_IMG}")

        # 如果真的有图片，可以这样用：
        # result = segmenter({
        #     'image': 'input.jpg',
        #     'background': 'background.jpg'  # 可选，替换背景
        # })
        # Image.fromarray(result[OutputKeys.OUTPUT_IMG]).save('output.png')

        return segmenter
    except Exception as e:
        print(f"❌ 图像分割初始化失败: {e}")
        return None


def speech_recognition_example():
    """示例5：语音识别"""
    print("\n🎤 5. 语音识别 (ASR)")

    try:
        # 创建语音识别pipeline
        asr_pipeline = pipeline(
            task='auto-speech-recognition',
            model='damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch'
        )

        print("支持的音频格式: WAV, MP3, FLAC等")
        print("采样率要求: 16kHz")
        print("\n实际调用方式:")
        print("result = asr_pipeline('audio.wav')")
        print("text = result['text']  # 识别结果")

        # 如果有音频文件，可以这样用：
        # result = asr_pipeline('path/to/audio.wav')
        # print(f"识别结果: {result['text']}")

        return asr_pipeline
    except Exception as e:
        print(f"❌ 语音识别初始化失败: {e}")
        return None


def dataset_loading_example():
    """示例6：加载数据集"""
    print("\n📊 6. 加载数据集")

    try:
        # 加载中文情感分析数据集
        dataset = MsDataset.load(
            'afqmc',
            namespace='modelscope',
            subset_name='default',
            split='train'
        )

        print(f"数据集: AFQMC (蚂蚁金融语义相似度)")
        print(f"样本数: 使用前5个样本演示")

        # 查看前几个样本
        for i, item in enumerate(dataset):
            if i >= 5:
                break
            print(f"样本{i + 1}: {item['sentence1'][:50]}... | {item['sentence2'][:50]}...")

        return dataset
    except Exception as e:
        print(f"❌ 数据集加载失败: {e}")
        return None


def model_inference_direct():
    """示例7：直接使用模型进行推理"""
    print("\n⚙️  7. 直接模型推理")

    try:
        # 直接加载模型
        model = Model.from_pretrained(
            'damo/nlp_structbert_sentiment-classification_chinese-base'
        )

        # 加载对应的预处理器
        from modelscope.preprocessors.nlp import TextClassificationTransformersPreprocessor
        preprocessor = TextClassificationTransformersPreprocessor(
            model.model_dir,
            first_sequence='sentence',
            second_sequence=None,
            label='label',
            label2id=model.config.label2id
        )

        print("✅ 模型和预处理器加载成功")
        print(f"模型类型: {type(model).__name__}")
        print(f"标签映射: {model.config.label2id}")

        # 示例输入
        sample_input = {'sentence': '这个产品非常好用'}
        processed = preprocessor(sample_input)
        print(f"预处理后的输入shape: {processed['input_ids'].shape}")

        return model, preprocessor
    except Exception as e:
        print(f"❌ 直接模型推理失败: {e}")
        return None, None


def batch_processing_example():
    """示例8：批量处理"""
    print("\n📦 8. 批量处理示例")

    # 创建pipeline
    batch_pipeline = pipeline(
        task='text-classification',
        model='damo/nlp_structbert_classification_chinese-base'
    )

    # 批量输入
    batch_texts = [
        "这个餐厅的食物非常美味",
        "物流速度太慢了",
        "客服态度很好，解决问题很快",
        "性价比不高，不推荐购买"
    ]

    print("批量处理结果:")
    results = batch_pipeline(batch_texts)

    for i, (text, result) in enumerate(zip(batch_texts, results)):
        label = "正面" if result['label'] == 'positive' else "负面"
        print(f"{i + 1}. {text[:20]:<20} → {label} ({result['score']:.3f})")


def advanced_features():
    """示例9：高级特性演示"""
    print("\n🚀 9. 高级特性")

    # 1. 模型信息查看
    print("📋 模型信息查看:")
    from modelscope.hub.api import ModelHubAPI
    api = ModelHubAPI()

    # 获取模型卡片信息（示例）
    print("可通过 api.get_model('model_id') 获取模型详细信息")

    # 2. 自定义推理参数
    print("\n⚙️  自定义推理参数:")
    classifier = pipeline(
        task='text-classification',
        model='damo/nlp_structbert_classification_chinese-base'
    )

    # 自定义推理参数
    custom_config = {
        'max_length': 128,
        'truncation': True,
        'padding': 'max_length'
    }

    result = classifier(
        "这是一个测试文本",
        **custom_config
    )
    print(f"使用自定义参数推理: {result}")

    # 3. Pipeline配置
    print("\n🔧 Pipeline配置选项:")
    print("- device: 指定运行设备 ('cuda:0', 'cpu')")
    print("- batch_size: 批量大小")
    print("- model_revision: 模型版本")
    print("- pipeline_name: 指定pipeline类型")


def main():
    """主函数"""
    setup_environment()

    # 演示各个功能
    download_model_example()
    nlp_text_classification()
    nlp_sentence_similarity()
    computer_vision_segmentation()
    speech_recognition_example()
    dataset_loading_example()
    model_inference_direct()
    batch_processing_example()
    advanced_features()

    print("\n" + "=" * 60)
    print("🎉 ModelScope 功能演示完成!")
    print("=" * 60)
    print("\n📚 核心使用模式总结:")
    print("1. Pipeline模式 (快速上手):")
    print("   pipeline = pipeline(task='xxx', model='model_id')")
    print("   result = pipeline(input_data)")
    print("\n2. 直接模型模式 (灵活控制):")
    print("   model = Model.from_pretrained('model_id')")
    print("   preprocessor = Preprocessor.from_pretrained('model_id')")
    print("\n3. 数据集模式 (训练/评估):")
    print("   dataset = MsDataset.load('dataset_name')")
    print("\n💡 更多功能请参考: https://modelscope.cn/docs")


if __name__ == '__main__':
    main()