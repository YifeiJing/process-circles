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

