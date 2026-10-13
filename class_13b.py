def total_calc(bill, tip_percent):
    tip_amount = bill * (1*0.01 * tip_percent)
    tip_amount = round(tip_amount, 2)
    print(f"please play:${tip_amount}")
    # specify only bill_amount
    # default value of percentageis taken
total_calc(150,20)