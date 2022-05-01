import urllib.request  # 导入包
import pandas as pd
from tqdm import tqdm


def getHtml(url):  # 获取html的内容
    html = urllib.request.urlopen(url).read()  # bytes 如果不用read()，html会是一个↓
    return html                                # http.client.HTTPResponse的变量


def saveHtml(fileName, fileContent):
    with open(fileName, "wb") as f:  # 以wb打开文件
        f.write(fileContent)  # 写入


def main():
    Lmore15=pd.read_csv('200wLmore15_notrepeat.csv')
    objID=Lmore15['objID']
    RA_ICRS=Lmore15['RA_ICRS']
    DE_ICRS=Lmore15['DE_ICRS']
    for i in range(len(objID)):
        url = 'http://skyserver.sdss.org/dr17/VisualTools/navi?ra='+str(RA_ICRS[i])+'&dec='+str(DE_ICRS[i])+'&scale=0.02'
        html = getHtml(url)
        saveHtml('navi/sdss_objID_'+str(objID[i])+'.html', html)
        break
    # url = "http://skyserver.sdss.org/dr17/VisualTools/explore/summary?id=1237668296598749280"  # url
    # html = getHtml(url)  # 调用函数获取bytes
    # saveHtml("sdss_1237668296598749280.html", html)  # 保存
    print("保存网页完成")  # 提示语


if __name__ == "__main__":  # 主函数
    main()

