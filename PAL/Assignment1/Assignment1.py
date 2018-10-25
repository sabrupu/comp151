# Write a program to create a customer’s bill for a company. The company sells only five
# different products: TV, VCR, Remote Controller, CD Player and Tape Recorder. The unit
# prices are $400.00, $220, $35.20, $300.00, and $150.00, respectively. The program must
# read the quantity of each piece of equipment purchased from the keyboard. It then
# calculates the cost of each item, the subtotal, and the total cost after an 8.25% sales tax.
# The input data consist of a set of integers representing the quantities of each item sold.
# These integers must be input into the program in a user friendly way; that is, the program
# must prompt the user for each quantity as shown below. The numbers in boldface show
# the user’s answers.
#
#     • How Many TVs Were Sold? 3
#     • How Many VCRs Were Sold? 5
#     • How Many Remote Controllers Were Sold? 1
#     • How Many CDs Were Sold? 2
#     • How Many Tape Recorders Were Sold? 4
#
# The format for the output from the program follows:
#
#   QTY     DESCRIPTION         UNIT PRICE      TOTAL PRICE
#   ---     -----------         ----------      -----------
#   XX      TV                  400.00            XXXX.XX
#   XX      VCR                 220.00            XXXX.XX
#   XX      REMOTE CTRLR         35.20            XXXX.XX
#   XX      CD PLAYER           300.00            XXXX.XX
#   XX      TAPE RECORDER       150.00            XXXX.XX
#                                                 ---------
#                               SUBTOTAL          XXXXX.XX
#                               TAX                XXXX.XX
#                               TOTAL             XXXXX.XX

print('Assignment 1')
print()

# tv        = int(input('How many TVs were sold? '))
# vcr       = int(input('How many VCRs were sold? '))
# rem_cont = int(input('How many remote controllers were sold? '))
# cd        = int(input('How many CDs were sold? '))
# tape_rec  = int(input('How many tape recorders were sold? '))
#
#
# tv_sold          = tv       * 400
# vcr_sold         = vcr      * 220
# rem_cont_sold    = rem_cont * 35.20
# cd_sold          = cd       * 300
# tape_rec_sold    = tape_rec * 150
# sum              = tv_sold + vcr_sold + rem_cont_sold + cd_sold + tape_rec_sold
#
#
# print(f'Total: {tv_sold}')
# print(f'Total: {vcr_sold}')
# print(f'Total: {rem_cont_sold}')
# print(f'Total: {cd_sold}')
# print(f'Total: {tape_rec_sold}')
# print(f'Overall sum: {sum}')


def main():
    # Cost of items
    tv = 400.00
    vcr = 200.00
    rem_cont = 35.20
    cd = 300.00
    tape_rec = 150.00

    # Get user input
    tv_sold = int(input('How many TVs were sold? '))
    vcr_sold = int(input('How many VCRs were sold? '))
    rem_cont_sold = int(input('How many remote controllers were sold? '))
    cd_sold = int(input('How many CDs were sold? '))
    tape_rec_sold = int(input('How many tape recorders were sold? '))

    # print('QTY\t DESCRIPTION\t UNIT PRICE\t TOTAL PRICE')
    # print('---\t -----------\t ----------\t -----------')
    # print(f' {tv_sold}\t TV\t\t {tv}\n {vcr_sold}\t VCR\t\t {vcr}\n {rem_cont_sold}\t REMOTE CTRL'
    #       f'\t\t {rem_cont}\n {cd_sold}\t CD PLAYER\t\t {cd}\n {tape_rec_sold}\t TAPE RECORDER\t\t {tape_rec}')


main()