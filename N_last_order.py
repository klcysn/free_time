# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

class log():
    def __init__(self) :
        self.order = []
    
    

    def get_last(self):
        N = len(self.order)
        try:
            i = int(input(f"You have {N} order, please enter how many order you want to list form last : "))
            if i < N :
                for j in self.order[len(self.order)-(i):] :
                    print(j)
            else :
                raise ValueError("Number you entered must be equal or smaller than total order")

        except :
            print("Number you entered must be equal or smaller than total order!")

    def set_order(self, order_id):
        self.order.append(order_id)

    
    
