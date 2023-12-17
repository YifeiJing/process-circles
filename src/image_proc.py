from PIL import Image, ImageFilter
import cv2 as cv
import numpy as np
import sys
from union_find import UnionFind

class Target:
  def __init__(self, img_np):
      (x,y) = img_np.shape
      print(f"Image size: {img_np.shape}")
      self.points = []
      for i in range(x):
         for j in range(y):
              if img_np[i,j] == 0:
                  self.points.append((i,j))
      self.uf = UnionFind(len(self.points))
      def is_connected(p1, p2):
          x_diff, y_diff = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
          if x_diff <= 1 and y_diff <= 1:
              return True
          else:
              return False

      for i in range(len(self.points)):
          for j in range(i+1, len(self.points)):
              if is_connected(self.points[i], self.points[j]):
                  self.uf.union(i, j)
       # find the two groups with the most members
      largestA, largestB = 0, 0
      for i in range(len(self.uf.size)):
          if self.uf.size[i] > self.uf.size[largestA]:
              largestB = largestA
              largestA = i
          elif self.uf.size[i] > self.uf.size[largestB]:
              largestB = i
      groupA, groupB = [], []
      for i in range(len(self.points)):
          if self.uf.find(i) == largestA:
              groupA.append(i)
          else:
              groupB.append(i)
      # find the center point by average all points in the area
      x_sum, y_sum = 0, 0
      for i in groupB:
          x_sum += self.points[i][0]
          y_sum += self.points[i][1]
      self.center = (round(x_sum/len(groupB)), round(y_sum/len(groupB)))
      print(f"Center detected: {self.center}")
      self.borders = groupA
      self.centers = groupB

  def __str__(self):
      res = ""
      return f"{len(self.points)} points with the center {self.center}"
      for p in self.points:
          res += f"({p[0]},{p[1]})"
      return res

def read_image(path):
    orig_img = 255 - cv.cvtColor(cv.imread(path), cv.COLOR_BGR2GRAY)
    kernel = np.ones((4,4), np.uint8)
    erode = cv.erode(orig_img, kernel, iterations=1)
    return 255 - erode

def make_image(size, res_points, center, sample_points):
    img = np.ones(size, dtype=np.uint8) * 255
    for i in range(len(res_points)):
        img[res_points[i][0], res_points[i][1]] = 128
    for i in range(len(sample_points)):
        img[sample_points[i][0], sample_points[i][1]] = 0
    def make_center(c):
        img[c[0] - 1, c[1]] = 0
        img[c[0] + 1, c[1]] = 0
        img[c[0], c[1] - 1] = 0
        img[c[0], c[1] + 1] = 0
        img[c] = 0
    make_center(center)
    cv.imwrite('result.jpg', img)

def write_image(path, img_np):
    Image.fromarray(img_np).save(path)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <image_path_name>")
    sys.exit(1)
  img_np = read_image(sys.argv[1])
  print(img_np.shape)
  #t = Target(img_np)
  #print(t)
  make_image((120, 100), [(10,10), (100, 90), (0,0), (1,0), (2,0)], (50, 50))
