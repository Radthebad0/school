print('Please enter the scores for player one.')
score_1_1=int(input())
score_2_1=int(input())
score_3_1=int(input())
score_1=score_1_1+score_2_1+score_3_1
print('Please enter the scores for player two.')
score_1_2=int(input())
score_2_2=int(input())
score_3_2=int(input())
score_2=score_1_2+score_2_2+score_3_2

print('Player one scored:',score_1)
print('Player two scored:',score_2)

if score_1 > score_2:
    print('player one wins!!')
else:
    print('player two wins!!')
