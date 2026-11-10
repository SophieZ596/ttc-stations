import math


def hours_needed(num_a, num_b):
    """Returns the hours it takes to make num_a of Product A and num_b
    of Product B."""
    hours_a = 3.5
    hours_b = 4.25
    return num_a * hours_a + num_b * hours_b


def profit(num_a, num_b):
    """Returns the profit, in dollars, from selling num_a of Product A
    and num_b of Product B."""
    profit_a = 10
    profit_b = 12.5
    return num_a * profit_a + num_b * profit_b

def best_plan(hours_available, boards_in_stock):
    """Returns [num_a, num_b, profit] for the most profitable plan that
    can be made in hours_available hours.  If several plans tie,
    returns the first one found, with num_a counting up in the outer
    loop and num_b in the inner one."""
    max_a = math.floor(hours_available / hours_needed(1, 0))
    max_b = math.floor(hours_available / hours_needed(0, 1))
    best = [0, 0, profit(0, 0)]
    for num_a in range(max_a + 1):
        for num_b in range(max_b + 1):
            if fits(num_a, num_b, hours_available, boards_in_stock):
                plan_profit = profit(num_a, num_b)
                if plan_profit > best[2]:
                    best = [num_a, num_b, plan_profit]
    return best

def boards_needed(num_a, num_b):
    return 3*num_a + 4*num_b

def fits(num_a, num_b, hours_available, boards_in_stock):
    return (hours_needed(num_a, num_b) <= hours_available and boards_needed(num_a, num_b) <= boards_in_stock)

def main():
    hours_available = 40
    boards_in_stock = 32
    plan = best_plan(hours_available, boards_in_stock)
    print("Make", plan[0], "of Product A and", plan[1], "of Product B.")
    print("Profit: $", plan[2], sep="")


if __name__ == "__main__":
    main()