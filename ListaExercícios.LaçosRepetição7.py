thanos = 1.50
ha = 1.10
anos=0
for i in range(1,100):
    thanos+=0.02
    ha+=0.03
    anos+=1
    if ha > thanos:
        break
print(f'A quantidade de anos é: {anos}')
