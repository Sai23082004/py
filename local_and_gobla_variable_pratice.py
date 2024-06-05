class amazon:
    overall_discount=5
    def __init__(self,p_id,p_name,p_price,p_discount):
        self.id=p_id
        self.name=p_name
        self.price=p_price
        self.discount=p_discount
    def final(self):
        final_price=self.price-self.price*self.discount/100-amazon.overall_discount*self.price/100
        return final_price
    
v1=amazon(1,'product1',300,15)
print(v1.final())