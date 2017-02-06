__author__ = 'Ashwin'

# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#
# Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
#
# What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
#
import math
import copy

def gen_die_pdf(numsides):
    vals = range(1,numsides+1)
    prob = 1.0/numsides
    probs = [prob]*numsides
    pdf_dict = dict(zip(vals,probs))
    return pdf_dict

def gen_sums_pdf(valdict1, valdict2):
    newvaldict = {}
    for val1 in valdict1.keys():
        val1prob = valdict1[val1]
        for val2 in valdict2.keys():
            val2prob = valdict2[val2]
            vals_sum = val1 + val2
            vals_prob = val1prob*val2prob
            if(vals_sum in newvaldict.keys()):
                newvaldict[vals_sum] += vals_prob
            else:
                newvaldict[vals_sum] = vals_prob

    return newvaldict

def gen_selfsum_pdf(pdf_input):
    return gen_sums_pdf(pdf_input,pdf_input)


def gen_multdie_pdf(numsides, numdice):
    num_dice_remaining = numdice
    one_die_pdf = gen_die_pdf(numsides)
    pow_2_pdfs = {0:one_die_pdf}
    partial_pdf = one_die_pdf
    while(num_dice_remaining > 0):
        pow2_to_use = int(math.log(num_dice_remaining,2))
        #if pdf  power needed is not already generated, generate it (and intervening powers)
        if(not(pow2_to_use in pow_2_pdfs.keys())):
            curr_max_pow2 = max(pow_2_pdfs.keys())
            curr_pdf = pow_2_pdfs[curr_max_pow2]
            for pow in range(curr_max_pow2+1,pow2_to_use+1):
                curr_pdf = gen_selfsum_pdf(curr_pdf)
                pow_2_pdfs[pow] = copy.deepcopy(curr_pdf)
        # then, update the current pdf accordingly
        partial_pdf = gen_sums_pdf(partial_pdf,pow_2_pdfs[pow2_to_use])
        # and reduce the number of dice left to simulate
        num_dice_remaining -= 2**pow2_to_use

    return partial_pdf


#generates dict where values are cumulative probs P(RV <= key)
def gen_cdf_from_pdf(pdf_input):
    poss_values_sorted = sorted(pdf_input.keys())
    cdf = {}
    curr_cumul_prob = 0.0
    for val in poss_values_sorted:
        curr_cumul_prob += pdf_input[val]
        cdf[val] = curr_cumul_prob

    return cdf


def get_prob_a_greater_than_b(pdf_of_a, pdf_of_b):
    prob = 0.0
    sorted_b_values = sorted(pdf_of_b.keys())
    for a_value in pdf_of_a.keys():
        a_prob = pdf_of_a[a_value]
        for b_value in sorted_b_values:
            if(b_value >= a_value):
                break
            else:
                b_prob = pdf_of_b[b_value]
                ab_prob = a_prob * b_prob
                prob += ab_prob

    return prob

peter_pdf = gen_multdie_pdf(4,8)
colin_pdf = gen_multdie_pdf(6,5)

prob_peter_wins = get_prob_a_greater_than_b(peter_pdf,colin_pdf)

print(prob_peter_wins)








#
# import random
# random.seed()
#
# def die_roll(numsides):
#     return random.randint(1,numsides)
#
# def sum_multiple_dice_roll(numsides,numdice):
#     dice_sum = 0
#     for i in range(0,numdice):
#         dice_sum += die_roll(numsides)
#     return dice_sum
#
# pete_wins = 0
# num_trials = 10**5
# for trial in range(0,num_trials):
#     if(trial%(num_trials/10) == 0):
#         print("trial " + str(trial))
#     pete = sum_multiple_dice_roll(4,9)
#     colin = sum_multiple_dice_roll(6,6)
#     if(pete > colin):
#         pete_wins += 1
# print(pete_wins)
# print(pete_wins/float(num_trials))