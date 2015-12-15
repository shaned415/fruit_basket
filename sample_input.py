bill_size = raw_input("How much money to start with? (5, 10, or 20)\n>")

if bill_size == '5':
    total = 500
elif bill_size == '10':
    total = 1000
else:
    total = 2000

banana, kiwi, mango, papaya, pineapple = 32, 41, 97, 254, 399

b_count = range(((total/banana)+1))
k_count = range(((total/kiwi)+1))
m_count = range(((total/mango)+1))
pa_count = range(((total/papaya)+1))
pi_count = range(((total/pineapple)+1))

for b in b_count:
    for k in k_count:
        for m in m_count:
            for pa in pa_count:
                for pi in pi_count:
                    if (banana * b) + (kiwi * k) + (mango * m) + (papaya * pa) + (pineapple * pi) == total:
                        print "Bananas: {0}, Kiwi: {1}, Mangoes: {2}, Papaya: {3}, Pineapple: {4}".format(b, k, m, pa, pi)
