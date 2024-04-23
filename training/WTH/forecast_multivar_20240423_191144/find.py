# @Time : 2024/4/23 19:31
# @Author : SYY

import pickle

# 打开.pkl文件
with open('eval_res.pkl', 'rb') as f:
    # 使用pickle模块加载数据
    data = pickle.load(f)

print(data)