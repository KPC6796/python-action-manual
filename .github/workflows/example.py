import os

def main():
  print("Hello Kamakshi")
  
  token = os.environ.get('PYTHON_ACTION_MANUAL')
  if not token:
    raise RunTimeError('PYTHON_ACTION_MANUAL env var is not set')
  print('We found our env var')
  
if __name__ == '__main__':
  main()
