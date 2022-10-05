# Start writing your functions below this line

'''defining the parts of the egg
Top of the egg'''
def eggTop():
    print("   ————————")
    print(" /          \\")
    print("/            \\")

    #Bottom of the egg
def eggBottom():
    print("\\            /")
    print(" \\          /")
    print("   ————————")
def eggLine():
    print(" —\"—'—\"—'—\"—")
    #print(" —" """"—'—" """ "—'—"""""—""")

#defining main function
def main():
    for x in range(2):
        eggTop()
        eggBottom()
        eggLine()
    eggBottom()
    eggTop()
    eggLine()
    eggBottom()

#executing main function
main()

'''
execution of the functions:
'''



'''
def main():
    # all of your function calls should go here. Remove the word "pass" before adding function calls.
    pass

if __name__ == '__main__':
    main()
'''