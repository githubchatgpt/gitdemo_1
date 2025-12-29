from PIL import Image, ImageDraw
import os


output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)

for i in range(150):

    img = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(img)


    draw.rectangle([50, 50, 350, 250], outline='blue', width=2)
    draw.text((150, 140), f'Image {i + 1}', fill='black')

    # 保存图片
    img.save(f'{output_dir}/image_{i + 1:03d}.png')

print("100张图片生成完成！")