from PIL import Image, ImageFilter
import numpy as np
import sys
from union_find import UnionFind

class Target:
  def __init__(self, img_np):
      (x,y) = img_np.shape
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


  def __str__(self):
      res = ""
      return f"{len(self.points)} points with the center {self.center}"
      for p in self.points:
          res += f"({p[0]},{p[1]})"
      return res

def read_image(path):
    return np.array(Image.open(path).convert('L'))
def write_image(path, img_np):
    Image.fromarray(img_np).save(path)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <image_path_name>")
    sys.exit(1)
  img_np = read_image(sys.argv[1])
  print(img_np.shape)
  t = Target(img_np)
  #print(t)
  #Image.fromarray(img_np).show()
