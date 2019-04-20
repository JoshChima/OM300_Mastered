import math
#D = Demand
#S = Settingup/Order cost
#H = Holding cost
#Q = EOQ = Q* = Per Order Quantity
EOQ = lambda D,S,H: math.sqrt((2*D*S)/H)
Order_Cost = lambda Numof_Orders,perOrder_Cost: Numof_Orders*perOrder_Cost
Holding_Cost = lambda Ave_inv, Holdingcost_perunit_peryear: Ave_inv*Holdingcost_perunit_peryear
Average_inventory = lambda Q: Q/2
Annual_Holding_Costs = lambda Q,H: (Q/2)*H
Optimal_Num_Orders = lambda Annu_D, Q: Annu_D/Q
Numof_Daysbetween_Twosubsequent_Orders = lambda Op_days,Numof_Orders: Op_days/Numof_Orders
Total_Ordering_andHolding_Cost = lambda Order_Cost,Holding_Cost: Order_Cost+Holding_Cost
Total_Annual_Inventory_Cost = lambda Total_Ordering_andHolding_Cost,Total_Costof_Goods_Sold: Total_Ordering_andHolding_Cost+Total_Costof_Goods_Sold
ROP = lambda d,L: d*L
d = lambda D,Numof_Workingdays_ayear: D/Numof_Workingdays_ayear
#print(EOQ(5900,(29.13),(8.81)))
#print(Average_inventory(197.53))
#print(Optimal_Num_Orders(5900,197.53))
#print(Numof_Daysbetween_Twosubsequent_Orders(250,29.87))
#print(Total_Ordering_andHolding_Cost(Order_Cost(29.87,29.13),Holding_Cost(98.77,8.81)))
#print(Total_Annual_Inventory_Cost(1740.28,(5900*99.44)))

print(EOQ(14400,75,26))
print(Annual_Holding_Costs(288,26))
print(Order_Cost(Optimal_Num_Orders(14400,288),75))
print(ROP(d(14400,300),3))
#print(Numof_Daysbetween_Twosubsequent_Orders(250,27.71))
#print(Total_Ordering_andHolding_Cost(Order_Cost(27.71,31),Holding_Cost(107.37,8)))
#print(Total_Annual_Inventory_Cost(1717.97,5950*105))

#print(EOQ(5000,30,50))
#print(Average_inventory(77.46))
#print(Optimal_Num_Orders(5000,77.46))
#print(Numof_Daysbetween_Twosubsequent_Orders(250,64.55))
#print(Total_Ordering_andHolding_Cost(Order_Cost(64.55,30),Holding_Cost(38.73,50)))
#print(Total_Annual_Inventory_Cost(3873,0))
#print(ROP(d(5000,250),10))
