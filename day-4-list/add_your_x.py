row1=['😁','😁','😁']
row2=['😁','😁','😁']
row3=['😁','😁','😁']

emojis=[row1,row2,row3]
print(f'{emojis[0]}\n{emojis[1]}\n{emojis[2]}\n')

replace=input('enter in which entity do you want to replace\n row first then column eg(23): ')

row=int(replace[0])
col=int(replace[1])

emojis[row-1][col-1]='😍'

print(f'{emojis[0]}\n{emojis[1]}\n{emojis[2]}\n')