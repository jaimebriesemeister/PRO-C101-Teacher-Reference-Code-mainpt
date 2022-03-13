# importe o módulo time
import time
  
# defina a função de contagem regressiva do cronômetro
def countdown_timer(seconds):
    
    while seconds > 0:       

        mins = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'

        print(timer)
        
        seconds -= 1
      
    print('Tempo Esgotado!')
  
  
# input time in seconds
seconds = input("Digite o tempo em segundos: ")
  
# function call
countdown_timer(int(seconds))