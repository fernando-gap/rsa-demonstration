def blocks(M):
  blocks = []
  for two in range(2, len(M)+2, 2):
      blocks.append(M[two-2:two])

  return convert_blocks(blocks)


# Os blocos sao convertidos em decimal e depois para hexadecimal
def convert_blocks(blocks):
  result = []

  for letter in blocks:
      hex_digits = ''
      for char in [*letter]:
          hex_digits += hex(ord(char))[2:]
          result.append(hex_digits)

  return result


# Os blocos sao revertidos para letras
def revert_blocks(M):
  result = []
  for block in M:
      left_side = block[:2]

      if len(block) > 2:
          right_side = chr(int(block[2:], base=16))
      else:
          right_side = ''

      result.append(chr(int(left_side, base=16)) + right_side)

  return result
