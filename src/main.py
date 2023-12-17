import sys
import image_proc as ip
import combine as cb

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <image1_path_name> <image2_path_name>")
    sys.exit(1)
  img_np_1 = ip.read_image(sys.argv[1])
  img_np_2 = ip.read_image(sys.argv[2])
  t1, t2 = ip.Target(img_np_1), ip.Target(img_np_2)
  r1, r2 = cb.compute_attr(t1), cb.compute_attr(t2)
  res = cb.combine(r1,r2)
  new_circle = cb.compute_target(res)
  new_circle_points, new_circle_center = new_circle[1], new_circle[0]
  a, b = max(img_np_1.shape[0], img_np_2.shape[0]), max(img_np_1.shape[1], img_np_2.shape[1])
  print(f"a,b: {a}, {b}")
  sample_points = []
  diff_a, diff_b = t1.center[0] - new_circle_center[0], t1.center[1] - new_circle_center[1]
  for i in t1.borders:
      sample_points.append((t1.points[i][0] - diff_a, t1.points[i][1] - diff_b))
  diff_a, diff_b = t2.center[0] - new_circle_center[0], t2.center[1] - new_circle_center[1]
  for i in t2.borders:
      sample_points.append((t2.points[i][0] - diff_a, t2.points[i][1] - diff_b))
  ip.make_image((2000,3000), new_circle_points, new_circle_center, sample_points)
