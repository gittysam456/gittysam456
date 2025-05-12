#lex_auth_012736349701922816604
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    def set_vehicle_id(self,ID):
        self.__vehicle_id=ID
    def set_vehicle_cost(self,Cost):
        self.__vehicle_cost=Cost
    def set_premium_account(self,Amount):
        self.__premium_amount=Amount
    def set_vehicle_type(self,Type):
       if Type in("Two Wheeler","Four wheeler"):
            self._vehicle_type=Type
       else:
           print("invalid vehicle type")
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def get_premium_account(self,Amount):
        return self.__premium_amount
    def get_vehicle_type(self):
            return self._vehicle_type
    def premium_amount(self):
        if self.vehicle_type=="Two wheeler":
            self.premium_amount=self.vehicle_cost * 0.02
        elif self.vehicle_type=="Four wheeler":
            self.premium_amount=self.vehicle_cost * 0.06
        else:
            print("the premium amount cannot be calculated")
        
           
    
