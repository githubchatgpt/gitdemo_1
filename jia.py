from PIL import Image, ImageDraw
import os

# 创建输出文件夹
output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)

for i in range(150):
    # 创建新图片（RGB模式，400x300像素，白色背景）
    img = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(img)

    # 添加一些简单图形和文字
    draw.rectangle([50, 50, 350, 250], outline='blue', width=2)
    draw.text((150, 140), f'Image {i + 1}', fill='black')

    # 保存图片
    img.save(f'{output_dir}/image_{i + 1:03d}.png')

print("100张图片生成完成！")