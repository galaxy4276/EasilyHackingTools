
# here is a new iteration of the password cracker so for this project we are going to crack a 3 letter password

# Rules: 1- only lowercase letter , 2 - letters from a to a to h only


class Cracking_code:

    def Insert_password():

        password = input("Insert the password for your creditcard only two digits since you will be scammed soon:")

        return password

    def Password_Cracker():

        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        all_permutations = []

        Password_haha = Cracking_code.Insert_password()

        for i in range(0, len(alphabets) - 2):

            pointer_1 = alphabets[i]

            for j in range(i + 1, len(alphabets) - 1):

                pointer_2 = alphabets[j]

                for k in range(j + 1, len(alphabets)):

                    pointer_3 = alphabets[k]

                    # all the possible combinations of the allphabets
                    string_join1 = pointer_1 + pointer_2 + pointer_3
                    string_join2 = pointer_1 + pointer_3 + pointer_2
                    string_join3 = pointer_2 + pointer_1 + pointer_3
                    string_join4 = pointer_2 + pointer_3 + pointer_1
                    string_join5 = pointer_3 + pointer_2 + pointer_1
                    string_join6 = pointer_3 + pointer_1 + pointer_2

                    if string_join1 == Password_haha:

                        return("We found it:", string_join1)

                    elif string_join2 == Password_haha:

                        return("We found it:", string_join2)

                    elif string_join3 == Password_haha:

                        return("We found it:", string_join3)

                    elif string_join4 == Password_haha:

                        return("We found it:", string_join4)

                    elif string_join5 == Password_haha:

                        return("We found it:", string_join5)

                    elif string_join6 == Password_haha:

                        return("We found it:", string_join6)