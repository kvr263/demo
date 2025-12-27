def main():
  a = list(range(10))
  for val in a:
    if val % 2 == 0:
        val = 0 
  print(a)


def addItem(item, my_list):
  my_list.append(item)
  return my_list

if __name__ == "__main__":
  main()
  addItem("abc",[])
