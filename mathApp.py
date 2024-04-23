import time
import random

def get_divisor(n):
    l = []
    for i in range(1,n+1):
        if n%i ==0:
            l.append(i)
    return random.choice(l)

if 31==31:
    total = 0
    correct = 0
    questions = []
    ops = ['+','-','*','/']
    start_time = time.time()
    
    while time.time()-start_time<=60:
        a = random.randint(1,99)
        op = random.choice(ops)

        if op == '/':
            b = get_divisor(a)

        elif op == '*':
            b = random.randint(1,10)

        else:
            b = random.randint(1,99)
        a_op_b = '{}{}{}'.format(a,op,b)


        c = int(eval(a_op_b))

        try:
            ans = int(input('{} = '.format(a_op_b)))
        except:
            ans = ''
        
        if time.time()-start_time<=60:
            if ans == c:
                print("Correct ! Time remain {} seconds.".format(60-(time.time()-start_time)))
                correct +=1
            else:
                print("Wrong ! Time remain {} seconds.".format(60-(time.time()-start_time)))
                total += 1
                questions.append('{}={}'.format(a_op_b,ans))
    
    print("{} questions and your correct rate is {:.2f}%".format(total,correct/total*100))
        