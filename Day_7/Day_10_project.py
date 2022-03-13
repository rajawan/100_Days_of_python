Oction={}
is_bid_finished=False
def highest_bidder(oction_record):
    highest_bid=0
    winner=""
    for bidder in oction_record:
        bid_amount=oction_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"{winner} is the highest bidder ")
while not is_bid_finished:
    bidder_name=input("Enter bidder name: ")
    bid_price=int(input("Enter Your bid price: $"))
    Oction[bidder_name]=bid_price
    should_continue=input("Are there any others bidder? type 'yes' or 'no' ")
    if should_continue!='yes'and should_continue !='no':
        print("Invalid input")
        break
    elif should_continue=='no':
        is_bid_finished=True
highest_bidder(Oction)