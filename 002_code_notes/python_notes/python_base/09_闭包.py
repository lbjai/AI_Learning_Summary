"""
形成闭包的条件
1.函数嵌套
2.将内部函数作为返回值返回
3.内部函数必须要使用外部函数的变量
"""
from keras.models import load_model
from keras.preprocessing import image
import numpy as np


def predict(img):
    """
    加载模型和模型预测
    主要步骤:
        1.加载模型(请加载你认为的最佳模型)
        2.图片处理
        3.用加载的模型预测图片的类别
    :param img: PIL.Image 对象
    :return: string, 模型识别图片的类别,
            共 'cardboard','glass','metal','paper','plastic','trash' 6 个类别
    """
    # 把图片转换成为numpy数组
    img = image.img_to_array(img)
    x = np.expand_dims(img, axis=0)
    y = model.predict(x)

    labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
    # -------------------------------------------------------------------------
    predict = labels[np.argmax(y)]
    # 返回图片的类别
    return predict


# 输入图片路径和名称
img_path = 'test.jpg'

# 打印该张图片的类别
img = image.load_img(img_path)
print(predict(img))


class Prediction:
    def __init__(self):
        # 如果你的模型是在 results 文件夹下的 dnn.h5 模型，则 self.model_path = 'results/dnn.h5'
        self.model_path = ""
        self.img = img
        self.model = self.load_model()

    def load_model(self):
        # 加载模型,加载请注意 model_path 是相对路径, 与当前文件同级。
        try:
            # 作业提交时测试用, 请勿删除此部分
            model_path = os.path.realpath(__file__).replace('main.py', model_path)
        except NameError:
            model_path = './' + model_path

        # -------------------------- 实现模型预测部分的代码 ---------------------------
        # 加载模型
        model = load_model(model_path)

        return model

    def predict(self,img):
        """
        加载模型和模型预测
        主要步骤:
            1.加载模型(请加载你认为的最佳模型)
            2.图片处理
            3.用加载的模型预测图片的类别
        :param img: PIL.Image 对象
        :return: string, 模型识别图片的类别,
                共 'cardboard','glass','metal','paper','plastic','trash' 6 个类别
        """
        # 把图片转换成为numpy数组
        img = image.img_to_array(img)
        x = np.expand_dims(img, axis=0)
        y = self.model.predict(x)

        labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
        # -------------------------------------------------------------------------
        y_predict = labels[np.argmax(y)]
        # 返回图片的类别
        return y_predict
