from pulp import *


class Producer:
    def __init__(self, base, stock=0):
        self.base = base
        self.stock = stock

    def get_name(self):
        return self.base.get_base_nickname()

    def add_to_stock(self, value):
        self.stock += value

    def get_stock(self):
        return self.stock


class Consumer:
    def __init__(self, base, demand=0):
        self.base = base
        self.demand = demand

    def get_name(self):
        return self.base.get_base_nickname()

    def add_to_demand(self, value):
        self.demand += value

    def get_demand(self):
        return self.demand


class SupplyCalculator:


    @classmethod
    def calculate(cls, producers: list[Producer], consumers: list[Consumer]):
        # Creates a list of all the supply nodes
        Warehouses = []
        # Creates a dictionary for the number of units of supply for each supply node
        supply = {}

        Consumers = []
        demand = {}

        for producer in producers:
            Warehouses.append(producer.get_name())
            supply[producer.get_name()] = producer.get_stock()

        for consumer in consumers:
            Consumers.append(consumer.get_name())
            demand[consumer.get_name()] = consumer.get_demand()

        # Creates a list of costs of each transportation path
        costs = [  # Bars
            # 1 2 3 4 5
            [2, 4, 5, 2, 1],  # A   Warehouses
            [3, 7, 3, 2, 3],  # B
        ]

        # The cost data is made into a dictionary
        costs = makeDict([Warehouses, Consumers], costs, 0)

        # Creates the 'prob' variable to contain the problem data
        prob = LpProblem("Beer Distribution Problem", LpMinimize)

        # Creates a list of tuples containing all the possible routes for transport
        Routes = [(w, b) for w in Warehouses for b in Consumers]

        # A dictionary called 'Vars' is created to contain the referenced variables(the routes)
        vars = LpVariable.dicts("Route", (Warehouses, Consumers), 0, None, LpInteger)

        # The objective function is added to 'prob' first
        prob += (
            lpSum([vars[w][b] * costs[w][b] for (w, b) in Routes]),
            "Sum_of_Transporting_Costs",
        )

        # The supply maximum constraints are added to prob for each supply node (warehouse)
        for w in Warehouses:
            prob += (
                lpSum([vars[w][b] for b in Consumers]) <= supply[w],
                f"Sum_of_Products_out_of_Warehouse_{w}",
            )

        # The demand minimum constraints are added to prob for each demand node (bar)
        for b in Consumers:
            prob += (
                lpSum([vars[w][b] for w in Warehouses]) >= demand[b],
                f"Sum_of_Products_into_Bar{b}",
            )

        # The problem data is written to an .lp file
        prob.writeLP("BeerDistributionProblem.lp")

        # The problem is solved using PuLP's choice of Solver
        prob.solve()

        # The status of the solution is printed to the screen
        print("Status:", LpStatus[prob.status])

        # Each of the variables is printed with it's resolved optimum value
        for v in prob.variables():
            print(v.name, "=", v.varValue)

        # The optimised objective function value is printed to the screen
        print("Total Cost of Transportation = ", value(prob.objective))

