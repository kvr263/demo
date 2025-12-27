def main():
  a = list(range(10))
  for val in a:
    if val % 2 == 0:
        val = 0 
  print(a)

if __name__ == "__main__":
  main()
