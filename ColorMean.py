import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#이미지 불러오기 
image = cv2.imread("/Users/junholee/test/opencvTest/20190717211443887_1000.jpg")
#BRG를 RGB로 바꾸기
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#width와 height를 통합
image = image.reshape(image.shape[0] * image.shape[1],3)

# k - mean 알고리즘으로 k개의 데이터평균을 만들어 clustering
k = 5
clt = KMeans(n_clusters=k)
clt.fit(image)

# 정렬 안된 색상 저장하는 배열
colors = []
# clustering된 컬러값을 확인
for center in clt.cluster_centers_:
    # center값은  RGB값으로 나오므로, web color(16진수)로 변경
    colors.append('#%02x%02x%02x' % (int(round(center[0])), int(round(center[1])), int(round(center[2]))))
    

# 컬러의 분율이 얼마나 되는지 확인
def centroidHistogram(clt):
    # grab the number of differnt clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0,len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

# 색 분율을 구하고, 가공 가능한 리스트로 변환
histRaw = centroidHistogram(clt)
histList = []
histList.extend(histRaw)



# 분율에 따른 정렬

# 정렬된 색을 저장할 배열 선언
colorSorted = []

for i in range(len(histRaw)) :
    #최대 분율의 인덱스
    tempIdx = histList.index(max(histList))
    #최대 분율을 가지는 색상을 최종 배열에 저장
    colorSorted.append(colors[tempIdx])
    #저장한 색상의 분율 및 색상 제외
    histList.pop(tempIdx)
    colors.pop(tempIdx)

print(colorSorted)