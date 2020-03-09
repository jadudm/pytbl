RIGHT  = 0
LEFT   = 1
CENTER = 2

def pad (in_string, limit=20, side=RIGHT):
  current = len(in_string) + 1
  padding = ' ' * (limit - current)
  half_padding = ' ' * ((limit - current) // 2)
  padded = in_string
  if side == RIGHT:
    padded = padded + padding
  elif side == LEFT:
    padded = padding + padded
  else: # side == CENTER:
    padded =  half_padding + padded + half_padding
  return padded