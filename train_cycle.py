# ====================
# 学習サイクルの実行
# ====================

# パッケージのインポート
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='1'
from dual_network import dual_network
from self_play import self_play
from train_network import train_network
from evaluate_network import evaluate_network

# デュアルネットワークの作成
dual_network()

for i in range(5):
    print('Train',i,'====================')
    # セルフプレイ部
    self_play()

    # パラメータ更新部
    train_network()

    # 新ハ゜ラメータ評価部
    evaluate_network()