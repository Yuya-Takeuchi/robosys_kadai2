# robosys_kadai2
ロボットシステム学　課題２

## 概要
２つのノードを動かし、suuzi.pyに入力した数字が３の倍数または３のつく数字だった場合「アホになる」、  
それ以外の数字だった場合「何もなし」をnabeatu.pyで出力する。


## 環境構築
[こちら](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop)のスクリプトを使用しROSの環境構築をしました。


## 動作環境
- Ubuntu 20.04
- Ros Noetic

## 実行手順

1.インストール
```
cd　 ~/catkin_ws/src
git clone https://github.com/Yuya-Takeuchi/robosys_kadai2.git
cd ..
catkin_make
source ~/.bashrc
```
2.ターミナル①でroscoreを立ち上げる
```
roscore
```
3.ターミナル②でsuuzi.pyを立ち上げる。
```
chmod +x suuzi.py
rosrun robosys_kadai2 suuzi.py
```
4.ターミナル③でnabeatu.pyを立ち上げる。
```
chmod +x nabeatu.py
rosrun robosys_kadai2 nabeatu.py
```


## デモ動画
実際に動かしたときの映像が[こちら](https://youtu.be/Aa_mUcEzrWc)です。

## ライセンス
[BSD 3-Clause License](https://github.com/Yuya-Takeuchi/robosys_kadai2/blob/main/LICENSE)
