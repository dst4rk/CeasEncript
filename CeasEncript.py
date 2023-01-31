import argparse,sys
import shlex


def encriptor(unencryptedtext,n):
    result = ""
    for le in range (len(unencryptedtext)):
        c = unencryptedtext[le] 
        if (c.isupper()):
            result += chr((ord(c) + n - 65) % 26 + 65)
        else:
            result += chr((ord(c) + n - 97) % 26 + 97)
    return result 
     

def desencriptor(encryptedtext,n):
    result = ""
    for le in range (len(encryptedtext)):
        c = encryptedtext[le] 
        if (c.isupper()):
            result += chr((ord(c) - n - 65) % 26 + 65)
        else:
            result += chr((ord(c) - n - 97) % 26 + 97)    
    return result
        
def main():
    parser = argparse.ArgumentParser(description="Text Encryption and Decryption Tool using the Ceasar rule")
    parser.add_argument("-e", type=str, help="Encrypts text using the Ceasar rule, to enter the text to be encrypted use double quotation marks")
    parser.add_argument("-d", type=str, help="Deciphering text using Ceasar rule")
    args = parser.parse_args()
    n = 5
    if args.e:
        text = str(shlex.split(" ".join(sys.argv[1:])))
        print('The encrypted text is: ', encriptor(text,n))
    elif args.d:
        text = str(shlex.split(" ".join(sys.argv[1:])))
        print('The decrypted text is : ',str(desencriptor(text,n))[16:-4].replace("uznu", " "))

def run():
    print("Welcome to the Ceaser Encriptor and Descriptor Tool \n")
    if len(sys.argv) < 2:
        print("Please enter -h for help")
    else:
        main()
        
if __name__ == '__main__':
    run()

# Maicker M. Ravelo Flores :) - Dstark