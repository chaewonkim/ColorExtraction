import sys
import os
from ColorExtractor import extractHexColor
from seg import removeBgr


#경로 설정
imagePath = sys.argv[1]
outputPath = imagePath[:imagePath.rfind("/")+1] + "output_" + imagePath[imagePath.rfind("/")+1:imagePath.rfind(".")+1]+"png"
print(outputPath)
#배경지운파일생성
removeBgr(imagePath, outputPath, 1)
print("background removed file created")
#색상코드 추출
hexColor = extractHexColor(outputPath,4)
#프린트
print(hexColor)

#중간파일삭제
os.remove(outputPath)