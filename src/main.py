import sys, os
import image_proc as ip
import combine as cb

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <image_dir>")
    sys.exit(1)
  if os.path.isdir(sys.argv[1]) is False:
    print(f"Usage: {sys.argv[0]} <image_dir>")
    sys.exit(1)
  file_list = [os.path.join(sys.argv[1], f) for f in os.listdir(sys.argv[1])]
  ts, rs = [], []
  for f in file_list:
      print(f"Analyzing {f}")
      img = ip.read_image(f)
      t = ip.Target(img)
      r = cb.compute_attr(t)
      ts.append(t)
      rs.append(r)
  print(f"Combination started on {len(rs)} targets ...") 
  res = cb.combine(rs)
  new_circle = cb.compute_target(res, len(ts))
  new_circle_points, new_circle_center = new_circle[1], new_circle[0]
  ip.make_image((2000,3000), new_circle_points, new_circle_center, [])
  print("Finished without error. Can check result.jpg")

def foo():
  sample_points = []
  diff_a, diff_b = t1.center[0] - new_circle_center[0], t1.center[1] - new_circle_center[1]
  for i in t1.borders:
      sample_points.append((t1.points[i][0] - diff_a, t1.points[i][1] - diff_b))
  diff_a, diff_b = t2.center[0] - new_circle_center[0], t2.center[1] - new_circle_center[1]
  for i in t2.borders:
      sample_points.append((t2.points[i][0] - diff_a, t2.points[i][1] - diff_b))

