import numpy as np
import cv2
import os

def Laplacian(img):
    Mods = {1:[[0,-1,0],[-1,4,-1],[0,0-1,0]],
            2:[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],
            3:[[1,-2,1],[-2,4,-2],[1,-2,1]],
            4:[[0,-1,0],[-1,5,-1],[0,-1,0]]}
    #print (Mods)

    SourceArray = np.array(img)
    index = SourceArray.shape
    #print (index)
    OutArrey = np.zeros((index),dtype=int)

    for flag in Mods:
        key = np.array(Mods[flag])
        for i in range(1,index[0]-1):
            for j in range(1,index[1]-1):
                temp = (SourceArray[i-1][j-1]*key[0][0] + SourceArray[i-1][j]*key[0][1] + SourceArray[i-1][j+1]*key[0][2] +
                        SourceArray[i][j-1]*key[1][0] + SourceArray[i][j]*key[1][1] + SourceArray[i][j+1]*key[1][2] + 
                        SourceArray[i+1][j-1]*key[2][0] + SourceArray[i+1][j]*key[2][1] + SourceArray[i+1][j+1]*key[2][2])
                OutArrey[i][j] = temp
        AimImg = 'aim{}.jpg'.format(flag)
        cv2.imwrite(AimImg,OutArrey)        
    
    return None

def main():
    Img_1 = cv2.imread('E:\\Microsoft VS Code\\MyPython\\Demo_1\\source.jpg',2|4)
    Laplacian(Img_1)
    #cv2.imshow('asd.png',Img_2)
    #os.system('pause')
    return None

if __name__ == '__main__':
    main()


