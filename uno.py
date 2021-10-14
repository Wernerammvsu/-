transposeHorizontal = '32145'
transposeVertical = '24351'
N = 5

print('Text the message (25 symbols is maximum available)')
message = input()


messageMatrix = [' '] * N
for i in range(5):
    messageMatrix[i] = [' '] * N

length = len(message)
if length > N * N:
    print('In message more symbols then available')
def printMatrix(matrix):
    print('-----------------------------------')
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print('')

    print('-----------------------------------')


for i in range(N):
    for j in range(N):
        pos = i * N + j
        if pos < length:
            messageMatrix[i][j] = message[pos]

print('messageMatrix')
printMatrix(messageMatrix)

encryptedMessageMatrix = [' '] * N
for i in range(N):
    encryptedMessageMatrix[i] = [' '] * N

for i in range(N):
    for j in range(N):
        encryptedMessageMatrix[i][j] = messageMatrix[int(transposeVertical[i])-1][int(transposeHorizontal[j])-1]

print('')
print('encryptedMessageMatrix')
printMatrix(encryptedMessageMatrix)

encryptedMessage = ''
for i in range(N):
    for j in range(N):
        encryptedMessage += encryptedMessageMatrix[i][j]
print('encryptedMessage:',encryptedMessage)

receivedEncryptedMessage = encryptedMessage
print('receivedEncryptedMessage:',receivedEncryptedMessage)

receivedEncryptedMessageMatrix = [' '] * N
for i in range(N):
    receivedEncryptedMessageMatrix[i] = [' '] * N

for i in range(N):
    for j in range(N):
        receivedEncryptedMessageMatrix[i][j] = receivedEncryptedMessage[i * N + j]

print('receivedEncryptedMessageMatrix')
printMatrix(receivedEncryptedMessageMatrix)

disencryptedMessageMatrix = [' '] * N
for i in range(N):
    disencryptedMessageMatrix[i] = [' '] * N

for i in range(N):
    for j in range(N):
        disencryptedMessageMatrix[int(transposeVertical[i])-1][int(transposeHorizontal[j])-1] = receivedEncryptedMessageMatrix[i][j]


print('disencryptedMessageMatrix')
printMatrix(disencryptedMessageMatrix)

disencryptedMessage = ''
for i in range(N):
    for j in range(N):
        disencryptedMessage += disencryptedMessageMatrix[i][j]

print('disencryptedMessage:',disencryptedMessage)