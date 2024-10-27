import sys
import os
import time

def clean_screen():
    os.system('cls' if os.name =='nt' else 'clear')

frames = [
    r"""
        (\___/)              (\___/)  
       (=' . '=)            (=' . '=)  
       (")___(")            (")___(")  
   Don't you                  want me        
""",
    r"""
       (\___/)~            ~(\___/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
   Like                      I want you 
""",
    r"""
     ~(\___/)              (\___/)~  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
   baby                     Don't you  
""",
    r"""
        (\___/)              (\___/)  
    ~(=' . '=)~          ~(=' . '=)~  
      (")___(")            (")___(")  
     need me               Like I need you 
""",
    r"""
      ~(\___/)~           ~(\___/)~  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
    now                    Sleep tomorrow
""",
    r"""
     (\___/)  =>         <=  (\___/)  
     (=' . '=)           (=' . '=)  
     (")___(")           (")___(")  
    But tonight              go crazy
""",
    r"""
      (\___/)               (\___/)  
   ~(=' . '=)~           ~(=' . '=)~  
     (")___(")            (")___(")  
  All you gotta           Do is meet me
""",
    r"""
        (\___/)              (\___/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
    At the                   Apateu
""",
    r"""
      (\___/)               (\___/)  
   ~(=' . '=)~           ~(=' . '=)~  
     (")___(")            (")___(")    
      Apateu                  Apateu  
""",
    r"""
        (\___/)              (\___/)  
      (=' . '=)            (=' . '=)  
      (")___(")            (")___(")  
      Apateu                  Apateu  
"""
]


def animated_bunny():
    for i in range(5):
        for frame in frames:
            clean_screen()
            print(frame)
            time.sleep(1.2)

animated_bunny()
