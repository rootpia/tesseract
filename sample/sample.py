# -*- coding: utf-8 -*-
from pytesseract import pytesseract
from PIL import Image
import os

def sampleA(filepath):
    # 1枠の縦横ピクセル
    w = 80
    h = 65

    # 枠線を除去するマージンピクセル。縦横共通。
    margin_w = 20
    margin_h = 15

    img = Image.open(filepath, "r")
    for pos_h in range(0, 3):
        # 読み取るマスの左上位置
        leftpos_y = margin_h + (h * pos_h) + (margin_h * pos_h)
        for pos_w in range(0, 3):
            # 読み取るマスの左上位置
            leftpos_x = margin_w + (w * pos_w) + (margin_w * pos_w)

            # 該当のマスをトリミング
            crop = img.crop((leftpos_x, leftpos_y, leftpos_x + w, leftpos_y + h))
            # crop.save("/opt/crop" + str(imgid) + "-" +  str(pos_h) + "-" + str(pos_w) + ".png")

            # インストールしたtesseractコマンドのパス
            pytesseract.tesseract_cmd = "/usr/bin/tesseract"

            # -psm 10は1文字判定のフラグ
            result = pytesseract.image_to_string(crop, config="-psm 10 -c tessedit_char_whitelist='0123456789-.'", lang="eng+jpn")

            print(result)

def sampleB(filepath):
    # -psmを未指定の場合、画像全体から文字認識する
    img = Image.open(filepath, "r")
    pytesseract.tesseract_cmd = "/usr/bin/tesseract"
    result = pytesseract.image_to_string(img, config="-c tessedit_char_whitelist='0123456789-.'", lang="eng+jpn")
    print(result)

def sampleC(filepath):
    img = Image.open(filepath, "r")
    pytesseract.tesseract_cmd = "/usr/bin/tesseract"
    result = pytesseract.image_to_string(img, lang="eng")
    print(result.encode('utf-8'))


if __name__ == '__main__':
    filepath1 = os.path.dirname(os.path.abspath(__file__)) + "/sample1.png"
    print("--- sample1A ---")
    sampleA(filepath1)
    print("--- sample1B ---")
    sampleB(filepath1)
    print("--- sample1C ---")
    sampleC(filepath1)

    filepath2 = os.path.dirname(os.path.abspath(__file__)) + "/sample2.png"
    print("--- sample2B ---")
    sampleB(filepath2)
    print("--- sample2C ---")
    sampleC(filepath2)

    filepath3 = os.path.dirname(os.path.abspath(__file__)) + "/sample3.png"
    print("--- sample3C ---")
    sampleC(filepath3)

    filepath4 = os.path.dirname(os.path.abspath(__file__)) + "/sample4.png"
    print("--- sample4B ---")
    sampleB(filepath4)
    print("--- sample4C ---")
    sampleC(filepath4)
