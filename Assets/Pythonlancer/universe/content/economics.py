from pulp import *


class Producer:
    def __init__(self, base, stock=0):
        self.base = base
        self.stock = stock

    def get_name(self):
        return self.base.get_name()

    def get_stock(self):
        return self.stock


class Consumer:
    def __init__(self, base, demand, distance=0):
        self.base = base
        self.demand = demand
        self.distance = distance

    def get_name(self):
        return self.base.get_name()

    def get_demand(self):
        return self.demand

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance


class SupplyCalculator:

    @classmethod
    def calculate(cls, commodity_producers, commodity_consumers):
        # Creates a list of all the supply nodes
        the_producers = []
        # Creates a dictionary for the number of units of supply for each supply node
        supply = {}
        # Creates a list of all demand nodes
        the_consumers = []
        # Creates a dictionary for the number of units of demand for each demand node
        demand = {}
        # Creates a list of costs of each transportation path
        costs = []

        for producer in commodity_producers:
            the_producers.append(producer.get_name())
            supply[producer.get_name()] = producer.get_stock()

            costs_item = []

            for consumer in commodity_consumers:
                costs_item.append(
                    producer.base.graph.get_depth_by_base_name(consumer.get_name())
                )
            costs.append(costs_item)

        for consumer in commodity_consumers:
            the_consumers.append(consumer.get_name())
            demand[consumer.get_name()] = consumer.get_demand()

        # The cost data is made into a dictionary
        costs = makeDict([the_producers, the_consumers], costs, 0)

        # Creates the 'prob' variable to contain the problem data
        prob = LpProblem("Beer Distribution Problem", LpMinimize)

        # Creates a list of tuples containing all the possible routes for transport
        Routes = [(w, b) for w in the_producers for b in the_consumers]

        # A dictionary called 'Vars' is created to contain the referenced variables(the routes)
        vars = LpVariable.dicts("Route", (the_producers, the_consumers), 0, None, LpInteger)

        # The objective function is added to 'prob' first
        prob += (
            lpSum([vars[w][b] * costs[w][b] for (w, b) in Routes]),
            "Sum_of_Transporting_Costs",
        )

        # The supply maximum constraints are added to prob for each supply node (warehouse)
        for w in the_producers:
            prob += (
                lpSum([vars[w][b] for b in the_consumers]) <= supply[w],
                f"Sum_of_Products_out_of_Warehouse_{w}",
            )

        # The demand minimum constraints are added to prob for each demand node (bar)
        for b in the_consumers:
            prob += (
                lpSum([vars[w][b] for w in the_producers]) >= demand[b],
                f"Sum_of_Products_into_Bar{b}",
            )

        # The problem is solved using PuLP's choice of Solver
        prob.solve()

        # The status of the solution is printed to the screen
        print("Status:", LpStatus[prob.status])

        # Each of the variables is printed with it's resolved optimum value
        for v in prob.variables():
            print(v.name, "=", v.varValue)

        # The optimised objective function value is printed to the screen
        print("Total Cost of Transportation = ", value(prob.objective))

