def operator_error(problem):
  if problem.find('*')!= -1 or problem.find('/')!= -1:
    return True

def checkNumericError(num1,num2):
  if (num1.isnumeric() is False) or (num2.isnumeric() is False):
    return True

def numLengthError(num1,num2):
  if len(num1)>4 or len(num2)>4:
    return True

def arithmetic_arranger(problems,ans = None):
    arranged_problems = ''
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    spaceBetweenProblem = ' ' * 4

    #If number of problems is > 5
    if len(problems) > 5:
      return "Error: Too many problems."
    
    for prob in problems:
      if operator_error(prob):
        return "Error: Operator must be '+' or '-'."

      opr = ' + ' if prob.find('+')!=-1 else ' - '
      probList = prob.split(opr)
      opr = opr.strip()

      if checkNumericError(probList[0],probList[1]):
        return "Error: Numbers must only contain digits."

      if numLengthError(probList[0],probList[1]):
        return "Error: Numbers cannot be more than four digits."
      
      num1 = probList[0]
      num2 = probList[1]
      width = len(num1)+2 if len(num1)>len(num2) else len(num2)+2
      expr = num1 + opr + num2
      #print(expr)
      res = str(eval(expr))
      res = res.rjust(width)
      num1 = num1.rjust(width)
      num2 = num2.rjust(width-2)
      num2 = opr + ' ' + num2
      
      row1 += num1 + spaceBetweenProblem
      row2 += num2 + spaceBetweenProblem
      row3 += ('-' * width) + spaceBetweenProblem
      row4 += res + spaceBetweenProblem

    row1 = row1[0:len(row1)-4]
    row2 = row2[0:len(row2)-4]
    row3 = row3[0:len(row3)-4]
    row4 = row4[0:len(row4)-4]
    
    if ans:
      arranged_problems = row1 + '\n' + row2 + '\n' + row3 + '\n' + row4
    else:
      arranged_problems = row1 + '\n' + row2 + '\n' + row3
    
    return arranged_problems