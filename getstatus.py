import json
import time
import requests
from datetime import datetime

def detect_status(link):
    """
    检测网站状态。
    返回值：
        1: 正常 (HTTP 200)
        2: 不正常 (非200响应或异常)
        3: 今日曾经不正常但已恢复（需要与历史记录联动，此处简单处理为非连续异常）
    """
    url = link
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return 1
        else:
            return 2
    except requests.RequestException:
        return 2

def update_status_file(file_path,link):
    try:
        # 尝试读取现有的状态数据
        with open(file_path, 'r', encoding='utf-8') as file:
            status_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # 如果文件不存在或损坏，初始化默认数据
        status_data = {
            "days": [1] * 90,  # 默认90天的状态全为正常
            "current": 1,
            "last_update": ""
        }

    # 获取当前时间
    now = datetime.now()
    current_hour = now.hour
    current_status = detect_status(link)

    # 根据当前状态和历史状态判断是否为"已恢复"
    if (status_data["current"] == 2 or status_data["current"] == 3) and current_status == 1 and (not current_hour == 0):
        current_status = 3

    # 更新当前状态和最后更新时间
    status_data["current"] = current_status
    status_data["days"][len(status_data["days"])-1] = current_status
    status_data["last_update"] = now.isoformat()

    # 如果是新的一天（过零点），更新 days 列表
    if current_hour == 0:
        # 删除第一个状态并追加新的状态
        if len(status_data["days"]) >= 90:
            status_data["days"].pop(0)  # 删除第一个元素
        status_data["days"].append(current_status)

    # 将更新后的数据写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(status_data, file, ensure_ascii=False, indent=4)

    print(f"[{now}] 状态更新完成：当前状态为 {current_status}")

def main():
    file_path = "./status_data_site.json"  # 状态文件路径
    link = "https://acsstudio.site" # 要检测的网站链接
    update_status_file(file_path,link)
    file_path = "./status_data_status.json"  # 状态文件路径
    link = "https://status.acsstudio.site" # 要检测的网站链接
    update_status_file(file_path,link)
    file_path = "./status_data_survey.json"  # 状态文件路径
    link = "https://survey.acsstudio.site" # 要检测的网站链接
    update_status_file(file_path,link)
    while True:
        if datetime.now().minute == 1:
            file_path = "./status_data_site.json"  # 状态文件路径
            link = "https://acsstudio.site" # 要检测的网站链接
            update_status_file(file_path,link)
            file_path = "./status_data_status.json"  # 状态文件路径
            link = "https://status.acsstudio.site" # 要检测的网站链接
            update_status_file(file_path,link)
            file_path = "./status_data_survey.json"  # 状态文件路径
            link = "https://survey.acsstudio.site" # 要检测的网站链接
            update_status_file(file_path,link)
            time.sleep(3540)
            # 每小时检测一次    
        time.sleep(60)

if __name__ == "__main__":
    main()
