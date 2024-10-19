import sys
import os
import time

def clean_screen():
    os.system('cls' if os.name =='nt' else 'clear')

frames = [
    r"""
        (\_/)                (\_/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
           Hi                  ...  
""",
    r"""
        (\_/)                (\_/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
           Hi                  Hi  
""",
    r"""
        (\_/)                (\_/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
      You so cute            ...  
""",
    r"""
        (\_/)                (\_/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
      You so cute          Thank you!  
""",
    r"""
        (\_/)                (\_/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
         :)                   :)  
""",
    r"""
        (\_/)  =>         <=  (\_/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
         Mwah               Mwah  
""",
    r"""
        (\_/)                (\_/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
       Blushing           Blushing  
"""
]





def animated_bunny():
    for i in range(5):
        for frame in frames:
            clean_screen()
            print(frame)
            time.sleep(0.5)

animated_bunny()
