
def compute_hw_average(grades):
    if len(grades) == 0:
        return 0
    return grades[0]

def compute_hw_average(grades):
  if len(grades) == 0:
      return 0
  return sum(grades) / len(grades)
