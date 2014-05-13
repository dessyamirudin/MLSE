'''
Created on 7 Mar 2014

@author: Dessy Amirudin
'''

# A quadratic fit
import scipy.stats as ss
import matplotlib.pyplot as plt
import math

def main():
    #thetha for calculation (1000 number)
    thetha=[]
    for ind in range (1000):
        thetha.append(ind/1000.0)
    
    #calculating binomial distribution
    prob_binom = ss.binom.pmf(13,50,thetha)
    maximum=max(prob_binom)
    index_max=list(prob_binom).index(maximum)
    print 'the index of highest probability'
    print index_max
    thetha_max=thetha[index_max]
    print 'the value of thetha with highest probability'
    print thetha_max
    
    #plot the likelihood function
    plt.plot(thetha,prob_binom,'-')
    plt.xlabel(r'$\theta$',fontsize=20)
    plt.ylabel('Probability')
    plt.title('Likelihood P(iPhone/Bintaro)')
    #plt.text(0.4, .12, r'$max \theta=0.26$')
    plt.show()
    
if __name__=='__main__':
    main()



