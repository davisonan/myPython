#' % Quant Analyst Skills Test
#' % Xu Tian
#' % 2017/03/14

#' # Question 1: 
#' Find a formula to price the following fixed-odds contract:
#' I wish to win _ if over the next _ days, the _ has a high-low range
#' [exceeding/not exceeding] _ points.
#' Implement the solution in the programming language of your choice. 
#' Example: I wish to win 1000 dollars if over the next 7 days the USD/JPY has 
#' a high-low range exceeding 2 points. For example, if the USD/JPY has a 
#' range of low=98.45 and high=100.98 over the next 7 days, I will win 
#' $1000 (because high – low = 2.53 > 2). You can use Monte Carlo 
#' simulation to confirm/verify your results, but it shouldn’t be the 
#' primary solution. Please provide all the relevant details about the solution.

#' **Answer**: suppose there's no interest rate and the pricing method is
#' that the expected payoff of the contract is 0. Then let the probability 
#' of winning be $p$ when the condition is satisfied, the winning amount 
#' is $Y$, then the price of the contract is $X$, the fair price is then 
#' $X=p*Y$.

#' The next question is how we can estimate the probability $p$. If the 
#' event can be historically repeated, then we can use the empirical 
#' probability by counting the number of times this event occured over
#' the number of all the possible occurances, i.e., for all 7-day windows, 
#' we can find the proportion of windows that the high-low range exceeds 2 
#' points and plug this number in the above equation. This is the naive 
#' approach. We can also take the current market conditions into 
#' considersation, such as the volatilities, etc. This would essentially 
#' be training a logistic regression model. An even more advanced/sophisticated 
#' model can be built by taking more factors into consideration and build even 
#' more sophisticated predictive models, such as neural networks, extreme 
#' boosted trees, support vector machines, random forest models, etc. These 
#' models can all estimate the probability of the aforementioned event.

#' A Monte Carlo of the first idea is explored. Historical USD/JPY rates
#' are given since Jan. 4 1971. Here I'm assuming the next 7 days 
#' is about 7 calendar days. If 2 days are missing in a 7-day 
#' window, it's tolerable in calculating the high-low range. Besides, overlapping
#' window approach is chosen over the non-overlapping approach since we do want
#' to have the 7-day forecast starting at any day, not on any specific days.
#' The following code is doing just that.

import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as wb

start = datetime.datetime(1970, 1, 1)
end = datetime.date.today()
df = wb.DataReader("DEXJPUS", 'fred', start, end)
His = df.rolling(window=7, min_periods=5).max()
Los = df.rolling(window=7, min_periods=5).min()
hiloRange = His - Los

plt.figure()
plt.plot(hiloRange)
plt.title("The time series of historical rolling 7-day hi-lo range for USD/JPY")
plt.xlabel("Time")
plt.ylabel("Hi-lo range")

hiloRange = hiloRange.reset_index()['DEXJPUS'].dropna()

plt.figure()
plt.hist(hiloRange, 50, normed=1, facecolor='blue', alpha=0.75)
plt.title("The histogram of historical rolling 7-day hi-lo range for USD/JPY")
plt.xlabel("7-day hi-lo range")
plt.ylabel("Frequency")

#' The above graph shows the distribution of historical 7-day hi-lo ranges,
#' and the probability of the winning condition is calculated empirically as
#' 0.456, and the fair price is then 456 dollars.
print(np.mean(hiloRange > 2))

#' However, if we look at the historical time series closely, apparently, the 
#' volatility in earlier time is higher than that in recent time. This is related
#' to the second idea above. Here we try the same idea simply using the data after 
#' 2002 and here's the result.

start = datetime.datetime(2002, 1, 1)
end = datetime.date.today()
df = wb.DataReader("DEXJPUS", 'fred', start, end)
His = df.rolling(window=7, min_periods=5).max()
Los = df.rolling(window=7, min_periods=5).min()
hiloRange = His - Los

plt.figure()
plt.plot(hiloRange)
plt.title("The time series of historical rolling 7-day hi-lo range for USD/JPY")
plt.xlabel("Time")
plt.ylabel("Hi-lo range")

hiloRange = hiloRange.reset_index()['DEXJPUS'].dropna()

plt.figure()
plt.hist(hiloRange, 50, normed=1, facecolor='blue', alpha=0.75)
plt.title("The histogram of historical rolling 7-day hi-lo range for USD/JPY")
plt.xlabel("7-day hi-lo range")
plt.ylabel("Frequency")

#' Apparently the histogram is much narrowed towards the smaller values, and 
#' the probability higher than 2 in this period has dropped to 0.314. If
#' we use this probability to price the contract, the fair price would be 
#' reduced to about 314 dollars. 

print(np.mean(hiloRange > 2))

#' The fair price of the contract depends on the way we calculate 
#' it. Based on the above two illustrations and the other ideas mentioned above, 
#' the price of the contract can be more accurate in a sense that the expected 
#' payoff of the contract should be 0 in the long term.

#' # Question 2:
#' Simulate the following situation. Attach the code as part of your submission.
#' At a post office, customers enter a single line waiting to be served by any 
#' one of two clerks. Every minute there is a 60% chance that a new customer 
#' arrives. If there is no one in line and a server is free, the customer does 
#' not wait to be served. When a customer is being served there is a 25% chance 
#' every minute that they complete their business and leave. When the clerk is 
#' free he will take the next customer in line, in the order that they arrived.
#' Every minute, there is a 5% chance that a person standing in line will give 
#' up and leave. The post office is always open (24/7/365).
#' Note: For simplicity you can assume customers will always arrive at the 
#' beginning of the minute and if they leave they do so at the end of the 
#' minute.
#' a) What is the average amount of time a customer spends in the post office 
#' (including those not served)?
#' b) What percentage of customers leave without being served?
#' c) What percentage of time are the clerks idle?

