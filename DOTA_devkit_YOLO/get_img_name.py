import os
#import cPickle




def GetFileFromThisRootDir(dir,ext = None):
  allfiles = []
  needExtFilter = (ext != None)
  for root,dirs,files in os.walk(dir):
    for filespath in files:
      filepath = os.path.join(root, filespath)
      extension = os.path.splitext(filepath)[1][1:]
      if needExtFilter and extension in ext:
        allfiles.append(filepath)
      elif not needExtFilter:
        allfiles.append(filepath)
  return allfiles


def image2txt(srcpath, dstpath):
    """
    将srcpath文件夹下的所有子文件名称打印到namefile.txt中
    @param srcpath: imageset
    @param dstpath: imgnamefile.txt的存放路径
    """
    filelist = GetFileFromThisRootDir(srcpath)  # srcpath文件夹下的所有文件相对路径 eg:['example_split/../P0001.txt', ..., '?.txt']
    for fullname in filelist:  # 'example_split/../P0001.txt'
        name = os.path.basename(os.path.splitext(fullname)[0])# 只留下文件名 eg:P0001
        print(name)
        # name = os.path.basename(os.path.splitext(fullname)) #保留全程
        dstname = os.path.join(dstpath, 'test_split_imgnamefile.txt')  # eg: result/imgnamefile.txt
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        with open(dstname, 'a') as f:
            f.writelines(name + '\n')

if __name__ == '__main__':
   
    # image2txt('/home/liyuchen/eff/Rotation-EfficientDet-D0-master-new/eval/HRSC2016/test/', '/home/liyuchen/eff/Rotation-EfficientDet-D0-master-new/eval/HRSC2016')
    # image2txt('/home/liyuchen/eff/Rotation-EfficientDet-D0-master-new/datasets/DOTA_v1.0/val_split/', '/home/liyuchen/eff/Rotation-EfficientDet-D0-master-new/datasets/DOTA_v1.0/val_name')
    # image2txt('/home/liyuchen/YOLOX/YOLOX-OBB-main/datasets/DOTA_v1.0/val/images/', '/home/liyuchen/YOLOX/YOLOX-OBB-main/datasets/DOTA_v1.0/val/val_name')
    image2txt('/home/liyuchen/YOLOX/YOLOX-OBB-main/datasets/fastener/JPEGImages/', '/home/liyuchen/YOLOX/YOLOX-OBB-main/datasets/fastener/ImageSets/train_name')
    

   