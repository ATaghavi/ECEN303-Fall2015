__author__ = "Eric Niyigaba"
__NetID__ = "ericniyigaba"
__GitHubID__ = "ericniyigaba"
__challenge__ = "1"
__version__ = "0.0"
__grader__ = ""
__SelfGrade__ = "4"
__PeerGrade__ = ""


"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""
import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
      if random.random() <= p:
        return 1
      else:
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    NumberHeads = 0

    for TrialIndex3 in range(0, NumberFlips):
        NumberHeads += biasedcoinflip(ParameterP)
    
    SumTrials.append(NumberHeads)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips+1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
Sum = 0
for OutcomeIndex3 in range(0, NumberFlips + 1):
    Sum += Distribution[OutcomeIndex3]
print(Sum)

OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

"""
Describe what happens to the figure as you vary ParameterP from zero to one.
 As ParameterP approaches 0,the probability distribution tend to approach 0 as well.
 the same thing happens as the probability approaches 1, the distribution also approcheases 1 too.
 Also when ParameterP = 0, the probability distribution is located at 0 but for Parameter= 1, 
 the probability is on the top of 1 at ParameterP = 1,
 
What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
the most likely is 6 heads out of 8 flips.  as it can be calculated: 0.7*8 = 5.6 which is almost 6
