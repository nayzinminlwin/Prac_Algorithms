import random, sys, time

class Solution():
    def random_HelloWorld(self)->None:

        # rightString = "Hello World!"
        rightString = input("Enter the string you want me to guess: ")
        guessString = ""

        for i in range(len(rightString)):
            # print("i is ",i)
            while True:
                guess = random.randint(31,122)
                sys.stdout.write(f"\r{guessString}{chr(guess)}")
                sys.stdout.flush()
                time.sleep(0.02)
                if guess == ord(rightString[i]):
                    guessString = guessString + chr(guess)
                    break

        print("\nThe String is ",guessString)

sol = Solution()
sol.random_HelloWorld()