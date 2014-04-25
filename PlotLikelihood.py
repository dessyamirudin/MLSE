'''
Created on 7 Mar 2014

@author: TOSHIBA
'''

# A quadratic fit
import scipy.stats as ss
import matplotlib.pyplot as plt
import random
import math

def nCr(n,k):
    f=math.factorial
    return f(n)/f(k)/f(n-k)

def generate_number(p):
    if random.random()<=p:
        return 1
    else:
        return 0

def main():
    #generating number 1 to 100
    index_number=[]
    for index in range(1000):
        index_number.append(index+1)
      
    #Generating 100 data with P(data=1)=0.3
    number_100=[]
    thetha=0.3
    for ind in range(1000):
        random_1_0=generate_number(thetha)
        number_100.append(random_1_0)
    
    log_likelihood=[]
    just_likelihood=[]
    for i in range(1000):
        prob_likelihood=ss.binom.pmf(sum(number_100[:i+1]),i+1,thetha)/nCr(i+1,sum(number_100[:i+1]))
        just_likelihood.append(prob_likelihood)
        log_likelihood.append(-1*math.log(prob_likelihood))
    
    #plot the likelihood loglikelihood function
    plt.figure(1)
    
    plt.subplot(211)
    plt.plot(index_number,just_likelihood,'-')
    #plt.xlabel(r'Data Point')
    plt.ylabel('Probability')
    plt.title('likelihood P(iPhone/Bintaro)=0.3')
    plt.grid(True)
    
    plt.subplot(212)
    plt.plot(index_number,log_likelihood,'-')
    plt.xlabel(r'Data Point')
    plt.ylabel('Probability')
    plt.title('Log-likelihood P(iPhone/Bintaro)=0.3')
    plt.grid(True)
            
    plt.show()
    
    
if __name__=='__main__':
    main()



