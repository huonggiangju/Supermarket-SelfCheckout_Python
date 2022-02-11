
from checkout import CheckoutRegister


def main():
    check_out_register = CheckoutRegister()  #create an instance of CheckoutRegister

    #looping a transaction
    while True:
        # looping for scan items
        while True:
            bar_code = input("Please enter product bar code: ").upper()
            while len(bar_code) == 0:
                bar_code = input("Barcode is invalid, please re-enter: ").upper()
            print(check_out_register.scan_item(bar_code))

            option = input("\nWould you like to scan another product? (Y/N) ").lower()
            if option == "n":
                break
            elif option != "n" and option !="y":
                print("Opp... Wrong input.")

        #looping for accept payment
        total_due = check_out_register.get_total_payment()
        input_amount = False
        while True:
            # validate input data type
            try:
                amount = float(input(f"Payment due: {total_due}\nPlease enter an amount to pay: "))
            except ValueError:
                print('That form of payment is not accepted')
            else:
                if amount < 0:  # check input <0
                    print("We do not accept negative payment")
                elif amount > 0:
                    amount_due = check_out_register.accept_payment(amount)
                    total_due -= amount  # calculate amount due
                    if total_due <= 0:
                        break

        # print receipt
        print(check_out_register.print_receipt())

        # Ask if user wants to quit or start a new sale
        next = input("Next sale or Quit? (N/Q)").lower()
        if next == "q":
            break







        # save transaction
        # check_out_register.save_transaction()


main()