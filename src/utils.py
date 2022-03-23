def get_multiline():
    """Get multi line string input"""
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return '\n'.join(lines)


def wait():
    """Funcao de Stall"""
    input("\nPressione Enter para continuar...\n")

def get_int(line):
    """Receber input para integer"""
    while True:
      try:
        x = int(input(line))
        break
      except ValueError:
          print("Por favor introduza um número válido...")
          continue
    return x
