from sys import argv

fb_dict = { 3:"Fizz", 5:"Buzz" }

def fizzbuzz(n):
    n = int(n)
    t = sorted(tuple(fb_dict.items()))
    out = [e[1] for e in t if n % int(e[0]) == 0]
    return "".join(out) if len(out) > 0 else n

if __name__ == '__main__':
    start, end = 0, 17
    if len(argv) > 1:
      try: start = int(argv[1])
      except ValueError: pass
      if len(argv) >= 3:
        try: end = int(argv[2])
        except ValueError: pass

    if start > end: end, start = start+1, end-1
    for n in range(start+1, end):
        print(fizzbuzz(n))
