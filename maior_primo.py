def maior_primo (xNum1):

  xNum = int(xNum1) 
  if xNum >= 2:
      
     xi01 = 2
     xUly = 2
     while xi01 <= xNum:
        xRange = range(2,xi01+1)
        xi02 = 0
        xUlt_Primo = True
        while xi02 <= len(xRange)-1:  
           xd = xRange[xi02]
           if xi01%xd == 0 and xi01 != xd:
              xUlt_Primo = False
           xi02 +=1
        if xUlt_Primo:   
           xUlt = xi01     
        xi01 +=1
     return (xUlt)
        


    
       