from collections import deque
import random, time

# A Customer class
class Customer(object):
    def __init__(self, arrivalTime):
        self.arrivalTime = arrivalTime
    def depart(self, departureTime):
        self.departureTime = departureTime
    def calTime(self):
        return self.departureTime - self.arrivalTime + 1

# A Simulator class
class Simulator(object):
    def __init__(self, pNewArrive, pComplete, pLeave):
        self.pNewArrive = pNewArrive
        self.pComplete = pComplete
        self.pLeave = pLeave
        self.nMin = 365 * 24 * 60
        self.iFreeA, self.iFreeB = True, True
        self.totalTimeA, self.totalTimeB = 0, 0  # working time
        self.countA, self.countB = 0, 0  # num served by A and B
        self.totalTimeCustomer = 0  # total time
        self.counter = 0  # num of customers 1) served or 2) left
        self.line = deque([])

        def f(p):
            def g():
                return 1 if random.random() < p else 0
            return g

        self.simNewArrive = f(pNewArrive)
        self.simComplete = f(pComplete)
        self.simLeave = f(pLeave)

    def sim(self):
        for t in range(self.nMin):
            # Simulate the arrival stage
            if self.simNewArrive():
                self.counter += 1
                aNewCustomer = Customer(t)
                self.line.append(aNewCustomer)
            
            # Simulate the service at A
            if self.iFreeA and len(self.line) > 0:
                customerAtA = self.line.popleft()
                self.iFreeA = False
                self.countA += 1
                self.totalTimeA -= t
                
            # Simulate the service at B
            if self.iFreeB and len(self.line) > 0:
                customerAtB = self.line.popleft()
                self.iFreeB = False
                self.countB += 1
                self.totalTimeB -= t

            # Simulate the completion at A.
            if not self.iFreeA and self.simComplete():
                self.iFreeA = True
                self.totalTimeA += t + 1
                customerAtA.depart(t)
                self.totalTimeCustomer += customerAtA.calTime()
            
            # Simulate the completion at B
            if not self.iFreeB and self.simComplete():
                self.iFreeB = True
                self.totalTimeB += t + 1
                customerAtB.depart(t)
                self.totalTimeCustomer += customerAtB.calTime()

            # Simulate the actions in queue
            if len(self.line) > 0:
                j = 0
                while True:
                    try:
                        if self.simLeave():
                            customerToLeave = self.line[j]
                            customerToLeave.depart(t)
                            waitTime = customerToLeave.calTime()
                            self.totalTimeCustomer += waitTime
                            self.line.remove(customerToLeave)
                        else:
                            j += 1
                    except:
                        break
        else:
            if not self.iFreeA:
                self.countA -= 1
                self.counter -= 1
                customerAtA.depart(t)
                self.totalTimeA += t + 1
                self.totalTimeA -= customerAtA.calTime()
            if not self.iFreeB:
                self.countB -= 1
                self.counter -= 1
                customerAtB.depart(t)
                self.totalTimeB += t + 1
                self.totalTimeB -= customerAtB.calTime()
            if len(self.line) > 0:
                self.counter -= len(self.line)

    def showResult(self):
        print('The average time a customer spends in the post office is: %.2f minutes.' %(self.totalTimeCustomer/self.counter))
        print('The percentage of customers leave without being served is {0:.02f}%.'.format((1-(self.countA+self.countB)/self.counter)*100))
        print('The percentage of time the clerks are idle is {0:.02f}%.'.format((1-(self.totalTimeA+self.totalTimeB)/(2*self.nMin))*100))

pNewArrive = 0.6
pComplete = 0.25
pLeave = 0.05
aSim = Simulator(pNewArrive, pComplete, pLeave)
aSim.sim()
aSim.showResult()


#' # Question 3:
#' Sports teams 'A' and 'B' are to play each other until one has four wins and 
#' is declared the series winner. You have 100 dollars to bet on Team A to win the 
#' series. You are, however, only allowed to bet on individual games, not the 
#' final outcome directly, and you must bet a positive amount on each game. 
#' So, if Team A wins the series, you must walk away with 200 dollars, but if Team A 
#' loses the series, you must walk away with zero, and you must do so having 
#' placed a non-zero bet on every game. How do you place your bets?

#' The detals can be found in the attached spreadsheet. The basic idea is we 
#' could find the boundary conditions of the game, for example, after 7 games, 
#' the results are either four wins and three losses (4-3) or three wins and 
#' four losses (3-4) with the corresponding balances as 200 dollars or 0 
#' dollars. In order to achieve these numbers, at game 6, if the result is 
#' 3-3, then the balance must be 100 dollars, which is the average of the next
#' two outcomes, since the same amount is either won or lost from the current 
#' balance. Therefore, the betting amount of the current game is simply the 
#' balance of the winning outcome minus the current balance, i.e., 200 - 100 is
#' 100 dollars.

#' Using this logic, we work out the balances backwards from game 7 with 
#' the other boundary conditions like 4-2, 4-1, 4-0 having 200 dollars and 2-4,
#' 1-4 and 0-4 having 0 dollars. After calculating these balances, the bet 
#' at each win-loss condition can be easily calculated. The attached speadsheet
#' contains the exact numbers.