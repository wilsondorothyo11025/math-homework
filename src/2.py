  from random import randint
  
  def calculate_area(shape):
      if shape == 'rectangle':
          width = randint(1, 10)
          height = randint(1, 10)
          return width * height
      elif shape == 'square':
          side = randint(1, 10)
          return side * side
      elif shape == 'circle':
          radius = randint(1, 10)
          return 3.14 * radius ** 2