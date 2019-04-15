profitGoal = 1000000

class Amulet():
    cost_pU = 95.00
    salePrice_pU = 200.00


box = 50*Amulet.cost_pU
costOfOnD = 6000
Order = lambda n: (n*Amulet.cost_pU) + 6000
rushOrder = lambda n:n*(Amulet.cost_pU + 40) + 6000

#Includes warehouse rental costs and insurance
costOfInventoryHolding_pU = 1.35


print(387/48)