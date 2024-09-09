from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
import os
import requests

# 设置 edgedriver 的路径
edge_driver_path = r"E:\edgedriver_win32\msedgedriver.exe"

# 创建 Edge 浏览器的选项
options = Options()
options.use_chromium = True  # 启用基于 Chromium 的 Edge
options.headless = True  # 无头模式，不显示浏览器界面


# 启动 Edge 浏览器
driver = webdriver.Edge(executable_path=edge_driver_path,port=57822)

# 打开目标页面
url = "https://zhuanlan.zhihu.com/p/533757458"
driver.get(url)

# 等待页面加载完成
time.sleep(3)

# 获取所有的图片标签
images = driver.find_elements("tag name", "img")

# 创建保存图片的文件夹
save_dir = ".\\猫猫虫伽波表情包爬取\\"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for index, img in enumerate(images):
    img_url = img.get_attribute("src")

    # 过滤掉 data:image 类型的图片
    if img_url and img_url.startswith("http"):
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(save_dir, f"image_{index}.jpg")
            with open(img_name, 'wb') as f:
                f.write(img_data)
                print(f"保存图片: {img_name}")
        except Exception as e:
            print(f"下载图片失败: {img_url}, 错误信息: {e}")
    else:
        print(f"跳过图片: {img_url}")

# 关闭浏览器
driver.quit()